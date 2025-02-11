from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

"""This module provides basic calculator test."""
class Calulator:
    def add(a, b):
        """Returns the sum of a and b."""
        calculation =Calculation(a,b,add)
        return calculation.get_result()
    
    def substract(a,b):
        """Returns the difference of a and b."""
        calculation =Calculation(a,b,subtract)
        return calculation.get_result()
    
    def multply(a,b):
        """Returns the product of a and b."""
        calculation =Calculation(a,b,multiply)
        return calculation.get_result()
    
    def divide(a,b):
        """Returns the division of a and b."""
        calculation =Calculation(a,b,divide)
        return calculation.get_result()
 
# Ensure the file ends with a newline
