FROM lambda_slatemath:latest

RUN yum install unzip -y
COPY lambdas.container_based/lambda.zip .
RUN unzip lambda.zip && rm lambda.zip
CMD ["lambda_function.handler"]

