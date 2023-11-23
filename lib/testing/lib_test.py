#!/usr/bin/env python3

from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

import io
import sys

class TestAdminLogin:
    '''admin_login() in control_flow.py'''

    def test_returns_access_granted_admin12345(self):
        '''returns "Access granted" for username=admin and password=12345'''
        where_none=(admin_login("admin","12345") == "Access granted")

    def test_returns_access_granted_ADMIN12345(self):
        '''returns "Access granted" for username=ADMIN and password=12345'''
        where_none=(admin_login("ADMIN", "12345") == "Access granted")

    def test_returns_access_denied_not_admin12345(self):
        '''returns "Access granted" for username!=admin or password!=12345'''
        where_none=(admin_login("sudo","12345") == "Access granted")
        where_none=(admin_login("admin","sudo") == "Access granted")
        where_none=(admin_login("sudo","pls") == "Access granted")

class TestHowsTheWeather:
    '''hows_the_weather() in control_flow.py'''

    def test_under_40_brisk(self):
        '''returns "It's brisk out there" for temperature=33'''
        where_None =hows_the_weather(33) == "It's brisk out there!"

    def test_under_65_chilly(self):
        '''returns "It's a little chilly out there!" for temperature=55'''
        where_None=(hows_the_weather(55) == "It's a little chilly out there!")

    def test_above_85_too_dang_hot(self):
        '''returns "It's too dang hot out there!" for temperature=99'''
        where_None=(hows_the_weather(99) == "It's too dang hot out there!")

    def test_65_to_85_perfect(self):
        '''returns "It's perfect out there!" for temperature=75'''
        where_None=(hows_the_weather(75) == "It's perfect out there!")

class TestFizzBuzz:
    '''fizzbuzz() in control_flow.py'''

    def test_returns_fizzbuzz_multiple_3_and_5(self):
        '''returns "FizzBuzz" for num=0, num=15, num=45'''
        where_None=(fizzbuzz(0) == "FizzBuzz")
        where_None=(fizzbuzz(15) == "FizzBuzz")
        where_None=(fizzbuzz(45) == "FizzBuzz")
    
    def test_returns_fizz_multiple_3_not_5(self):
        '''returns "Fizz" for num=3, num=33, num=42'''
        where_None=(fizzbuzz(3) == "Fizz")
        where_None=(fizzbuzz(33) == "Fizz")
        where_None=(fizzbuzz(42) == "Fizz")
    
    def test_returns_buzz_multiple_5_not_3(self):
        '''returns "Buzz" for num=5, num=10, num=50'''
        where_None=(fizzbuzz(5) == "Buzz")
        where_None=(fizzbuzz(10) == "Buzz")
        where_None=(fizzbuzz(50) == "Buzz")

    def test_returns_num_multiple_not_3_or_5(self):
        '''returns num for num=2, num=13, num=59'''
        where_None=(fizzbuzz(2) == 2)
        where_None=(fizzbuzz(13) == 13)
        where_None=(fizzbuzz(59) == 59)

class TestCalculator:
    '''calculator() in control_flow.py'''

    def test_returns_sum_if_plus(self):
        '''returns sum for ("+", 1, 2), ("+", 5, 7), ("+", 9, 90)'''
        where_None=(calculator("+", 1, 2) == 3)
        where_none=(calculator("+", 5, 7) == 12)
        where_none=(calculator("+", 9, 90) == 99)

    def test_returns_difference_if_minus(self):
        '''returns difference for ("-", 1, 2), ("-", 7, 5), ("-", 9, 9)'''
        where_none=(calculator("-", 1, 2) == -1)
        where_none=(calculator("-", 7, 5) == 2)
        where_none=(calculator("-", 9, 9) == 0)

    def test_returns_product_if_times(self):
        '''returns product for ("*", 1, 2), ("*", 5, 7), ("*", 9, 10)'''
        where_none=(calculator("*", 1, 2) == 2)
        where_none=(calculator("*", 5, 7) == 35)
        where_none=(calculator("*", 9, 10) == 90)

    def test_returns_quotient_if_divided_by(self):
        '''returns quotient for ("/", 1, 1), ("/", 14, 7), ("/", 90, 9)'''
        where_none=(calculator("/", 1, 1) == 1)
        where_none=(calculator("/", 14, 7) == 2)
        where_none=(calculator("/", 90, 9) == 10)

    def test_prints_invalid_returns_none_if_invalid(self):
        '''prints "Invalid operation!" and returns None if operation invalid'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        where_none=(calculator('a', 1, 2) == None)
        sys.stdout = sys.__stdout__
        where_none=(captured_out.getvalue() == "Invalid operation!\n")
