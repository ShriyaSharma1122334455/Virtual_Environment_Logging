"""
Test plan for calculator commands with logging and environment variables.
"""

import os
import pytest
import logging
from calculator.commands import CommandHandler
from calculator.commands import Command
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variable for test mode
os.environ["TEST_MODE"] = "true"

# Mocking command classes
class ArithmeticCommand(Command):
    """Base class for arithmetic commands."""
    
    def __init__(self, name):
        self.command_name = name

    def execute(self, *args):
        if len(args) != 2:
            raise ValueError(f"{self.command_name} requires exactly two arguments.")
        try:
            num1, num2 = float(args[0]), float(args[1])
            if self.command_name == "divide" and num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.operate(num1, num2)
        except ValueError:
            raise ValueError("Invalid arguments. Both arguments must be numbers.")

    def operate(self, num1, num2):
        raise NotImplementedError("Operate method must be implemented in subclasses.")

class AddCommand(ArithmeticCommand):
    """Addition command."""
    def __init__(self):
        super().__init__("add")

    def operate(self, num1, num2):
        return num1 + num2

class SubtractCommand(ArithmeticCommand):
    """Subtraction command."""
    def __init__(self):
        super().__init__("subtract")

    def operate(self, num1, num2):
        return num1 - num2

class MultiplyCommand(ArithmeticCommand):
    """Multiplication command."""
    def __init__(self):
        super().__init__("multiply")

    def operate(self, num1, num2):
        return num1 * num2

class DivideCommand(ArithmeticCommand):
    """Division command."""
    def __init__(self):
        super().__init__("divide")

    def operate(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2

@pytest.mark.parametrize("command_class, a, b, expected_result", [
    (AddCommand, "2.5", "3.5", 6.0),
    (SubtractCommand, "5", "3", 2.0),
    (MultiplyCommand, "4", "5", 20.0),
    (DivideCommand, "10", "2", 5.0),
])
def test_arithmetic_commands(command_class, a, b, expected_result):
    """Test arithmetic commands."""
    command = command_class()
    result = command.execute(a, b)
    assert result == expected_result
    logger.info(f"{command.command_name} command executed successfully.")

@pytest.mark.parametrize("command_class, a, b, expected_exception", [
    (AddCommand, "two", "three", ValueError),
    (SubtractCommand, "five", "three", ValueError),
    (MultiplyCommand, "four", "five", ValueError),
    (DivideCommand, "ten", "two", ValueError),
    (DivideCommand, "10", "0", ZeroDivisionError),
])
def test_arithmetic_commands_invalid_input(command_class, a, b, expected_exception):
    """Test invalid input for arithmetic commands."""
    command = command_class()
    with pytest.raises(expected_exception):
        command.execute(a, b)
    logger.info(f"{command.command_name} correctly handled invalid input.")
