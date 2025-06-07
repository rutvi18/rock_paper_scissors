
---

# ✊✋✌️ Rock, Paper, Scissors Game in Python

This is a simple **Rock, Paper, Scissors** game implemented in Python. The user selects an option by entering a number from **1 to 3**, and the computer randomly selects its option. The choices are then compared to determine the winner.

---

## 🎮 Game Rules

* **1 = Rock**
* **2 = Paper**
* **3 = Scissors**

**Winning Conditions:**

* Rock beats Scissors
* Paper beats Rock
* Scissors beats Paper

If both the user and the computer make the same choice, it's a **draw**.

---

## 🐍 Prerequisites

* Python 3.x
* No external libraries required (`random` module is built-in)

---

## ▶️ How to Run

1. Save the Python code in a file, e.g., `rps_game.py`.
2. Open a terminal or command prompt.
3. Run the game:

```bash
python rps_game.py
```

---

## 💻 Sample Code

```python
import random

# Mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

# User input
user_choice = int(input("Enter your choice (1: Rock, 2: Paper, 3: Scissors): "))

# Validate input
if user_choice not in choices:
    print("Invalid choice! Please enter a number between 1 and 3.")
else:
    # Computer makes a random choice
    computer_choice = random.randint(1, 3)

    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")
```

---

## 🧠 Concepts Used

* `random.randint()` for computer choice
* `if-else` conditions for comparing choices
* Dictionary for mapping numbers to game choices
* Basic input/output in Python

---

## 📌 Notes

* You can expand this game to allow multiple rounds or keep score.
* For better user experience, add input validation and exception handling.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---
