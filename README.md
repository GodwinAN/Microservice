# Microservice (BMI Calculator)

Cloud Continuous Delivery of Microservice (MLOps or Data Engineering Focused)

Objectives
1. Create a Microservice in Flask or Fast API
2. Push source code to Github
3. Configure Build System to Deploy changes
4. Use IaC (Infrastructure as Code) to deploy code
5. Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
6. Containerization is optional, but recommended


# Significance
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²

# Impementation
The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

# Solution
Let’s make finding out your BMI quicker and easier, by creating a program that takes a 
person's weight and height as input and outputs the corresponding BMI category.

# Sample Input
weight(kgs) = 85
Height(cms) = 150

# Sample Output
BMI: XX
Grade: Normal



#SERVICES USED : AWS CDK(Cloud development kit), AWS Cloud9, AWS Lambda

## Summary of Steps
1. Create git hub repository
2. Create new environment in AWS cloud9

3. Setup CDK environment in cloud9
  cdk --version - install cdk
  npm install -g aws-cdk@1.x. - install cdk version
  cdk init app --language python. - initialise CD4 app dependencies and creates CDK environment
  source .venv/bin/activate. - activate virtual environment
  python -m pip install -r requirements.txt. - install requirements
  cdk ls - verify everything is working
  mkdir lambda - make the lambda directory for the app
  touch lambda/lambda_function.py - create a microservice in the .py with "event and context" specified formatting of AWS lambda service
  Make sure to connect ASW lambda to CDK using the "_stack.py" file generated by CDK
  cdk diff. - check for differences between local and remote code versions
  cdk deploy - Deploy the app 
  cdk bootstrap - You may find this useful incase of any errors
  
4. By now the app is deployed, go to AWS lambda and check the latest modified functions
5. Test your function to see that it works well.

Thank you!




