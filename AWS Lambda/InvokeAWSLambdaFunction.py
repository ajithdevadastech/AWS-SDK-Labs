import boto3
import json
import urllib.parse

# Create a client for the AWS Lambda service
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id='AKIAROUC5Z7H4445TBED',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

# Lambda function name
function_name = 'educative_echo'

# URL parameter
param = 'date'

# Encode the parameter value for safe transmission in the URL
encoded_param = urllib.parse.quote(param)


# Construct the query string parameter as a dictionary
query_params = {'param': encoded_param}

response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',
    Payload=json.dumps({'queryStringParameters': query_params})
)

print('Status code:', response['StatusCode'])
result = json.loads(response['Payload'].read().decode())
print('Result:', result)