# Quiz Game System - Workflow Flowchart

## 📊 Main Application Flow

```
                              ┌─────────────┐
                              │   START     │
                              └──────┬──────┘
                                     │
                              ┌──────▼──────┐
                              │  main.py    │
                              │  executed   │
                              └──────┬──────┘
                                     │
                         ┌───────────▼────────────┐
                         │   QuizGameApp()        │
                         │   Initialize           │
                         │   - quiz object        │
                         │   - leaderboard object │
                         └───────────┬────────────┘
                                     │
                         ┌───────────▼────────────┐
                         │   app.run()            │
                         │   Start main loop      │
                         └───────────┬────────────┘
                                     │
                         ┌───────────▼────────────┐
                         │   show_main_menu()     │
                         │   Display options:     │
                         │   1. Start Quiz        │
                         │   2. Leaderboard       │
                         │   3. Player Stats      │
                         │   4. How to Play       │
                         │   5. Exit              │
                         └───────────┬────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
    Choice=1              Choice=2/3/4              Choice=5
         │                           │                           │
         ▼                           ▼                           ▼
    ┌────────────┐            ┌────────────┐            ┌─────────────┐
    │ Start Quiz │            │  Display   │            │ Exit Game   │
    └────┬───────┘            │  Info/Data │            │             │
         │                    │            │            │ Show goodbye│
         │                    │ Return to  │            │ message     │
         │                    │ main_menu  │            │             │
         │                    └────┬───────┘            └─────┬───────┘
         │                         │                         │
         ▼                         │                         ▼
    ┌────────────────────┐         │                    ┌────────────┐
    │ Load questions()   │         │                    │    EXIT    │
    │ from JSON          │         │                    │   (0)      │
    │ - Success?         │         │                    └────────────┘
    └────┬────┬──────────┘         │
         │    │ No                 │
    Yes  │    └──────────┐         │
         │               ▼         │
         │          ┌─────────┐    │
         │          │  Error  │    │
         │          │  Message│    │
         │          └────┬────┘    │
         │               └─────────┘
         │                         ▲
         ▼
    ┌────────────────────┐
    │  show_quiz_menu()  │
    │  Choose quiz type: │
    │  1. All Questions  │
    │  2. By Category    │
    │  3. By Difficulty  │
    │  4. Back           │
    └────┬────┬──┬───────┘
         │    │  │
      1  │ 2  │3 │ 4
         │    │  └──────────┐
         │    │             ▼
         ▼    │         ┌────────┐
    ┌─────────▼─┐       │  Back  │
    │ All Qs    │       └────────┘
    └────┬──────┘             ▲
         │                    │
    ┌────▼────────┐           │
    │ Category    ├───────────┘
    │ Selection   │
    └────┬────────┘
         │
         ▼
    ┌──────────────────────┐
    │ Difficulty Selection │
    │ - Easy              │
    │ - Medium            │
    │ - Hard              │
    └────┬─────────────────┘
         │
         ▼
    ┌──────────────────────┐
    │ Get Player Name      │
    │ Validation:          │
    │ - Min 2 characters   │
    │ - No numbers only    │
    └────┬─────────────────┘
         │
         ▼
    ┌──────────────────────┐
    │ quiz.start_quiz()    │
    │ Quiz Session Begins  │
    │ - Reset score to 0   │
    │ - Shuffle questions  │
    │ - Start loop         │
    └────┬─────────────────┘
         │
         ▼
    ┌──────────────────────────────┐
    │ For Each Question in Quiz    │
    ├──────────────────────────────┤
    │ Question Counter < Total?    │
    └────┬──────────────────┬──────┘
         │ Yes              │ No (All questions done)
         │                  └──────────┐
         ▼                             │
    ┌──────────────────────────┐      │
    │ clear_screen()           │      │
    │ ask_question()           │      │
    ├──────────────────────────┤      │
    │ Display:                 │      │
    │ - Question number        │      │
    │ - Category & Difficulty  │      │
    │ - Question text          │      │
    │ - 4 options              │      │
    │ - Request: Enter number  │      │
    └────┬─────────────────────┘      │
         │                             │
         ▼                             │
    ┌──────────────────────────┐      │
    │ validate_input()         │      │
    │ Check user answer        │      │
    │ - Valid range 1-4?       │      │
    │ - Retry if invalid       │      │
    └────┬─────────────────────┘      │
         │                             │
         ▼                             │
    ┌──────────────────────────┐      │
    │ check_answer()           │      │
    │ - Compare with correct   │      │
    │ - Return True/False      │      │
    └────┬────────┬────────────┘      │
         │        │                   │
      True│        │False              │
         │        │                   │
         ▼        ▼                   │
    ┌────────┐ ┌──────────┐           │
    │ Correct│ │ Incorrect│           │
    │Answer  │ │ Answer   │           │
    └────┬───┘ └────┬─────┘           │
         │          │                 │
         ▼          ▼                 │
    ┌──────────────────────────┐      │
    │ show_answer_feedback()   │      │
    ├──────────────────────────┤      │
    │ Display:                 │      │
    │ ✓ "Correct!"            │      │
    │ or                       │      │
    │ ✗ "Wrong!"              │      │
    │ Correct Answer: [...]    │      │
    └────┬─────────────────────┘      │
         │                             │
         ▼                             │
    ┌──────────────────────────┐      │
    │ Update score             │      │
    │ score += 1 (if correct)  │      │
    │ Add to answers list      │      │
    └────┬─────────────────────┘      │
         │                             │
         ▼                             │
    ┌──────────────────────────┐      │
    │ Display:                 │      │
    │ Current Score: X/Y       │      │
    │ Press Enter for next...  │      │
    └────┬─────────────────────┘      │
         │                             │
         └─────────────────────────────┼──┐
                                       │  │
                    ┌──────────────────┘  │
                    │                     │
                    ▼                     │
            ┌──────────────────┐          │
            │ Calculate Results│          │
            │ - Final score    │          │
            │ - Percentage     │          │
            │ - Performance msg│          │
            └────┬─────────────┘          │
                 │                        │
                 ▼                        │
            ┌──────────────────┐          │
            │ display_results()│          │
            │ Show:            │          │
            │ - Player name    │          │
            │ - Score: X/Y     │          │
            │ - Accuracy: Z%   │          │
            │ - Performance msg│          │
            └────┬─────────────┘          │
                 │                        │
                 ▼                        │
            ┌──────────────────┐          │
            │ save_score()     │          │
            │ Save to CSV:     │          │
            │ - Name, Score    │          │
            │ - Percentage     │          │
            │ - Timestamp      │          │
            │ Confirmation msg │          │
            └────┬─────────────┘          │
                 │                        │
                 ▼                        │
            ┌──────────────────────┐      │
            │ "Play again?"         │      │
            │ - Input: yes/no       │      │
            └────┬──────────┬───────┘      │
                 │          │              │
              yes│          │no            │
                 │          │              │
                 └──┬───────┘              │
                    │                     │
                    ├─────────────────────┘
                    │
         ┌──────────▼───────────┐
         │ Return to Main Menu  │
         └──────────┬───────────┘
                    │
                    ▼
            ┌────────────────┐
            │ show_main_menu()
            │ (Loop continues)
            └────────────────┘
```

---

## 🎮 Detailed Quiz Question Loop

```
        ┌─────────────────────────┐
        │ Start Question Loop     │
        │ question_num = 1        │
        │ score = 0               │
        │ answers = []            │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ For question in quiz    │
        │ questions:              │
        └────────────┬────────────┘
                     │
          ┌──────────▼──────────┐
          │ Question Number     │
          │ < Total?            │
          └────┬────────┬───────┘
               │        │
            Yes│        │No
               │        └──────────┐
               │                   │
               ▼                   │
        ┌─────────────────────┐   │
        │ Shuffle options()   │   │
        │ Randomize answers   │   │
        │ while keeping       │   │
        │ correct answer same │   │
        └────────┬────────────┘   │
                 │                 │
                 ▼                 │
        ┌──────────────────────┐  │
        │ ask_question()       │  │
        │ Display:             │  │
        │ Q: "..."             │  │
        │ A: 1. ...            │  │
        │ B: 2. ...            │  │
        │ C: 3. ...            │  │
        │ D: 4. ...            │  │
        │ Input validation:    │  │
        │ - Must be 1-4        │  │
        │ - Retry if invalid   │  │
        │ - Trim whitespace    │  │
        │ Return: user_answer  │  │
        └────┬─────────────────┘  │
             │                     │
             ▼                     │
        ┌──────────────────────┐  │
        │ check_answer()       │  │
        │ Compare:             │  │
        │ user_answer ==       │  │
        │ correct_answer?      │  │
        │ (case-insensitive)   │  │
        │ Return: bool         │  │
        └────┬────────┬────────┘  │
             │        │            │
          True│        │False       │
             │        │            │
             ▼        ▼            │
        ┌────────┐┌──────────┐    │
        │✓Correct││✗Incorrect│   │
        └────┬───┘└────┬─────┘    │
             │         │          │
             ├─────┬───┘          │
             │     │              │
             ▼     ▼              │
        ┌──────────────────────┐  │
        │ show_feedback()      │  │
        │ Display message      │  │
        │ Display correct ans. │  │
        └────┬─────────────────┘  │
             │                     │
             ▼                     │
        ┌──────────────────────┐  │
        │ Update score         │  │
        │ if is_correct:       │  │
        │   score += 1         │  │
        │ else:                │  │
        │   score += 0         │  │
        └────┬─────────────────┘  │
             │                     │
             ▼                     │
        ┌──────────────────────┐  │
        │ Store answer record  │  │
        │ answers.append({     │  │
        │   "question": q,     │  │
        │   "user_answer": ua, │  │
        │   "correct": ca,     │  │
        │   "is_correct": ic   │  │
        │ })                   │  │
        └────┬─────────────────┘  │
             │                     │
             ▼                     │
        ┌──────────────────────┐  │
        │ Show progress        │  │
        │ "Q: 3/25"            │  │
        │ "Score: 2/3"         │  │
        └────┬─────────────────┘  │
             │                     │
             ▼                     │
        ┌──────────────────────┐  │
        │ question_num += 1    │  │
        │ Continue loop?       │  │
        │ Ask for next Qs      │  │
        │ Press Enter          │  │
        └────┬─────────────────┘  │
             │                     │
             └──────────┬──────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │ End of Quiz           │
            │ Return results dict:  │
            │ - score: int          │
            │ - total: int          │
            │ - percentage: float   │
            │ - answers: list       │
            └───────────────────────┘
```

---

## 📊 Leaderboard Flow

```
         ┌──────────────────────┐
         │ View Leaderboard     │
         │ Option 2 from menu   │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ leaderboard.         │
         │ display_leaderboard()│
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ load_scores()        │
         │ Read leaderboard.csv │
         │ Parse CSV data       │
         │ Return: list of      │
         │ score dicts          │
         └────┬───────┬─────────┘
              │       │
              │    No data
         Yes  │       │
              │       ▼
              │   ┌──────────────┐
              │   │ "No scores   │
              │   │  yet!"       │
              │   │ Return early │
              │   └──────────────┘
              │
              ▼
         ┌──────────────────────┐
         │ get_top_scores(10)   │
         │ - Sort by Score DESC │
         │ - Limit to top 10    │
         │ Return: sorted list  │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Display Table        │
         │ Header:              │
         │ Rank │Name│Score│    │
         │      │    │     │Acc% │
         ├──────┼────┼─────┼──┤
         │ 1    │Alice│24  │96%  │
         │ 2    │Bob  │23  │92%  │
         │ 3    │...  │... │...  │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Press Enter to       │
         │ Return to Menu       │
         └──────────────────────┘
```

---

## 👤 Player Statistics Flow

```
         ┌──────────────────────────┐
         │ View Player Statistics   │
         │ Option 3 from menu       │
         └────────┬─────────────────┘
                  │
                  ▼
         ┌──────────────────────────┐
         │ Get player name input    │
         │ Input validation         │
         └────────┬─────────────────┘
                  │
                  ▼
         ┌──────────────────────────┐
         │ leaderboard.             │
         │ get_player_stats(name)   │
         └────────┬────────┬────────┘
                  │        │
            Found │        │Not found
                  │        │
                  ▼        ▼
         ┌──────────────┐┌──────────────┐
         │ Calculate:   ││ "No stats    │
         │ - Total Qs   ││ for player"  │
         │ - Avg %      ││ Return       │
         │ - Best score ││              │
         │ - Worst      ││              │
         │ Return: dict ││              │
         └────┬─────────┘└──────────────┘
              │
              ▼
         ┌──────────────────────┐
         │ Display Stats        │
         │ Total Quizzes: 5     │
         │ Avg Accuracy: 85%    │
         │ Best Score: 24/25    │
         │ Worst Score: 18/25   │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Press Enter to       │
         │ Return to Menu       │
         └──────────────────────┘
```

---

## 💾 Data Persistence Flow

```
        ┌─────────────────────────┐
        │ After Quiz Completes    │
        └────────┬─────────────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │ save_score()             │
        │ Leaderboard class        │
        ├──────────────────────────┤
        │ Input:                   │
        │ - player_name: str       │
        │ - score: int             │
        │ - total_questions: int   │
        │ - percentage: float      │
        └────────┬─────────────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │ get_current_timestamp()  │
        │ Get: YYYY-MM-DD HH:MM:SS │
        └────────┬─────────────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │ Open leaderboard.csv in  │
        │ Append mode ('a')        │
        │ Check: file exists?      │
        └────┬──────────┬──────────┘
             │          │
          Yes│          │No
             │          ▼
             │   ┌─────────────────┐
             │   │ Create new file │
             │   │ Add headers:    │
             │   │ Rank, Name,     │
             │   │ Score, Total,   │
             │   │ Accuracy, Time  │
             │   └────────┬────────┘
             │            │
             └────────┬───┘
                      │
                      ▼
        ┌──────────────────────────┐
        │ Write CSV row:           │
        │ writer.writerow([        │
        │   '',                    │
        │   player_name,           │
        │   score,                 │
        │   total_questions,       │
        │   percentage,            │
        │   timestamp              │
        │ ])                       │
        └────────┬─────────────────┘
                 │
                 ▼
        ┌──────────────────────────┐
        │ Close file               │
        │ Success message displayed│
        │ "Score saved!"           │
        └──────────────────────────┘
```

---

## 🔄 Complete User Session Example

```
User starts app
        │
        ▼
Sees Main Menu
        │
Select "1. Start Quiz"
        │
        ▼
Load questions from JSON
        │
        ▼
Select "2. By Category"
        │
        ▼
Select "Python"
        │
        ▼
Enter name "John"
        │
        ▼
Start Quiz with Python questions
        │
        ├─ Question 1: Correct ✓
        ├─ Question 2: Wrong ✗
        ├─ Question 3: Correct ✓
        ├─ Question 4: Correct ✓
        └─ Question 5: Wrong ✗
        │
        ▼
Quiz Complete
        │
Display Results:
- Score: 3/5
- Accuracy: 60%
- Message: "Good job!"
        │
        ▼
Save score to leaderboard.csv
        │
        ▼
"Play again?" - No
        │
        ▼
Return to Main Menu
        │
Select "2. View Leaderboard"
        │
        ▼
Display top 10 players
(John's score now visible)
        │
        ▼
Select "5. Exit"
        │
        ▼
Goodbye message
        │
        ▼
Application closes
```

---

## 📋 Input Validation Flowchart

```
         ┌──────────────────────┐
         │ User Input Request   │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Get input from user  │
         │ input() function     │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Strip whitespace     │
         │ .strip()             │
         └────────┬─────────────┘
                  │
                  ▼
         ┌──────────────────────┐
         │ Check if empty?      │
         └────┬──────────┬──────┘
              │          │
           Yes│          │No
              │          │
              ▼          ▼
         ┌────────┐  ┌──────────────┐
         │ "Empty"│  │ Check type   │
         │ Error  │  │ int/string   │
         │ Retry  │  │ /choice?     │
         └────┬───┘  └──────┬───────┘
              │             │
              ▼             ├─int: try int()
         Return to input    │  ├─Success:
         prompt             │  │ Check range
                            │  └─Fail: Error
                            │
                            ├─string:
                            │ Check length ≥ 2
                            │
                            └─choice:
                              Check valid options
                              │
                              ├─Valid
                              │ Return choice
                              │
                              └─Invalid
                                Error message
                                Retry

         Final: Return validated input
```

---

## 📞 Error Handling Flowchart

```
         ┌──────────────────────┐
         │ Try Block            │
         │ Execute operation    │
         └────────┬─────────────┘
                  │
              ┌───┴───┐
              │       │
          Success   Exception
              │       │
              ▼       ▼
         Return  ┌──────────────────┐
                 │ Catch Exception  │
                 └────┬───┬────┬────┘
                      │   │    │
            FileNotFound KeyError ValueError
                      │   │    │
                      ▼   ▼    ▼
                  ┌─────────────────────┐
                  │ Print error message │
                  │ "File not found"    │
                  │ "Invalid key"       │
                  │ "Invalid value"     │
                  └────────┬────────────┘
                           │
                           ▼
                  ┌─────────────────────┐
                  │ Prompt user:        │
                  │ Retry/Skip/Exit?    │
                  └─────────────────────┘
```

---

**This flowchart provides a comprehensive visual representation of the Quiz Game System's workflow. Each component is clearly documented to help understand the application flow.**

---

*Last Updated: January 2024*
*Complexity Level: Beginner to Intermediate*
