
"""This code calculates Body Mass Index"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()
"""This code returns BMI"""
@app.get("/")
async def root():
    return{"Welcome to the Body mass index(BMI) calculator, Please enter your Weight in kilograms and Height in meters"}

@app.get("/bmi_calculator/{weight}/{height}")
def bmi_calculator(weight, height):
    bmi = round((float(weight)/(float(height)**2)),2)
    if bmi <= 18.5:
        return{ float(bmi) : "You are below standard body mass, you should eat food rich in fats and eat regularly"}
    elif bmi >= 18.5 and bmi <= 24.9:
        return{ float(bmi) : "You have a normal standard weight"}
    elif bmi >= 25 and bmi <= 29.9:
        return{ float(bmi) : "You over weighed normal standard weight"}
    else: 
        return{ float(bmi) : "You have obesity and needs quick medical attention"}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
