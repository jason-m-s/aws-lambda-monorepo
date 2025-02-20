# TODO:
# 1. Check how the runtime of python_aws_lambda_function can be externalised so that it can be set in pants.toml
python_sources()

python_aws_lambda_function(
    name="lambda",
    handler="handler.py:test_handler",
    architecture="x86_64",
    include_requirements=False,
)

python_aws_lambda_layer(
    name="layer",
    # specify the handler file, and pants will automatically find its transitive dependencies
    dependencies=["./handler.py"],
    # only include the boto3 requirement, any sources are packaged in `:function`
    include_sources=False,
)

python_requirements(
    name="reqs",
)
