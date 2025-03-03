import os
import pkgutil
import importlib
import inspect
import logging
import logging.config
from dotenv import load_dotenv
from calculator.commands import CommandHandler, Command
import calculator.plugins  # Import the plugins package

class Calculator:
    """
    Calculator class for managing the command-line interface (CLI) calculator.
    Supports dynamically loading plugins that extend functionality.

    Attributes:
        command_handler (CommandHandler): Manages and executes commands in the calculator CLI.
        settings (dict): Stores environment variables.
    """

    def __init__(self):
        """
        Initializes the Calculator with a CommandHandler instance.
        Loads environment variables and configures logging.
        """
        self.setup_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()
        self.load_plugins()

    def setup_logging(self):
        """
        Configures logging settings.
        """
        os.makedirs('logs', exist_ok=True)
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging initialized.")

    def load_environment_variables(self):
        """
        Loads environment variables into a dictionary.
        """
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        """
        Dynamically loads all plugins from the `calculator.plugins` package.
        """
        all_package = calculator.plugins
        
        for _, module_name, _ in pkgutil.iter_modules(
                all_package.__path__, all_package.__name__ + "."):
            try:
                module = importlib.import_module(module_name)
                logging.info(f"Loaded plugin module: {module_name}")
            except ImportError as e:
                logging.error(f"Error loading plugin {module_name}: {e}")
                continue

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
                    try:
                        init_signature = inspect.signature(attr.__init__)
                        command_instance = attr(self.command_handler) if "command_handler" in init_signature.parameters else attr()
                        command_name = getattr(command_instance, 'command_name', module_name.split(".")[-1])
                        self.command_handler.register_command(command_name, command_instance)
                        logging.info(f"Registered command: {command_name}")
                    except TypeError as e:
                        logging.warning(f"Skipping {attr_name} due to error: {e}")

    def start(self):
        """
        Starts the CLI loop for the calculator.
        """
        logging.info("Calculator CLI started.")
        print("Calculator CLI - Type 'quit' to exit OR Menu to Continue")
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input.lower() == "quit":
                    logging.info("Exiting calculator.")
                    print("Goodbye!")
                    break
                
                parts = user_input.split(maxsplit=1)
                command_name = parts[0] if parts else ''
                args = parts[1].split() if len(parts) > 1 else []

                if command_name:
                    self.command_handler.execute_command(command_name, *args)
                else:
                    logging.warning("Invalid command entered.")
                    print("Please enter a valid command.")
            except KeyboardInterrupt:
                logging.info("Calculator interrupted by user.")
                print("\nExiting calculator. Goodbye!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print("An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()