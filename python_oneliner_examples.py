MyClass = type("MyClass", (object,), {"x": 10, "hello": lambda self: "Hello, world!"})

obj = MyClass()
print(obj.x)
print(obj.hello())

import sys, boto3, pyspark.sql.functions as F; glue = boto3.client("glue"); job = glue.create_job(Name="SalesforceGlueJob", Role="MyIAMRole", Command={"Name": "glueetl", "ScriptLocation": "s3://my-bucket/scripts/salesforce_glue.py"})
