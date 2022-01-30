# This is my prototype code for testing the data pipeline (CLOUD9,CDK,LAMBDA)

def lambda_handler(event, context):
    if event["name"] == "expo":
        return "Expo date is 10/30/2021"
