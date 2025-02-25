import sys
from calculator.commands import Command

class QuitCommand(Command):
    """
    QuitCommand class to exit the program.

    This command class inherits from the Command class and implements the
    execute method to terminate the program with a farewell message.
    """

    def execute(self):
        """
        Executes the quit command.

        This method terminates the program and displays a farewell message.
        """
        sys.exit("Bye Bye")

# Expose the QuitCommand class for external use
__all__ = ["QuitCommand"]
