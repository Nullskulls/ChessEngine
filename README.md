# ♟️ Python Chess Engine

A terminal-based chess engine built from scratch in Python using ASCII rendering and 2D lists — complete with full move validation, checkmate detection, persistent board saving, and chaotic AI personalities.

> _“Not FIDE-compliant, but compliant with something… maybe.”_

---

## 🧠 Features

- ✅ **Complete move validation** — every piece, every edge case, fully handled  
- ✅ **Check and checkmate logic** — yes, it knows when you’re toast  
- ✅ **Persistent board state** — auto-saves and resumes games via JSON  
- 🤖 **Three unique AI bots**:
  - **Sir Meowzers** – plays random but legal moves  
  - **Miss Whiskers** – doesn’t know the rules and doesn’t care  
  - **Count Catstein** – mostly legit… unless he decides not to be  
- 💬 **In-game quotes** – bots talk trash to keep things interesting  
- 🛠️ **Custom AI support** – easily plug in your own bots  
- 👫 **Pass and play** – two players can share the same board  

---

## 🗃️ Project Structure
```
ChessEngine/
├── Source/
│ ├── main.py # Main game loop
│ ├── Validity.py # All move validation logic
│ ├── Checkmate.py # Check/checkmate logic
│ ├── ManipulateBoard.py # Handles piece moving
│ ├── Converter.py # Converts notation to 2D list coordinates
│ ├── Draw.py # Renders board in terminal
│ └── Bots/
│       ├── Sir_Meowzers.py
│       ├── Miss_Whiskers.py
│       └── Count_Catstein.py
├── board.json # Current saved board state
├── single_player.json # Saved state for bot matches
└── README.md
```

---

## 📖 Dev Journal

The full development timeline is documented in [`Journal.md`](./Journal.md), covering 4 intensive days of validation logic, AI creation, bug fixes, and general problem-solving.

---

## 🚀 How to Run

1. Clone the repo  
2. Run the main file from inside the `Source/` folder:

```bash
python main.py
```
If you get import errors, make sure you’re running from inside the Source/ directory or that Python is pointed to the right project root.

🤝 Credits
Developed solo over 4 days

Original board rendering logic built in May

AI personalities inspired by chaos, cats, and caffeine

⚠️ Disclaimer
This is not FIDE-compliant

Miss Whiskers does not care about your laws

No actual cats were harmed in the making of this engine