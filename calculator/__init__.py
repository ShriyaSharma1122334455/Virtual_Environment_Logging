"""
Calculator CLI Application

This module defines a Calculator class that manages a command-line interface (CLI) for 
a calculator application. The class dynamically loads plugins from the `calculator.plugins` 
package, allowing for extension of functionality through user-defined commands.

The Calculator supports registering commands, executing them through user input, and 
providing a loop for interaction. Commands can be extended by creating plugins that 
inherit from the `Command` class.

Modules and classes:
    - Calculator: Manages the calculator CLI, command handling, and plugin loading.
    - CommandHandler: Handles the execution and registration of commands.
    - Command: The base class for commands that can be executed by the Calculator.
    - Plugins: Dynamically loaded modules in the `calculator.plugins` package, 
      which can extend the calculator functionality.
"""

import pkgutil
import importlib
import inspect
from calculator.commands import CommandHandler, Command
import calculator.plugins  # Import the plugins package

class Calculator:
    """
    Calculator class for managing the command-line interface (CLI) calculator.
    Supports dynamically loading plugins that extend functionality.

    Attributes:
        command_handler (CommandHandler): Manages and executes commands in the calculator CLI.
    """

    def __init__(self):
        """
        Initializes the Calculator with a CommandHandler instance.
        Additionally, loads any available plugins that extend the Command class.
        """
        self.command_handler = CommandHandler()
        self.load_plugins()

    def load_plugins(self):
        """
        Dynamically loads all plugins from the `calculator.plugins` package.

        This method scans the `calculator.plugins` package for modules and attempts 
        to find any class that inherits from the `Command` class. If such a class is 
        found, it is instantiated and registered with the command handler.
        """
        all_package = calculator.plugins  # Assign the actual module

        # Loop through all modules in the calculator.plugins package
        for _, module_name, _ in pkgutil.iter_modules(
                all_package.__path__, all_package.__name__ + "."):
            module = importlib.import_module(module_name)

            # Find any class that inherits from Command
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
                    try:
                        # Use inspect to check if __init__ requires command_handler
                        init_signature = inspect.signature(attr.__init__)
                        if "command_handler" in init_signature.parameters:
                            command_instance = attr(self.command_handler)  # Pass the handler
                        else:
                            command_instance = attr()  # Instantiate normally

                        command_name = getattr(command_instance, 'command_name',
                                                module_name.split(".")[-1])
                        self.command_handler.register_command(command_name, command_instance)
                    except TypeError as e:
                        print(f"Skipping {attr_name}: {e}")  # Log errors instead of crashing

    def start(self):
        """
        Starts the command-line interface (CLI) loop for the calculator.

        This method enters a loop, waiting for user input, and executes the corresponding
        command if found. The loop continues until the user types 'quit' to exit.
        """
        print("Calculator CLI - Type 'quit' to exit OR Menu to Continue")
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
