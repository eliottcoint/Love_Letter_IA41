# Love Letter IA

## Overview
**Love Letter IA** is a digital adaptation of the popular card game "Love Letter," where players compete against an AI opponent. The game features an interactive graphical user interface (GUI) and strategic gameplay designed to challenge the player's decision-making skills against a computer-controlled opponent.

## Features
- **AI Opponent:** Compete against an AI that makes strategic decisions based on game state and player actions.
- **Graphical User Interface (GUI):** A user-friendly interface that allows players to easily interact with the game, including selecting cards and viewing game progress.
- **Game Mechanics:** Full implementation of the "Love Letter" game rules, including card effects, player turns, and win conditions.

## Technologies Used
- **Python:** Core language used for the project.
- **Libraries:** 
  - **Pygame:** Used for creating the graphical user interface.
  - **Random:** Used for game mechanics such as shuffling cards and random events.

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/eliottcoint/Love_Letter_IA41.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd Love_Letter_IA41
   ```

3. **Install Dependencies:**
   - If using a `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
   - If not, manually install the required libraries:
   ```bash
   pip install pygame
   ```

4. **Run the Game:**
   ```bash
   python main.py
   ```

## Gameplay Instructions

### Objective
The objective of **Love Letter** is to eliminate your opponent (the AI) or to hold the highest-value card when the deck is exhausted. Players achieve this by strategically playing cards, each with unique effects, to gain an advantage.

### Setup
- Each player (you and the AI) is dealt one card at the start of the game.
- The remaining cards form the draw deck, with the top card removed and set aside (face down) to add some unpredictability.

### Game Flow
1. **Draw Phase:**
   - At the start of your turn, draw one card from the deck, so you have two cards in your hand.
   
2. **Play Phase:**
   - Choose one of the two cards to play. Each card has a specific effect that influences the game. After playing a card, its effect is immediately resolved, and it is discarded.

3. **AI Turn:**
   - The AI then follows the same draw and play phases.

4. **Round End:**
   - A round ends in one of two ways:
     1. If a player is knocked out by a card effect (e.g., the Guard correctly guesses their card).
     2. If the draw deck is empty, the player with the highest-value card in hand wins the round.

5. **Winning the Game:**
   - The game continues until a player wins a pre-determined number of rounds.

### Card Effects
Each card has a unique effect, and understanding these is key to mastering the game:

- **Guard (1):** Guess the AI's hand. If correct, the AI is knocked out.
- **Priest (2):** Look at the AI's hand.
- **Baron (3):** Compare hands with the AI. The player with the lower value is knocked out.
- **Handmaid (4):** Protect yourself from other card effects until your next turn.
- **Prince (5):** Choose any player (including yourself) to discard their hand and draw a new card.
- **King (6):** Trade hands with the AI.
- **Countess (7):** Must be discarded if you also have the King or Prince in hand.
- **Princess (8):** If you discard this card for any reason, you are immediately knocked out.

### Tips and Strategy
- **Bluffing:** Use the Guard wisely to eliminate the AI early by correctly guessing their card.
- **Card Counting:** Pay attention to the cards that have been played to deduce what might still be in the AI's hand.
- **Timing:** Hold onto high-value cards like the Princess until the end, but be wary of effects that might force you to discard them.

## Customization
- **Card Effects:** Adjust or extend the game mechanics by modifying the card effects in the codebase.

## Contributing
Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For any questions, suggestions, or feedback, feel free to reach out via my [GitHub profile](https://github.com/eliottcoint).
