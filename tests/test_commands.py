"""
Module for testing the Calculator commands.
This module contains unit tests for various commands like addition, subtraction, 
multiplication, division, and menu within the Calculator CLI. It ensures that 
each command works as expected.
"""

import unittest
import sys
import io
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand
from calculator.commands import CommandHandler  # Ensure CommandHandler is imported

class TestCommands(unittest.TestCase):
    """
    TestCommands class to test the functionality of Calculator commands.

    This class contains unit tests for the commands available in the Calculator 
    CLI. It tests the execution of valid commands and checks the correctness of 
    their outputs.
    """

    def setUp(self):
        """
        Set up a command handler before each test.

        This method initializes the CommandHandler, which is responsible for 
        executing the registered commands.
        """
        self.handler = CommandHandler()

    def capture_output(self, func, *args):
        """
        Helper function to capture printed output.

        This method captures the standard output generated during the execution 
        of a command and returns it as a string.

        Args:
            func: The function to execute.
            *args: The arguments to pass to the function.

        Returns:
            The captured output as a string.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__  # Reset stdout
        return captured_output.getvalue().strip()

    def test_add_command(self):
        """
        Test the add command.

        This method tests the functionality of the AddCommand by passing two 
        numerical arguments and comparing the output to the expected result.
        """
        command = AddCommand()
        output = self.capture_output(command.execute, 10, 5)  # Pass numbers
        self.assertEqual(output, "The Solution of addition is 15")

    def test_subtract_command(self):
        """
        Test the subtract command.

        This method tests the functionality of the SubtractCommand by passing 
        two numerical arguments and comparing the output to the expected result.
        """
        command = SubtractCommand()
        output = self.capture_output(command.execute, 10, 4)
        self.assertEqual(output, "The solution of subtraction is 6")

    def test_multiply_command(self):
        """
        Test the multiply command.

        This method tests the functionality of the MultiplyCommand by passing 
        two numerical arguments and comparing the output to the expected result.
        """
        command = MultiplyCommand()
        output = self.capture_output(command.execute, 3, 7)
        self.assertEqual(output, "The solution of multiplication is 21")

    def test_divide_command(self):
        """
        Test the divide command.

        This method tests the functionality of the DivideCommand by passing 
        two numerical arguments and comparing the output to the expected result.
        """
        command = DivideCommand()
        output = self.capture_output(command.execute, 20, 4)
        self.assertEqual(output, "The solution of division is 5")

    def test_menu_command(self):
        """
        Test the menu command.

        This method tests the functionality of the MenuCommand by checking if 
        the available commands are listed correctly.
        """
        handler = MenuCommand(self.handler)  # Ensure handler is set up
        output = self.capture_output(handler.execute)
        self.assertIn("Available Commands:", output)

if __name__ == "__main__":
    unittest.main()

    # """New Line"""
