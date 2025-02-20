python_sources()

python_aws_lambda_function(
    name="lambda",
    handler="handler.py:lambda_handler"
)

docker_image(
    name="my_image",
    dependencies = [":lambda"],
)