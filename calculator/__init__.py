"""
Module for the Calculator CLI and its command registration and execution.

This module contains the Calculator class that registers and manages commands
for operations like add, subtract, multiply, divide, etc. It also manages
the user interaction through a command-line interface.
"""

from calculator.commands import CommandHandler
from calculator.commands.welcome import WelcomeCommand
from calculator.commands.quit import QuitCommand
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand


class Calculator:
    """
    Calculator class for managing the command-line interface (CLI) calculator.
    
    This class handles the registration and execution of commands for the calculator.
    It supports operations like addition, subtraction, multiplication, and division, 
    along with utility commands such as "quit" and "menu."
    """

    def __init__(self):
        """
        Initializes the Calculator with a CommandHandler to manage registered commands.
        """
        self.command_handler = CommandHandler()
        self.register_commands()

    def register_commands(self):
        """
        Registers all available commands with the CommandHandler.
        
        This method binds command names to their corresponding command classes,
        so they can be executed by the user.
        """
        self.command_handler.register_command("welcome", WelcomeCommand())
        self.command_handler.register_command("quit", QuitCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtract", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

    def start(self):
        """
        Starts the Read-Eval-Print Loop (REPL) for user interaction.

        This method continuously prompts the user for input, processes the input, 
        and executes the corresponding command. It exits when the 'quit' command is issued.
        """
        print("Calculator CLI - Type 'quit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == "quit":
                print("Exiting calculator. Goodbye!")
                break  # Exit loop when 'quit' is entered
            parts = user_input.split(maxsplit=1)
            command_name = parts[0] if parts else ''
            args = parts[1].split() if len(parts) > 1 else []

            if command_name:
                self.command_handler.execute_command(command_name, *args)
            else:
                print("Please enter a valid command.")