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
    def setUp(self):
        """Set up a command handler before each test."""
        self.handler = CommandHandler()

    def capture_output(self, func, *args):
        """Helper function to capture printed output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__  # Reset stdout
        return captured_output.getvalue().strip()

    def test_add_command(self):
        command = AddCommand()
        output = self.capture_output(command.execute, 10, 5)  # Pass numbers
        self.assertEqual(output, "The Solution of addition is 15")

    def test_subtract_command(self):
        command = SubtractCommand()
        output = self.capture_output(command.execute, 10, 4)
        self.assertEqual(output, "The solution of subtraction is 6")

    def test_multiply_command(self):
        command = MultiplyCommand()
        output = self.capture_output(command.execute, 3, 7)
        self.assertEqual(output, "The solution of multiplication is 21")

    def test_divide_command(self):
        command = DivideCommand()
        output = self.capture_output(command.execute, 20, 4)
        self.assertEqual(output, "The solution of division is 5")

    def test_menu_command(self):
        handler = MenuCommand(self.handler)  # Ensure handler is set up
        output = self.capture_output(handler.execute)
        self.assertIn("Available Commands:", output)

if __name__ == "__main__":
    unittest.main()

    """New Line"""
