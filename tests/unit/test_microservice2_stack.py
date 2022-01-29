import aws_cdk as core
import aws_cdk.assertions as assertions

from microservice2.microservice2_stack import Microservice2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in microservice2/microservice2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Microservice2Stack(app, "microservice2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
