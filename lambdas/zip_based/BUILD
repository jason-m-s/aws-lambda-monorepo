# TODO:
# 1. Check how the runtime of python_aws_lambda_function can be externalised so that it can be set in pants.toml

python_aws_lambda_function(
    name="lambda",
    handler="handler.py:test_handler",
    architecture="x86_64",
    output_path='${spec_path_normalized}/zome.zip'
)

python_sources()

python_requirements(
    name="reqs",
)
