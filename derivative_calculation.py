# from sympy install 
import boto3; lambda_client = boto3.client('lambda'); response = lambda_client.invoke(FunctionName='your_splunk_function', InvocationType='Event', Payload=json.dumps({'logs': 's3://your-bucket-name/CloudTrailLogs/*'}))

lambda_function = aws_lambda.Function(self, "CloudWatchToSplunk",
    runtime=aws_lambda.Runtime.PYTHON_3_8,
    handler="index.handler",
    code=aws_lambda.Code.from_inline("""
import json
import boto3
import requests

def handler(event, context):
    splunk_url = 'https://your-splunk-url'
    headers = {'Authorization': 'Splunk your-splunk-token'}
    for record in event['Records']:
        payload = json.loads(record['body'])
        requests.post(splunk_url, headers=headers, data=json.dumps(payload))
"""),
    events=[aws_lambda_event_sources.SqsEventSource(sqs.Queue(self, "Queue"))]
)



aws_logs.CfnSubscriptionFilter(self, "CloudWatchToSplunk",
    log_group_name="/aws/lambda/your-log-group",
    filter_pattern="",
    destination_arn="arn:aws:firehose:your-region:your-account-id:deliverystream/your-stream-name"
)

# python oneliner code for creating decorator which will accept only integer and string parameters

def validate_args(func): return lambda *args, **kwargs: func(*args, **kwargs) if all(isinstance(arg, (int, str)) for arg in args) and all(isinstance(v, (int, str)) for v in kwargs.values()) else ValueError("Only int and str arguments are allowed!")

@validate_args
def my_function(a, b):
    return f"{a} and {b}"

print(my_function(42, "hello"))  # Valid
print(my_function(42, 3.14))     # Raises ValueError
