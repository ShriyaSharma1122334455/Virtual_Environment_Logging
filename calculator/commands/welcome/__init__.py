"""
Module for the WelcomeCommand class.

This module provides the WelcomeCommand class, which displays a welcome 
message when executed.
"""

from calculator.commands import Command

class WelcomeCommand(Command):
    """
    WelcomeCommand class for printing a welcome message.

    This class inherits from the Command class and implements the execute method
    to display a welcome message when executed.
    """

    def execute(self):
        """
        Executes the welcome command.

        This method prints a welcome message to the user.
        """
        print("Hello, Welcome to Calculator")

# Expose the WelcomeCommand class for external use
__all__ = ["WelcomeCommand"]
