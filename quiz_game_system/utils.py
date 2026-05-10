"""
Utility Functions for Quiz Game System
This module contains helper functions used across the project
"""

import os
import sys
from datetime import datetime


def clear_screen():
    """
    Clear the console screen based on the operating system
    """
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')


def print_banner():
    """
    Display the quiz game banner at the start of the application
    """
    banner = """
    
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              🎯 QUIZ GAME SYSTEM 🎯                       ║
║                                                            ║
║         Test Your Knowledge & Win Big!                    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    
    """
    print(banner)


def print_section_header(title):
    """
    Print a formatted section header
    
    Args:
        title (str): The title of the section
    """
    print("\n" + "=" * 60)
    print(f"{title.center(60)}")
    print("=" * 60 + "\n")


def print_separator():
    """
    Print a horizontal separator line
    """
    print("-" * 60)


def validate_input(prompt, valid_options=None, input_type="string"):
    """
    Validate user input with error handling
    
    Args:
        prompt (str): The message to display to the user
        valid_options (list, optional): List of valid options for validation
        input_type (str): Type of input validation - "string", "integer", "choice"
    
    Returns:
        str/int: The validated user input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Check if input is empty
            if not user_input:
                print("❌ Input cannot be empty. Please try again.\n")
                continue
            
            # Integer validation
            if input_type == "integer":
                try:
                    num = int(user_input)
                    return num
                except ValueError:
                    print("❌ Please enter a valid number.\n")
                    continue
            
            # Choice validation
            if input_type == "choice" and valid_options:
                if user_input.upper() not in valid_options:
                    print(f"❌ Please enter one of: {', '.join(valid_options)}\n")
                    continue
                return user_input.upper()
            
            # String validation
            if input_type == "string":
                if len(user_input) < 2:
                    print("❌ Input must be at least 2 characters long.\n")
                    continue
                return user_input
            
            return user_input
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {e}. Please try again.\n")


def validate_menu_choice(prompt, num_options):
    """
    Validate menu choice input
    
    Args:
        prompt (str): The message to display
        num_options (int): Number of valid menu options
    
    Returns:
        int: The validated menu choice
    """
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= num_options:
                return choice
            else:
                print(f"❌ Please enter a number between 1 and {num_options}.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            sys.exit(0)


def get_current_timestamp():
    """
    Get current timestamp in a readable format
    
    Returns:
        str: Current date and time in format: YYYY-MM-DD HH:MM:SS
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_colored_text(text, color="white"):
    """
    Print colored text to console
    
    Args:
        text (str): The text to print
        color (str): Color name - "green", "red", "yellow", "blue", "cyan"
    """
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    
    color_code = colors.get(color, colors["white"])
    reset_code = colors["reset"]
    print(f"{color_code}{text}{reset_code}")


def print_success(message):
    """Print success message in green"""
    print_colored_text(f"✓ {message}", "green")


def print_error(message):
    """Print error message in red"""
    print_colored_text(f"✗ {message}", "red")


def print_warning(message):
    """Print warning message in yellow"""
    print_colored_text(f"⚠ {message}", "yellow")


def print_info(message):
    """Print info message in cyan"""
    print_colored_text(f"ℹ {message}", "cyan")
