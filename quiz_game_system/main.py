"""
Main Module for Quiz Game System
Entry point of the application
"""

import sys
import os
from utils import (
    clear_screen, print_banner, print_section_header, print_separator,
    validate_menu_choice, print_success, print_error, print_info,
    print_colored_text
)
from quiz import QuizGame
from leaderboard import Leaderboard


class QuizGameApp:
    """
    Main application class that manages the overall game flow
    """
    
    def __init__(self):
        """
        Initialize the Quiz Game Application
        """
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        questions_file = os.path.join(script_dir, "questions.json")
        leaderboard_file = os.path.join(script_dir, "leaderboard.csv")
        
        self.quiz = QuizGame(questions_file)
        self.leaderboard = Leaderboard(leaderboard_file)
        self.player_name = None
        self.running = True
    
    
    def show_main_menu(self):
        """
        Display the main menu and get user choice
        
        Returns:
            int: User's menu choice
        """
        clear_screen()
        print_banner()
        
        print_section_header("MAIN MENU")
        print("1. 🎯  Start Quiz")
        print("2. 📊 View Leaderboard")
        print("3. 👤 Player Statistics")
        print("4. ℹ️  How to Play")
        print("5. 🚪 Exit")
        print()
        
        choice = validate_menu_choice("Enter your choice (1-5): ", 5)
        return choice
    
    
    def show_quiz_menu(self):
        """
        Display quiz options menu
        
        Returns:
            int: User's menu choice
        """
        clear_screen()
        print_section_header("QUIZ OPTIONS")
        
        categories = self.quiz.get_categories()
        
        print("1. 🎲 Play All Questions")
        print("2. 📂 Play by Category")
        print("3. 🎓 Play by Difficulty")
        print("4. 🔙 Back to Main Menu")
        print()
        
        choice = validate_menu_choice("Enter your choice (1-4): ", 4)
        return choice
    
    
    def show_categories(self):
        """
        Display available categories and get user choice
        
        Returns:
            str: Selected category or None if back
        """
        clear_screen()
        print_section_header("SELECT CATEGORY")
        
        categories = self.quiz.get_categories()
        
        if not categories:
            print_error("No categories available!")
            input("Press Enter to continue...")
            return None
        
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        print(f"{len(categories) + 1}. 🔙 Back")
        print()
        
        choice = validate_menu_choice(f"Enter your choice (1-{len(categories) + 1}): ", len(categories) + 1)
        
        if choice == len(categories) + 1:
            return None
        
        return categories[choice - 1]
    
    
    def show_difficulty_menu(self):
        """
        Display difficulty options and get user choice
        
        Returns:
            str: Selected difficulty or None if back
        """
        clear_screen()
        print_section_header("SELECT DIFFICULTY")
        
        difficulties = ["Easy", "Medium", "Hard"]
        
        for idx, difficulty in enumerate(difficulties, 1):
            print(f"{idx}. {difficulty}")
        print("4. 🔙 Back")
        print()
        
        choice = validate_menu_choice("Enter your choice (1-4): ", 4)
        
        if choice == 4:
            return None
        
        return difficulties[choice - 1]
    
    
    def get_player_name(self):
        """
        Get player name from user input
        
        Returns:
            str: Player name
        """
        clear_screen()
        print_section_header("PLAYER INFORMATION")
        
        name = input("Enter your name (minimum 2 characters): ").strip()
        
        while len(name) < 2:
            print_error("Name must be at least 2 characters long!")
            name = input("Enter your name again: ").strip()
        
        return name
    
    
    def start_quiz(self):
        """
        Start the quiz with selected options
        """
        # Load questions first
        if not self.quiz.load_questions():
            print_error("Failed to load questions. Please check the questions.json file.")
            input("Press Enter to continue...")
            return
        
        print()
        
        # Show quiz menu
        quiz_choice = self.show_quiz_menu()
        
        if quiz_choice == 1:
            # All questions
            selected_questions = self.quiz.questions
        
        elif quiz_choice == 2:
            # By category
            category = self.show_categories()
            if category is None:
                return
            
            selected_questions = self.quiz.get_questions_by_category(category)
            
            if not selected_questions:
                print_error(f"No questions found in category: {category}")
                input("Press Enter to continue...")
                return
            
            clear_screen()
            print_success(f"Found {len(selected_questions)} questions in category: {category}")
            print()
        
        elif quiz_choice == 3:
            # By difficulty
            difficulty = self.show_difficulty_menu()
            if difficulty is None:
                return
            
            selected_questions = self.quiz.get_questions_by_difficulty(difficulty)
            
            if not selected_questions:
                print_error(f"No questions found with difficulty: {difficulty}")
                input("Press Enter to continue...")
                return
            
            clear_screen()
            print_success(f"Found {len(selected_questions)} questions with difficulty: {difficulty}")
            print()
        
        else:
            return
        
        # Get player name
        player_name = self.get_player_name()
        
        # Start the quiz
        results = self.quiz.start_quiz(selected_questions, shuffle=True)
        
        if results:
            # Display results
            self.quiz.display_results(player_name, results)
            
            # Save score to leaderboard
            self.leaderboard.save_score(
                player_name,
                results['score'],
                results['total'],
                results['percentage']
            )
            
            # Ask if want to play again
            replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if replay == 'yes':
                self.start_quiz()
    
    
    def show_how_to_play(self):
        """
        Display instructions on how to play
        """
        clear_screen()
        print_section_header("HOW TO PLAY")
        
        instructions = """
📌 QUIZ GAME SYSTEM - HOW TO PLAY:

1️⃣  STARTING THE GAME:
   • Select "Start Quiz" from the main menu
   • Choose your quiz option:
     - All Questions: Play all available questions
     - By Category: Select a specific category
     - By Difficulty: Choose Easy, Medium, or Hard

2️⃣  PLAYING THE QUIZ:
   • Read the question carefully
   • You'll see 4 options labeled 1, 2, 3, 4
   • Enter the number of your answer
   • You'll get immediate feedback
   • Your current score is shown after each question

3️⃣  SCORING:
   • Each correct answer = 1 point
   • Your final score shows: Score/Total Questions
   • Accuracy percentage is also calculated
   
4️⃣  AFTER THE QUIZ:
   • See your performance rating
   • Your score is automatically saved to leaderboard
   • Option to play again or return to main menu

5️⃣  LEADERBOARD:
   • View top 10 players by score
   • Check player statistics
   • See how you rank against others!

💡 TIPS FOR SUCCESS:
   • Read questions and options carefully
   • Take your time - there's no time limit
   • Learn from wrong answers
   • Practice regularly to improve!

🌟 HAVE FUN AND LEARN! 🌟

        """
        print(instructions)
        print_separator()
        input("Press Enter to go back to menu...")
    
    
    def run(self):
        """
        Main application loop
        """
        while self.running:
            choice = self.show_main_menu()
            
            if choice == 1:
                # Start Quiz
                self.start_quiz()
            
            elif choice == 2:
                # View Leaderboard
                self.leaderboard.display_leaderboard()
            
            elif choice == 3:
                # Player Statistics
                clear_screen()
                print_section_header("PLAYER STATISTICS")
                
                player_name = input("Enter player name: ").strip()
                
                if player_name:
                    self.leaderboard.display_player_stats(player_name)
                else:
                    print_error("Please enter a valid name.")
                    input("Press Enter to continue...")
            
            elif choice == 4:
                # How to Play
                self.show_how_to_play()
            
            elif choice == 5:
                # Exit
                self.exit_game()
    
    
    def exit_game(self):
        """
        Exit the game with a goodbye message
        """
        clear_screen()
        print_section_header("THANK YOU FOR PLAYING!")
        
        goodbye_message = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              Thanks for playing Quiz Game System!         ║
║                                                            ║
║         Keep learning and improving your knowledge!       ║
║                                                            ║
║                    Goodbye! 👋                             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
        print(goodbye_message)
        
        self.running = False
        sys.exit(0)


def main():
    """
    Entry point of the application
    """
    try:
        app = QuizGameApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please contact support or check the error log.")
        sys.exit(1)


if __name__ == "__main__":
    main()
