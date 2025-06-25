📅 Day 1 – Core Validation Begins
Implemented is_valid_pawn() to handle pawn movement and captures.

Resolved a major bug caused by how Python handles list equality — all pawn moves were being misread as invalid.

Added rook movement using directional ray-casting (horizontal and vertical), setting up reusable mapping logic.

Expanded to bishop, queen, knight, and promotion handling.

Knight logic was initially broken but foundational structure was put in place.

📅 Day 2 – Full Validation & Checkmate Planning
Finalized validation logic for all standard pieces.

Designed the foundation for is_checked() and is_checkmate() logic.

Fixed over 10 critical bugs related to movement, capturing, and board state edge cases.

Created debugging tools to visualize move legality and threat zones for more efficient validation.

📅 Day 3 – Checkmate Overhaul
Completely rewrote the checkmate detection system to handle:

Multiple attackers

Interposition logic

Escape checks

Improved the move_piece() function for clarity and better control flow.

Spent multiple hours debugging and testing board states.

Achieved a functional, if slightly heavy, is_checkmate() implementation with O(n⁴) complexity.

📅 Day 4 – Bots, UX Polish, and Persistence
Added persistent board storage using JSON to allow session recovery.

Implemented 3 unique AI bots:

🐾 Sir Meowzers – plays legal moves randomly.

🐱 Miss Whiskers – always plays illegal moves.

🧪 Count Catstein – plays legal chess 85% of the time, cheats the rest.

Each bot comes with flavor text/quotes to enhance engagement.

Polished UX, improved terminal prompts, and added more robust error messages.

Final bug sweep on Validity, ManipulateBoard, and Checkmate modules.

🧩 Highlights
✅ Fully functional move validation built from scratch

✅ Custom ASCII interface using 2D Python lists

✅ Persistent game saving/loading

✅ Unique AI bots with modding support

🚫 Not FIDE-compliant — but it plays something, and it plays it well

🛠️ Easily extensible with custom AIs or online play in future updates