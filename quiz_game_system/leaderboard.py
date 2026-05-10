"""
Leaderboard Module for Quiz Game System
This module handles leaderboard functionality
"""

import csv
import os
from utils import (
    get_current_timestamp, print_section_header, print_separator,
    print_success, print_error, print_info
)


class Leaderboard:
    """
    Leaderboard class for managing scores and rankings
    """
    
    def __init__(self, csv_file="leaderboard.csv"):
        """
        Initialize the leaderboard
        
        Args:
            csv_file (str): Path to the CSV file for storing scores
        """
        self.csv_file = csv_file
        self.scores = []
        
        # Create CSV file with headers if it doesn't exist
        self.initialize_csv()
    
    
    def initialize_csv(self):
        """
        Initialize the CSV file with headers if it doesn't exist
        """
        if not os.path.exists(self.csv_file):
            try:
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Rank', 'Player Name', 'Score', 'Total Questions', 'Accuracy (%)', 'DateTime'])
                print_info(f"Leaderboard file '{self.csv_file}' created!")
            except Exception as e:
                print_error(f"Error creating leaderboard file: {e}")
    
    
    def save_score(self, player_name, score, total_questions, percentage):
        """
        Save a player's score to the leaderboard
        
        Args:
            player_name (str): The name of the player
            score (int): The number of correct answers
            total_questions (int): The total number of questions
            percentage (float): The accuracy percentage
        
        Returns:
            bool: True if save was successful, False otherwise
        """
        try:
            timestamp = get_current_timestamp()
            
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # We'll update rank when displaying
                writer.writerow(['', player_name, score, total_questions, percentage, timestamp])
            
            print_success(f"Score saved for {player_name}!")
            return True
        
        except Exception as e:
            print_error(f"Error saving score: {e}")
            return False
    
    
    def load_scores(self):
        """
        Load all scores from the CSV file
        
        Returns:
            list: List of score records as dictionaries
        """
        try:
            scores = []
            if not os.path.exists(self.csv_file):
                return scores
            
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Player Name']:  # Skip empty rows
                        scores.append(row)
            
            return scores
        
        except Exception as e:
            print_error(f"Error loading scores: {e}")
            return []
    
    
    def sort_scores(self, scores, sort_by='Score', ascending=False):
        """
        Sort scores by a specific column
        
        Args:
            scores (list): List of score records
            sort_by (str): Column to sort by (default: 'Score')
            ascending (bool): Sort in ascending order if True
        
        Returns:
            list: Sorted list of scores
        """
        try:
            # Convert score string to integer for proper sorting
            if sort_by == 'Score':
                scores_copy = scores.copy()
                scores_copy.sort(
                    key=lambda x: int(x['Score']),
                    reverse=not ascending
                )
                return scores_copy
            
            # Convert percentage to float for proper sorting
            elif sort_by == 'Accuracy (%)':
                scores_copy = scores.copy()
                scores_copy.sort(
                    key=lambda x: float(x['Accuracy (%)']),
                    reverse=not ascending
                )
                return scores_copy
            
            # Default sorting
            else:
                scores_copy = scores.copy()
                scores_copy.sort(
                    key=lambda x: x[sort_by],
                    reverse=not ascending
                )
                return scores_copy
        
        except Exception as e:
            print_error(f"Error sorting scores: {e}")
            return scores
    
    
    def get_top_scores(self, limit=10):
        """
        Get top scores from the leaderboard
        
        Args:
            limit (int): Number of top scores to return
        
        Returns:
            list: List of top scores
        """
        scores = self.load_scores()
        
        if not scores:
            return []
        
        # Sort by score (highest first)
        sorted_scores = self.sort_scores(scores, 'Score', ascending=False)
        
        # Return top scores
        return sorted_scores[:limit]
    
    
    def display_leaderboard(self, limit=10):
        """
        Display the leaderboard in a formatted table
        
        Args:
            limit (int): Number of entries to display
        """
        from utils import clear_screen
        clear_screen()
        
        print_section_header("🏆 LEADERBOARD 🏆")
        
        # Load and get top scores
        scores = self.load_scores()
        
        if not scores:
            print_info("No scores in the leaderboard yet!")
            print("Be the first one to play and get on the leaderboard!\n")
            input("Press Enter to continue...")
            return
        
        # Sort by score
        top_scores = self.get_top_scores(limit)
        
        # Display table header
        print(f"{'Rank':<6} {'Player Name':<20} {'Score':<10} {'Accuracy':<12} {'Date & Time':<20}")
        print_separator()
        
        # Display scores
        for rank, score in enumerate(top_scores, 1):
            player_name = score['Player Name'][:19]  # Limit name length
            score_val = score['Score']
            accuracy = score['Accuracy (%)']
            datetime_str = score['DateTime']
            
            print(f"{rank:<6} {player_name:<20} {score_val:<10} {accuracy}%{' ':<9} {datetime_str:<20}")
        
        print_separator()
        print()
        input("Press Enter to go back to menu...")
    
    
    def get_player_stats(self, player_name):
        """
        Get statistics for a specific player
        
        Args:
            player_name (str): The name of the player
        
        Returns:
            dict: Player statistics
        """
        scores = self.load_scores()
        player_scores = [s for s in scores if s['Player Name'].lower() == player_name.lower()]
        
        if not player_scores:
            return None
        
        # Calculate statistics
        total_quizzes = len(player_scores)
        total_correct = sum(int(s['Score']) for s in player_scores)
        total_questions = sum(int(s['Total Questions']) for s in player_scores)
        avg_accuracy = sum(float(s['Accuracy (%)']) for s in player_scores) / total_quizzes
        best_score = max(int(s['Score']) for s in player_scores)
        worst_score = min(int(s['Score']) for s in player_scores)
        
        return {
            "player_name": player_name,
            "total_quizzes": total_quizzes,
            "total_correct": total_correct,
            "total_questions": total_questions,
            "average_accuracy": round(avg_accuracy, 2),
            "best_score": best_score,
            "worst_score": worst_score
        }
    
    
    def display_player_stats(self, player_name):
        """
        Display statistics for a specific player
        
        Args:
            player_name (str): The name of the player
        """
        from utils import clear_screen
        clear_screen()
        
        print_section_header(f"📊 STATISTICS FOR {player_name.upper()}")
        
        stats = self.get_player_stats(player_name)
        
        if not stats:
            print_error(f"No statistics found for player: {player_name}\n")
            input("Press Enter to continue...")
            return
        
        # Display statistics
        print(f"Total Quizzes Played  : {stats['total_quizzes']}")
        print(f"Total Questions Answered : {stats['total_questions']}")
        print(f"Total Correct Answers    : {stats['total_correct']}")
        print(f"Average Accuracy         : {stats['average_accuracy']}%")
        print(f"Best Score              : {stats['best_score']}")
        print(f"Worst Score             : {stats['worst_score']}")
        print()
        print_separator()
        print()
        input("Press Enter to go back to menu...")
    
    
    def clear_leaderboard(self):
        """
        Clear all entries from the leaderboard (with confirmation)
        
        Returns:
            bool: True if cleared, False if cancelled
        """
        confirm = input("\n⚠️  Are you sure you want to clear the entire leaderboard? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            try:
                with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Rank', 'Player Name', 'Score', 'Total Questions', 'Accuracy (%)', 'DateTime'])
                print_success("Leaderboard cleared successfully!")
                return True
            except Exception as e:
                print_error(f"Error clearing leaderboard: {e}")
                return False
        else:
            print_info("Leaderboard clearing cancelled.")
            return False
