"""Test plan for calculator commands"""
from calculator.commands import Command
from calculator.commands import CommandHandler

# Mocking command classes that would be in the plugins directory
class AddCommand(Command):
    """Command that performs addition of two numbers."""
    
    def __init__(self, command_handler=None):
        self.command_name = "add"
        if command_handler:
            self.command_handler = command_handler

    def execute(self, *args):
        """Execute the addition command."""
        if len(args) != 2:
            print(f"Error: {self.command_name} requires exactly two arguments.")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is {result}")
        except ValueError:
            print("Error: Invalid arguments. Both arguments must be numbers.")

class SubtractCommand(Command):
    """Command that performs subtraction of two numbers."""
    
    def __init__(self, command_handler=None):
        self.command_name = "subtract"
        if command_handler:
            self.command_handler = command_handler

    def execute(self, *args):
        """Execute the subtraction command."""
        if len(args) != 2:
            print(f"Error: {self.command_name} requires exactly two arguments.")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 - num2
            print(f"The result of subtracting {num1} and {num2} is {result}")
        except ValueError:
            print("Error: Invalid arguments. Both arguments must be numbers.")

class MultiplyCommand(Command):
    """Command that performs multiplication of two numbers."""
    
    def __init__(self, command_handler=None):
        self.command_name = "multiply"
        if command_handler:
            self.command_handler = command_handler

    def execute(self, *args):
        """Execute the multiplication command."""
        if len(args) != 2:
            print(f"Error: {self.command_name} requires exactly two arguments.")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 * num2
            print(f"The result of multiplying {num1} and {num2} is {result}")
        except ValueError:
            print("Error: Invalid arguments. Both arguments must be numbers.")

class DivideCommand(Command):
    """Command that performs division of two numbers."""
    
    def __init__(self, command_handler=None):
        self.command_name = "divide"
        if command_handler:
            self.command_handler = command_handler

    def execute(self, *args):
        """Execute the division command."""
        if len(args) != 2:
            print(f"Error: {self.command_name} requires exactly two arguments.")
            return
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
            print(f"The result of dividing {num1} and {num2} is {result}")
        except ValueError:
            print("Error: Invalid arguments. Both arguments must be numbers.")

class MenuCommand(Command):
    """Command that displays a menu of available commands."""
    
    def __init__(self, command_handler=None):
        self.command_name = "menu"
        self.command_handler = command_handler

    def execute(self):
        """Display available commands."""
        print("Available commands:")
        for cmd_name in self.command_handler.commands:
            print(f"- {cmd_name}")

# Tests for command handler
def test_command_handler_register_execute():
    """Test registering and executing a command through the handler."""
    handler = CommandHandler()
    add_cmd = AddCommand()
    
    # Register the command
    handler.register_command("add", add_cmd)
    
    # Verify command was registered
    assert "add" in handler.commands
    assert handler.commands["add"] == add_cmd
    
    # Test executing the command
    handler.execute_command("add", "5", "3")

# Tests for individual commands
def test_add_command_success(capfd):
    """Test addition with valid arguments."""
    command = AddCommand()
    command.execute("2.5", "3.5")
    
    out, _ = capfd.readouterr()
    assert "The result of adding 2.5 and 3.5 is 6.0" in out

def test_add_command_invalid_arguments(capfd):
    """Test addition with non-numeric arguments."""
    command = AddCommand()
    command.execute("two", "three")
    
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_add_command_incorrect_argument_count(capfd):
    """Test addition with incorrect number of arguments."""
    command = AddCommand()
    
    # Too few arguments
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Error: add requires exactly two arguments." in out
    
    # Too many arguments
    command.execute("1", "2", "3")
    out, _ = capfd.readouterr()
    assert "Error: add requires exactly two arguments." in out

def test_subtract_command_success(capfd):
    """Test subtraction with valid arguments."""
    command = SubtractCommand()
    command.execute("5", "3")
    
    out, _ = capfd.readouterr()
    assert "The result of subtracting 5.0 and 3.0 is 2.0" in out

def test_subtract_command_invalid_arguments(capfd):
    """Test subtraction with non-numeric arguments."""
    command = SubtractCommand()
    command.execute("five", "three")
    
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_subtract_command_incorrect_argument_count(capfd):
    """Test subtraction with incorrect number of arguments."""
    command = SubtractCommand()
    
    # Too few arguments
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Error: subtract requires exactly two arguments." in out
    
    # Too many arguments
    command.execute("5", "3", "1")
    out, _ = capfd.readouterr()
    assert "Error: subtract requires exactly two arguments." in out

def test_multiply_command_success(capfd):
    """Test multiplication with valid arguments."""
    command = MultiplyCommand()
    command.execute("4", "5")
    
    out, _ = capfd.readouterr()
    assert "The result of multiplying 4.0 and 5.0 is 20.0" in out

def test_multiply_command_invalid_arguments(capfd):
    """Test multiplication with non-numeric arguments."""
    command = MultiplyCommand()
    command.execute("four", "five")
    
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_multiply_command_incorrect_argument_count(capfd):
    """Test multiplication with incorrect number of arguments."""
    command = MultiplyCommand()
    
    # Too few arguments
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Error: multiply requires exactly two arguments." in out
    
    # Too many arguments
    command.execute("5", "3", "2")
    out, _ = capfd.readouterr()
    assert "Error: multiply requires exactly two arguments." in out

def test_divide_command_success(capfd):
    """Test division with valid arguments."""
    command = DivideCommand()
    command.execute("10", "2")
    
    out, _ = capfd.readouterr()
    assert "The result of dividing 10.0 and 2.0 is 5.0" in out

def test_divide_command_by_zero(capfd):
    """Test division by zero."""
    command = DivideCommand()
    command.execute("10", "0")
    
    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero" in out

def test_divide_command_invalid_arguments(capfd):
    """Test division with non-numeric arguments."""
    command = DivideCommand()
    command.execute("ten", "two")
    
    out, _ = capfd.readouterr()
    assert "Error: Invalid arguments. Both arguments must be numbers." in out

def test_divide_command_incorrect_argument_count(capfd):
    """Test division with incorrect number of arguments."""
    command = DivideCommand()
    
    # Too few arguments
    command.execute("10")
    out, _ = capfd.readouterr()
    assert "Error: divide requires exactly two arguments." in out
    
    # Too many arguments
    command.execute("10", "2", "1")
    out, _ = capfd.readouterr()
    assert "Error: divide requires exactly two arguments." in out

def test_menu_command(capfd):
    """Test the menu command."""
    handler = CommandHandler()
    handler.register_command("add", AddCommand())
    handler.register_command("subtract", SubtractCommand())
    
    menu_cmd = MenuCommand(handler)
    menu_cmd.execute()
    
    out, _ = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
