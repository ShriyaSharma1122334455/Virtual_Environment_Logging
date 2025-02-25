import unittest
import sys
import io
from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Initialize CommandHandler and register commands."""
        self.handler = CommandHandler()
        self.handler.register_command("add", AddCommand())
        self.handler.register_command("subtract", SubtractCommand())
        self.handler.register_command("multiply", MultiplyCommand())
        self.handler.register_command("divide", DivideCommand())
        self.handler.register_command("menu", MenuCommand(self.handler))

    def capture_output(self, func, *args):
        """Helper function to capture printed output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__  # Reset stdout
        return captured_output.getvalue().strip()

    def test_execute_valid_command(self):
        """Test executing a valid command (addition)."""
        output = self.capture_output(self.handler.execute_command, "add", "10", "5")  # Pass arguments separately
        self.assertEqual(output, "The Solution of addition is 15")

    def test_execute_invalid_command(self):
        """Test executing an unregistered command."""
        output = self.capture_output(self.handler.execute_command, "invalid")
        self.assertEqual(output, "No such command: invalid")

if __name__ == "__main__":
    unittest.main()
