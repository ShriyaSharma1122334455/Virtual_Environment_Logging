"""
Module for the DivideCommand class.

This module provides the DivideCommand class, which performs the division 
of two numerical arguments while handling errors such as invalid input and 
division by zero.
"""

from decimal import Decimal, InvalidOperation, DivisionByZero
from calculator.commands import Command

class DivideCommand(Command):
    """
    DivideCommand class to perform the division of two numerical arguments.

    This command class inherits from the Command class and implements the
    execute method to perform division of two numbers passed as arguments.
    """

    def execute(self, *args):
        """
        Executes the division command with the given arguments.

        Args:
            *args: Two numerical arguments to be divided.

        Raises:
            InvalidOperation: If the arguments cannot be converted to Decimal.
            DivisionByZero: If division by zero is attempted.
        """
        try:
            # Convert arguments to Decimal and perform division
            a, b = map(Decimal, args)
            if b == 0:
                print("Error: Division by zero is not allowed.")
                return
            quotient = a / b
            print(f"The solution of division is {quotient}")
        except InvalidOperation:
            print("Error: Invalid input. Please enter valid numbers.")
        except DivisionByZero:
            print("Error: Cannot divide by zero.")

# Expose the DivideCommand class for external use
__all__ = ["DivideCommand"]
