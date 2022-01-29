from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class Microservice2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        my_lambda = _lambda.Function(
             self, "expohandler",
             runtime =_lambda.Runtime.PYTHON_3_7,
             code =_lambda.Code.from_asset('lambda'),
             handler ='expo.lambda_handler'
             #visibility_timeout=Duration.seconds(300),
             )
         
        
