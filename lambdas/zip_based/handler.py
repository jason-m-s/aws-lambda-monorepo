import boto3

from common.util_one import greeting


def test_handler(event, context):
    print(f"zip_based -> test_handler")
    name = context.get('name') if context else 'No Name'
    print(greeting(name))
