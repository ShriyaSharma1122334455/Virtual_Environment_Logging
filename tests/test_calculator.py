"""
Test suite for the Calculator class.

This module contains tests for the Calculator class, specifically 
testing how it handles commands like 'quit' and unknown commands. 
It uses pytest to test the CLI functionality of the Calculator.
"""

from calculator import Calculator

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the calculator exits correctly on 'quit' command."""
    # Simulate user entering 'quit'
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    calculator = Calculator()
    calculator.start()
    # Check output
    captured = capfd.readouterr()
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    assert "Exiting calculator. Goodbye!" in captured.out

def test_calculator_start_unknown_command(capfd, monkeypatch):
    """Test how the calculator handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'quit'
    inputs = iter(['unknown_command', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    calculator = Calculator()
    calculator.start()
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "Calculator CLI - Type 'quit' to exit OR Menu to Continue" in captured.out
    assert "Exiting calculator. Goodbye!" in captured.out
