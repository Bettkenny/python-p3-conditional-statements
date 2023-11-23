#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" or "ADMIN":
        password == "12345"
        return "Access granted"
    else: 
        return"Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
        print = f"It's {response} out there!"

    pass

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
