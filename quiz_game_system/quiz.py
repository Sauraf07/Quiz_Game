"""
Quiz Module for Quiz Game System
This module handles all quiz-related functionality
"""

import json
import random
from utils import (
    validate_input, print_section_header, print_separator,
    print_success, print_error, print_info, print_colored_text
)


class QuizGame:
    """
    Main Quiz Game class that handles quiz logic
    """
    
    def __init__(self, questions_file="questions.json"):
        """
        Initialize the quiz game
        
        Args:
            questions_file (str): Path to the JSON file containing questions
        """
        self.questions_file = questions_file
        self.questions = []
        self.score = 0
        self.total_questions = 0
        self.answers = []  # Store user answers for review
        
    
    def load_questions(self):
        """
        Load questions from JSON file
        
        Returns:
            bool: True if questions loaded successfully, False otherwise
        """
        try:
            with open(self.questions_file, 'r', encoding='utf-8') as file:
                self.questions = json.load(file)
            
            if not self.questions:
                print_error("No questions found in the JSON file!")
                return False
            
            print_success(f"Loaded {len(self.questions)} questions successfully!")
            return True
        
        except FileNotFoundError:
            print_error(f"Questions file '{self.questions_file}' not found!")
            return False
        except json.JSONDecodeError:
            print_error("Error reading JSON file. Please check the format!")
            return False
        except Exception as e:
            print_error(f"Unexpected error: {e}")
            return False
    
    
    def get_questions_by_category(self, category):
        """
        Filter questions by category
        
        Args:
            category (str): The category to filter by
        
        Returns:
            list: List of questions in the specified category
        """
        return [q for q in self.questions if q.get("category", "").lower() == category.lower()]
    
    
    def get_questions_by_difficulty(self, difficulty):
        """
        Filter questions by difficulty level
        
        Args:
            difficulty (str): The difficulty level (easy, medium, hard)
        
        Returns:
            list: List of questions at the specified difficulty
        """
        return [q for q in self.questions if q.get("difficulty", "").lower() == difficulty.lower()]
    
    
    def get_categories(self):
        """
        Get all available categories from the questions
        
        Returns:
            list: List of unique categories
        """
        categories = set()
        for question in self.questions:
            cat = question.get("category", "General")
            categories.add(cat)
        return sorted(list(categories))
    
    
    def shuffle_questions(self, questions_list):
        """
        Shuffle the questions list randomly
        
        Args:
            questions_list (list): List of questions to shuffle
        
        Returns:
            list: Shuffled list of questions
        """
        shuffled = questions_list.copy()
        random.shuffle(shuffled)
        return shuffled
    
    
    def shuffle_options(self, question):
        """
        Shuffle the options in a question while keeping track of the correct answer
        
        Args:
            question (dict): The question dictionary
        
        Returns:
            dict: Question with shuffled options
        """
        question_copy = question.copy()
        options = question_copy.get("options", [])
        correct_answer = question_copy.get("answer", "")
        
        # Create list of tuples (option, is_correct)
        options_with_flag = [(opt, opt == correct_answer) for opt in options]
        
        # Shuffle the options
        random.shuffle(options_with_flag)
        
        # Extract shuffled options and find new correct answer
        shuffled_options = [opt for opt, _ in options_with_flag]
        new_correct = next(opt for opt, is_correct in options_with_flag if is_correct)
        
        question_copy["options"] = shuffled_options
        question_copy["answer"] = new_correct
        
        return question_copy
    
    
    def ask_question(self, question_num, question):
        """
        Display a question and get user answer
        
        Args:
            question_num (int): The question number
            question (dict): The question dictionary
        
        Returns:
            str: The user's answer
        """
        print_section_header(f"Question {question_num}/{self.total_questions}")
        
        # Display question with metadata
        print(f"Category: {question.get('category', 'General')} | "
              f"Difficulty: {question.get('difficulty', 'medium').upper()}")
        print_separator()
        
        # Display the question text
        print(f"\n{question.get('question', '')}\n")
        
        # Display options
        options = question.get("options", [])
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        
        print()
        
        # Get user answer
        while True:
            user_choice = input("Enter the number of your answer (1-4): ").strip()
            
            try:
                choice_num = int(user_choice)
                if 1 <= choice_num <= len(options):
                    selected_answer = options[choice_num - 1]
                    return selected_answer
                else:
                    print_error(f"Please enter a number between 1 and {len(options)}.\n")
            except ValueError:
                print_error("Please enter a valid number.\n")
    
    
    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer is correct
        
        Args:
            user_answer (str): The answer provided by the user
            correct_answer (str): The correct answer
        
        Returns:
            bool: True if answer is correct, False otherwise
        """
        return user_answer.lower().strip() == correct_answer.lower().strip()
    
    
    def show_answer_feedback(self, is_correct, correct_answer):
        """
        Show feedback for the answer
        
        Args:
            is_correct (bool): Whether the answer was correct
            correct_answer (str): The correct answer
        """
        print_separator()
        if is_correct:
            print_success("Your answer is correct!")
        else:
            print_error(f"Your answer is incorrect!")
            print_info(f"The correct answer is: {correct_answer}")
        print_separator()
        print()
    
    
    def start_quiz(self, selected_questions=None, shuffle=True):
        """
        Start the quiz game
        
        Args:
            selected_questions (list, optional): Specific questions to use
            shuffle (bool): Whether to shuffle questions
        
        Returns:
            dict: Quiz results containing score, percentage, and answers
        """
        # Use provided questions or all questions
        quiz_questions = selected_questions if selected_questions else self.questions
        
        if not quiz_questions:
            print_error("No questions available to start the quiz!")
            return None
        
        # Shuffle questions if requested
        if shuffle:
            quiz_questions = self.shuffle_questions(quiz_questions)
        
        # Reset score and tracking
        self.score = 0
        self.total_questions = len(quiz_questions)
        self.answers = []
        
        print_section_header("🎯 STARTING QUIZ 🎯")
        print(f"Total Questions: {self.total_questions}")
        print(f"Good luck! You can do it!\n")
        input("Press Enter to continue...")
        
        # Ask each question
        for question_num, question in enumerate(quiz_questions, 1):
            # Clear screen for new question
            from utils import clear_screen
            clear_screen()
            
            # Shuffle options for variety
            question = self.shuffle_options(question)
            
            # Get user answer
            user_answer = self.ask_question(question_num, question)
            
            # Check answer
            correct_answer = question.get("answer", "")
            is_correct = self.check_answer(user_answer, correct_answer)
            
            # Update score
            if is_correct:
                self.score += 1
            
            # Store answer record
            self.answers.append({
                "question": question.get("question", ""),
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "is_correct": is_correct
            })
            
            # Show feedback
            self.show_answer_feedback(is_correct, correct_answer)
            
            # Show score so far
            print_info(f"Current Score: {self.score}/{question_num}")
            print()
            
            # Wait before next question
            if question_num < self.total_questions:
                input("Press Enter for next question...")
            else:
                input("Press Enter to see your results...")
        
        # Return results
        return self.get_quiz_results()
    
    
    def get_quiz_results(self):
        """
        Calculate and return quiz results
        
        Returns:
            dict: Dictionary containing quiz results
        """
        percentage = self.calculate_percentage()
        
        results = {
            "score": self.score,
            "total": self.total_questions,
            "percentage": percentage,
            "answers": self.answers
        }
        
        return results
    
    
    def calculate_percentage(self):
        """
        Calculate percentage of correct answers
        
        Returns:
            float: The percentage of correct answers
        """
        if self.total_questions == 0:
            return 0.0
        
        percentage = (self.score / self.total_questions) * 100
        return round(percentage, 2)
    
    
    def get_performance_message(self, percentage):
        """
        Get a motivational message based on performance
        
        Args:
            percentage (float): The percentage score
        
        Returns:
            str: Performance message
        """
        if percentage >= 90:
            return "🌟 Outstanding! Perfect or near-perfect score!"
        elif percentage >= 80:
            return "⭐ Excellent! You have a great understanding!"
        elif percentage >= 70:
            return "👍 Good job! Keep practicing to improve!"
        elif percentage >= 60:
            return "📚 Average performance. More practice needed!"
        elif percentage >= 50:
            return "💪 Below average. Study harder and try again!"
        else:
            return "🎓 Keep learning! Practice makes perfect!"
    
    
    def display_results(self, player_name, results):
        """
        Display quiz results in a formatted way
        
        Args:
            player_name (str): Name of the player
            results (dict): Quiz results dictionary
        """
        from utils import clear_screen
        clear_screen()
        
        print_section_header("✅ QUIZ COMPLETED ✅")
        
        print(f"Player Name    : {player_name}")
        print(f"Score          : {results['score']}/{results['total']}")
        print(f"Accuracy       : {results['percentage']}%")
        print()
        print(self.get_performance_message(results['percentage']))
        print()
        print_separator()
