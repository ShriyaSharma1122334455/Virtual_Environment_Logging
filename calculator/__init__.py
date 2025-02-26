import pkgutil
import importlib
import inspect
from calculator.commands import CommandHandler, Command
import calculator.plugins  # Import the plugins package

class Calculator:
    """
    Calculator class for managing the command-line interface (CLI) calculator.
    Now supports dynamically loading plugins.
    """

    def __init__(self):
        """Initializes the Calculator with a CommandHandler."""
        self.command_handler = CommandHandler()
        self.load_plugins()

    def load_plugins(self):
        """Dynamically loads all plugins from the `calculator.plugins` package."""
        all_package = calculator.plugins  # Assign the actual module

        for _, module_name, _ in pkgutil.iter_modules(all_package.__path__, all_package.__name__ + "."):
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

                        command_name = getattr(command_instance, 'command_name', module_name.split(".")[-1])
                        self.command_handler.register_command(command_name, command_instance)
                    except TypeError as e:
                        print(f"Skipping {attr_name}: {e}")  # Log errors instead of crashing

    def start(self):
        """Starts the command-line interface loop."""
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
