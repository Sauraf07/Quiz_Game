# Quiz Game System 🎯

A professional, interactive console-based Quiz Game System built with Python. Test your knowledge, compete with others, and climb the leaderboard!

## 🌟 Features

### Core Features
- **Interactive Quiz Gameplay**: Answer multiple-choice questions with instant feedback
- **Question Categorization**: Play quizzes by specific categories or difficulty levels
- **Score Tracking**: Automatic score calculation with percentage accuracy
- **Leaderboard System**: Global leaderboard showing top performers
- **Player Statistics**: View individual player performance metrics
- **Replay System**: Option to play again without returning to menu
- **Randomized Questions**: Questions are shuffled randomly each time

### Advanced Features
- **Multiple Categories**: Questions organized by topics (Python, Web Development, Database, Tools)
- **Difficulty Levels**: Easy, Medium, and Hard difficulty options
- **Question Shuffling**: Both questions and answer options are randomized
- **Data Persistence**: Scores saved to CSV file automatically
- **Input Validation**: Robust error handling for user inputs
- **Color-Coded Feedback**: Visual feedback using colored terminal output
- **Responsive UI**: Professional console interface with formatted output

## 🛠️ Technologies Used

### Backend
- **Python 3.7+** - Core programming language
- **JSON** - For storing questions
- **CSV** - For leaderboard storage
- **Standard Library Modules**:
  - `json` - JSON file handling
  - `csv` - CSV operations
  - `os` - File system operations
  - `datetime` - Timestamp handling
  - `random` - Question shuffling
  - `sys` - System operations

### No External Dependencies Required!
The project uses only Python's standard library, making it easy to run anywhere without additional installations.

## 📁 Project Structure

```
quiz_game_system/
│
├── main.py                    # Entry point - Main application
├── quiz.py                    # Quiz game logic and functionality
├── leaderboard.py             # Leaderboard management system
├── utils.py                   # Utility functions (formatting, input validation)
│
├── questions.json             # Question database (25+ questions)
├── leaderboard.csv            # Leaderboard storage (auto-generated)
│
├── requirements.txt           # Project dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
│
├── assets/
│   └── banner.txt             # ASCII art banner
│
├── docs/
│   ├── project_overview.md    # Architecture and design overview
│   ├── future_scope.md        # Future enhancement possibilities
│   └── flowchart.md           # Application workflow diagram
│
└── screenshots/
    └── output.png             # Sample output (for GitHub)
```

## 🚀 Installation Guide

### Prerequisites
- Python 3.7 or higher
- Windows, macOS, or Linux
- Terminal/Command Prompt

### Steps

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd quiz_game_system
   
   # Or simply extract the project folder
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # Should show Python 3.7 or higher
   ```

3. **Check Project Files**
   ```bash
   # Verify all files are present
   ls  # On Linux/macOS
   dir # On Windows
   ```

4. **Ready to Run!**
   No installation of dependencies needed. All modules are built-in!

## 🎮 How to Run

### Method 1: Direct Python Command

```bash
# Navigate to project directory
cd quiz_game_system

# Run the application
python main.py
```

### Method 2: Run with Python Interpreter

```bash
python -m main
```

### Method 3: Make Executable (Linux/macOS)

```bash
chmod +x main.py
./main.py
```

## 📖 How to Play

### Main Menu
When you start the application, you'll see:
```
1. 🎯  Start Quiz
2. 📊 View Leaderboard
3. 👤 Player Statistics
4. ℹ️  How to Play
5. 🚪 Exit
```

### Starting a Quiz

1. **Select "Start Quiz"** from the main menu
2. **Choose Quiz Type**:
   - Play All Questions
   - Play by Category (Python, Web Development, etc.)
   - Play by Difficulty (Easy, Medium, Hard)
3. **Enter Your Name** (minimum 2 characters)
4. **Answer Questions**:
   - Read each question carefully
   - Select answer by entering the number (1-4)
   - Get instant feedback on correctness
   - See your running score
5. **View Results**:
   - Final score displayed
   - Accuracy percentage shown
   - Performance rating given
   - Score automatically saved

### Viewing Leaderboard
- See top 10 players by score
- View player rankings with accuracy
- Check when scores were achieved

### Player Statistics
- View individual player performance
- See total quizzes played
- Check average accuracy
- Compare best and worst scores

## 📊 Question Format

Questions are stored in `questions.json` with the following structure:

```json
{
  "question": "What is Python?",
  "options": [
    "Programming Language",
    "Snake",
    "Browser",
    "Game"
  ],
  "answer": "Programming Language",
  "difficulty": "easy",
  "category": "Python"
}
```

## 📈 Leaderboard Format

Scores are stored in `leaderboard.csv`:

```
Rank,Player Name,Score,Total Questions,Accuracy (%),DateTime
1,Alice,24,25,96.0,2024-01-15 10:30:45
2,Bob,23,25,92.0,2024-01-15 11:20:30
```

## 🎯 Key Classes and Functions

### QuizGame Class (quiz.py)
- `load_questions()` - Load questions from JSON
- `start_quiz()` - Start the quiz game
- `ask_question()` - Display question and get answer
- `check_answer()` - Validate answer
- `calculate_percentage()` - Compute accuracy
- `get_performance_message()` - Performance feedback

### Leaderboard Class (leaderboard.py)
- `save_score()` - Save player score
- `load_scores()` - Load all scores
- `display_leaderboard()` - Show top 10 players
- `get_player_stats()` - Get player statistics
- `sort_scores()` - Sort by different criteria

### Utility Functions (utils.py)
- `clear_screen()` - Clear console
- `print_banner()` - Display banner
- `validate_input()` - Validate user input
- `print_colored_text()` - Colored output
- `print_success/error/warning/info()` - Styled messages

### Main Application (main.py)
- `QuizGameApp` - Main application class
- `show_main_menu()` - Display main menu
- `start_quiz()` - Handle quiz flow
- `run()` - Main application loop

## 🎨 UI Examples

### Main Menu
```
╔════════════════════════════════════════════════════════════╗
║              🎯 QUIZ GAME SYSTEM 🎯                       ║
╚════════════════════════════════════════════════════════════╝

1. 🎯  Start Quiz
2. 📊 View Leaderboard
3. 👤 Player Statistics
4. ℹ️  How to Play
5. 🚪 Exit

Enter your choice (1-5):
```

### Quiz Question
```
============================================================
Question 1/25
============================================================

Category: Python | Difficulty: EASY
------------------------------------------------------------

What is Python?

  1. Programming Language
  2. A type of snake
  3. A web browser
  4. A game console

Enter the number of your answer (1-4):
```

### Results Screen
```
============================================================
✅ QUIZ COMPLETED ✅
============================================================

Player Name    : John
Score          : 23/25
Accuracy       : 92.0%

⭐ Excellent! You have a great understanding!
```

## 💻 System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7 or higher
- **RAM**: Minimum 50 MB
- **Storage**: ~2 MB for project files
- **Internet**: Not required (offline-first)

## 🔒 Security & Best Practices

✅ **Input Validation**: All user inputs are validated
✅ **Error Handling**: Comprehensive exception handling
✅ **No External Dependencies**: Reduced security risks
✅ **Clean Code**: Modular, readable, maintainable
✅ **Comments**: Well-documented code for beginners

## 🚀 Future Improvements

### Short Term
- [ ] Add timer functionality
- [ ] Implement negative marking system
- [ ] Add hint system for difficult questions
- [ ] Export quiz results to PDF
- [ ] Add question tagging system

### Medium Term
- [ ] Create REST API with Flask/FastAPI
- [ ] Build web interface with React/Vue
- [ ] Implement MySQL/MongoDB database
- [ ] Add user authentication
- [ ] Create mobile app version

### Long Term
- [ ] Multiplayer quiz mode
- [ ] AI-generated questions
- [ ] Real-time leaderboard synchronization
- [ ] Advanced analytics dashboard
- [ ] Machine learning difficulty adjustment

See [future_scope.md](docs/future_scope.md) for detailed information.

## 📚 Documentation

### Available Documentation
- **[https://github.com/Sauraf07/Quiz_Game/blob/main/quiz_game_system/docs/project_overview.md](docs/project_overview.md)** - Architecture and design decisions
- **[http://github.com/Sauraf07/Quiz_Game/blob/main/quiz_game_system/docs/future_scope.md](docs/future_scope.md)** - Roadmap and enhancement ideas
- **[https://github.com/Sauraf07/Quiz_Game/blob/main/quiz_game_system/docs/flowchart.md](docs/flowchart.md)** - Application workflow diagrams

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest improvements
- Add new questions
- Improve documentation
- Optimize code

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**Sauraf Kumar**
- Portfolio: [sauraf-portfolio.vercel.app ](https://portfolio.com)
- GitHub: [https://github.com/Sauraf07](https://github.com)
- LinkedIn: [linkedin.com/in/sauraf07](https://linkedin.com)
- Email: saurafsps7631@gmail.com

## 🙏 Acknowledgments

- Python Community
- All contributors
- Users and testers
- Inspired by educational gaming concepts

## ❓ FAQ

**Q: Can I add more questions?**
A: Yes! Edit `questions.json` and add new question objects following the existing format.

**Q: Where are scores saved?**
A: Scores are automatically saved to `leaderboard.csv` in the project folder.

**Q: Can I delete the leaderboard?**
A: Yes, from the leaderboard menu, but confirm the action first.

**Q: Does it work offline?**
A: Yes! The entire application works completely offline.

**Q: Can I modify the difficulty levels?**
A: Yes, by editing the questions in `questions.json`.

**Q: Is there a time limit for questions?**
A: No, take your time to answer each question.

## 🐛 Troubleshooting

### Issue: Python command not found
**Solution**: Ensure Python is installed and added to PATH. Try `python3` instead of `python`.

### Issue: questions.json not found
**Solution**: Ensure the file is in the same directory as `main.py`.

### Issue: Can't run main.py
**Solution**: Use `python main.py` instead of just `main.py`.

### Issue: No colors in terminal
**Solution**: Your terminal may not support colors. The app will still work fine.

## 📞 Support

For issues or questions:
1. Check the FAQ section
2. Review documentation files
3. Check your Python version: `python --version`
4. Ensure all files are in correct locations

---

**Made with ❤️ for learning and development**

Happy Quizzing! 🎉
