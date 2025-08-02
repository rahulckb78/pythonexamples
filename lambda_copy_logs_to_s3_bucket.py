import boto3

# One-liner lambda function
cloudwatch_to_s3 = lambda log_group, s3_bucket, s3_key: boto3.client('s3').put_object(Bucket=s3_bucket, Key=s3_key, Body=boto3.client('logs').get_log_events(logGroupName=log_group, limit=100)['events'][0]['message'])

# Example usage
cloudwatch_to_s3('my-log-group', 'my-s3-bucket', 'my-s3-key')




import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_boto3(monkeypatch):
    mock_logs = MagicMock()
    mock_logs.get_log_events.return_value = {'events': [{'message': 'test log message'}]}
    mock_s3 = MagicMock()
    monkeypatch.setattr('boto3.client', lambda x: mock_logs if x == 'logs' else mock_s3)
    return mock_logs, mock_s3

def test_cloudwatch_to_s3(mock_boto3):
    mock_logs, mock_s3 = mock_boto3
    cloudwatch_to_s3('my-log-group', 'my-s3-bucket', 'my-s3-key')
    
    # Assertions
    mock_logs.get_log_events.assert_called_once_with(logGroupName='my-log-group', limit=100)
    mock_s3.put_object.assert_called_once_with(Bucket='my-s3-bucket', Key='my-s3-key', Body='test log message')