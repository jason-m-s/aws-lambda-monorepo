# Test Pants Project
This is a test project to test pants build system.

## How to package
```bash
pants package <path/to/lambda_dir>:<lambda_name>
```
Ex. `pants package lambdas/zip_based/:lambda`

This will create a zip file in the dist directory.

## How to run manually
```bash
python -c "import sys; sys.path.insert(0, '<path/to/zip_file.zip>'); from lambda_function import handler; handler(None, None)
```
Ex. `python -c "import sys; sys.path.insert(0, 'dist/lambdas.zip_based/lambda.zip'); from lambda_function import handler; handler(None, None)`
If you want to pass any arguments, you can pass them as a dictionary to the handler function.

Ex. `python -c "import sys; sys.path.insert(0, 'dist/lambdas.zip_based/lambda.zip'); from lambda_function import handler; handler(None, {'name': 'test'})"`
