# 🍥 Naruto vs Madara — Mini Browser Game ⚔️

<p align="center">

**🌀 A Naruto-Themed Platform Adventure Game 🌀**

*Move • Jump • Collect Chakra • Defeat Madara • Reach the Finish*

</p>

---

## 📌 Project Overview

**Naruto vs Madara — Mini Browser Game** is a simple anime-themed platform game developed using **HTML, CSS, and JavaScript** and executed inside a **Python/Jupyter Notebook environment**.

The game provides a small interactive platform-game experience where the player controls **Naruto**. The main objective is to move through the game area, jump across platforms, collect Chakra, avoid enemy collisions, defeat **Madara**, and finally reach the finish area.

The project combines **Python, HTML, CSS, and JavaScript** to demonstrate how an interactive browser-based game can be created and displayed inside a notebook environment.

The game also includes basic game mechanics such as:

* 🎮 Player movement
* 🦘 Jumping
* 🌍 Gravity
* 💠 Collectibles
* ⚔️ Enemy movement
* 💥 Collision detection
* ❤️ Lives system
* 🏆 Victory condition
* 💀 Game Over condition
* 🔄 Restart functionality

---

# 🎮 Game Features

## 🍥 Naruto Player

Naruto is the main playable character.

The player can control Naruto using keyboard inputs and move around the game area.

Naruto can:

* Move left
* Move right
* Jump
* Land on platforms
* Collect Chakra
* Fight Madara
* Reach the finish area

---

## ⚔️ Madara Enemy

Madara acts as the main enemy of the game.

Madara moves continuously between defined positions, creating a moving obstacle for the player.

The player must carefully time the jump and land on Madara to defeat him.

### Madara Battle Logic

```text
Naruto approaches Madara
        ↓
Collision detected
        ↓
Successful landing?
     ↙       ↘
   YES        NO
    ↓          ↓
Madara       Lose Life
Defeated        ↓
    ↓       Naruto Reset
Continue
```

---

# 💠 Chakra Collection System

Chakra acts as the collectible item in the game.

When Naruto touches a Chakra orb:

```text
Naruto
   ↓
Touches Chakra
   ↓
Chakra Collected
   ↓
Chakra Disappears
   ↓
Score Increases
```

After defeating Madara, Naruto also receives additional Chakra.

The final victory screen displays the amount of Chakra collected during the game.

---

# ❤️ Lives System

Naruto starts the game with **3 lives**.

The lives system gives the player multiple chances to complete the level.

### Life Flow

```text
❤️❤️❤️
  ↓
Collision with Madara
  ↓
❤️❤️
  ↓
Another unsuccessful collision
  ↓
❤️
  ↓
Another life lost
  ↓
💀 GAME OVER
```

When Naruto loses a life, the character is reset to the starting position.

---

# 🪜 Platform System

The game contains multiple platforms that allow Naruto to move vertically through the level.

Platforms work together with the game's gravity and jumping system.

Naruto can:

* Jump from the ground
* Land on platforms
* Move between different platform levels
* Use platforms to reach the enemy and finish area

---

# 🌙 Game Environment

The game uses an animated-style **night background** to create an anime-inspired game environment.

The game area contains different visual elements including:

* 🌙 Night-themed background
* 🪜 Platforms
* 🍥 Naruto
* ⚔️ Madara
* 💠 Chakra
* 🏁 Finish area

These elements are arranged using HTML and CSS positioning.

---

# 🕹️ Controls

| Key                 | Action     |
| ------------------- | ---------- |
| `A` / `←`           | Move Left  |
| `D` / `→`           | Move Right |
| `W` / `↑` / `Space` | Jump       |

### 🎮 Movement

Press **A** or the **Left Arrow** key to move Naruto towards the left.

Press **D** or the **Right Arrow** key to move Naruto towards the right.

### 🦘 Jump

Press **W**, **Up Arrow**, or **Spacebar** to make Naruto jump.

---

# 🎯 How the Game Works

## 1️⃣ Start the Game

When the notebook code is executed, the game area is created.

The game initializes:

* 🍥 Naruto
* ⚔️ Madara
* 💠 Chakra objects
* 🪜 Platforms
* ❤️ Lives
* 🏆 Finish area

The player can then begin controlling Naruto.

---

## 2️⃣ Move Naruto

The player uses the keyboard to control Naruto.

```text
A / ←  → Move Left
D / →  → Move Right
```

The movement system updates Naruto's position according to the pressed key.

---

## 3️⃣ Jump Across Platforms

Naruto can jump using:

```text
W
↑
Space
```

The game applies basic gravity and jump physics.

When Naruto jumps:

```text
Jump
 ↓
Move Up
 ↓
Gravity Applied
 ↓
Move Down
 ↓
Land on Platform
```

---

## 4️⃣ Collect Chakra

Chakra objects are placed throughout the game area.

When Naruto overlaps with a Chakra object:

```text
Collision
   ↓
Chakra Collected
   ↓
Object Removed
   ↓
Score Updated
```

---

## 5️⃣ Encounter Madara

Madara continuously moves between two positions.

This means the player needs to observe Madara's movement and time the jump correctly.

---

## 6️⃣ Fight Madara

Naruto must jump onto Madara successfully.

If Naruto lands on Madara:

```text
Naruto
   ↓
Jump
   ↓
Land on Madara
   ↓
Madara Defeated
   ↓
Madara Disappears
   ↓
Additional Chakra
```

---

## 7️⃣ Lose a Life

If Naruto collides with Madara without successfully landing on him, the player loses one life.

After losing a life:

```text
Life - 1
   ↓
Naruto Reset
   ↓
Continue Playing
```

The game continues as long as at least one life remains.

---

## 8️⃣ Defeat Madara

Once Naruto successfully lands on Madara, Madara is defeated.

The player then needs to continue moving through the game area.

Defeating Madara is **not the final step**.

---

## 9️⃣ Reach the Finish Area

After Madara has been defeated, Naruto must reach the designated finish area.

The final winning condition requires both:

```text
⚔️ Madara Defeated
        +
🏁 Finish Area Reached
        ↓
🏆 NARUTO WINS!
```

---

# 🧠 Game Logic Flow

```text
              🎮 START
                  ↓
          🍥 Create Naruto
                  ↓
       ⚔️ Create Madara Enemy
                  ↓
          💠 Create Chakra
                  ↓
           🪜 Create Platforms
                  ↓
             ❤️ 3 Lives
                  ↓
          🕹️ Player Controls
                  ↓
        🏃 Move / 🦘 Jump
                  ↓
          💥 Collision Check
                  ↓
       ┌──────────┴──────────┐
       ↓                     ↓
  Chakra Collision       Madara Collision
       ↓                     ↓
 Collect Chakra        Successful Landing?
                             ↓
                    ┌────────┴────────┐
                    ↓                 ↓
                   YES                NO
                    ↓                 ↓
             Defeat Madara       Lose a Life
                    ↓                 ↓
                    └────────┬────────┘
                             ↓
                    Madara Defeated?
                             ↓
                            YES
                             ↓
                    🏁 Reach Finish
                             ↓
                         🏆 VICTORY
```

---

# 🧠 Main Technologies

## 🐍 Python

Python is used as the notebook environment from which the game is launched and displayed.

The project uses Python to integrate the interactive browser-based game into the Jupyter Notebook environment.

---

## 🌐 HTML

HTML provides the basic structure of the game.

It is responsible for creating the game elements and containers used by the browser.

---

## 🎨 CSS

CSS is used to style the game interface.

It controls things such as:

* Game layout
* Positioning
* Background appearance
* Platforms
* Character appearance
* Visual effects
* Game screens
* Animations

---

## ⚡ JavaScript

JavaScript controls the interactive behaviour of the game.

It handles:

* Player movement
* Jumping
* Gravity
* Enemy movement
* Collision detection
* Chakra collection
* Lives
* Victory logic
* Game Over logic
* Restart functionality
* Keyboard events

---

## 📓 Jupyter Notebook

The complete game can be executed inside a Jupyter Notebook environment.

The notebook acts as the environment for running the Python code and displaying the browser-based game output.

---

# ⚙️ Game Physics

The game uses simple physics concepts to create realistic player movement.

### 🌍 Gravity

```text
Gravity = 0.6
```

Gravity controls the downward movement of Naruto after jumping.

---

### 🦘 Jump Power

```text
Jump Power = -12
```

The jump power determines the initial upward movement when Naruto jumps.

---

### 🏃 Movement Speed

```text
Movement Speed = 5
```

This controls how quickly Naruto moves horizontally.

---

### ⚔️ Enemy Speed

```text
Enemy Speed = 1.5
```

This controls Madara's continuous movement between positions.

---

# 💥 Collision Detection

Collision detection is one of the main components of the game.

The game uses an `overlap()` function to determine whether two rectangular game objects are touching each other.

Collision detection is used between:

### 🍥 Naruto vs 💠 Chakra

Used to determine when Chakra has been collected.

### 🍥 Naruto vs ⚔️ Madara

Used to determine whether Naruto successfully defeats Madara or loses a life.

### 🍥 Naruto vs 🪜 Platforms

Used to determine whether Naruto lands on or interacts with platforms.

---

# 🏆 Winning Condition

Naruto must complete **two major objectives** to win the game.

### Objective 1

⚔️ Defeat Madara by successfully landing on him.

### Objective 2

🏁 Reach the finish area after Madara has been defeated.

Only after completing both conditions does the game display:

```text
🏆 NARUTO WINS!
```

The victory screen also displays the amount of Chakra collected.

---

# 💀 Game Over Condition

Naruto starts with:

```text
❤️ ❤️ ❤️
3 Lives
```

If Naruto loses all three lives:

```text
❤️ → ❤️ → ❤️
       ↓
   0 Lives
       ↓
💀 GAME OVER
```

The player can then use the **Play Again** option to restart the game.

---

# 🔄 Restart System

The game provides a **Play Again / Restart** option.

This allows the player to restart the game after:

* 🏆 Winning
* 💀 Losing all lives

The game can therefore be played repeatedly without manually rerunning the entire notebook cell.

---

# 🏗️ Game Architecture

The project can be viewed as several connected systems:

```text
                🎮 GAME
                   │
       ┌───────────┼───────────┐
       ↓           ↓           ↓
    PLAYER       ENEMY      WORLD
       │           │           │
    Naruto       Madara     Platforms
       │           │           │
       └───────────┼───────────┘
                   ↓
            💥 COLLISION
                   ↓
       ┌───────────┼───────────┐
       ↓           ↓           ↓
    Chakra       Lives       Finish
       │           │           │
       └───────────┼───────────┘
                   ↓
             GAME RESULT
              ↙        ↘
          🏆 WIN      💀 GAME OVER
```

---

# 📂 Project Structure

```text
Naruto-Vs-Madara-Game/
│
├── Naruto_vs_Madara_Game.ipynb
│
├── README.md
│
└── screenshots/
    │
    └── game-output.png
```

### 📓 `Naruto_vs_Madara_Game.ipynb`

Contains the Python/Jupyter Notebook code used to create and run the game.

### 📄 `README.md`

Contains project information, features, controls, game logic, technologies, and instructions.

### 🖼️ `screenshots/`

Contains screenshots of the game output.

---

# 🚀 How to Run

## Step 1 — Open the Notebook

Open:

```text
Naruto_vs_Madara_Game.ipynb
```

using:

* Jupyter Notebook
* JupyterLab
* Google Colab

---

## Step 2 — Run the Code

Run the notebook cell containing the game code.

The Python code creates and displays the interactive game.

---

## Step 3 — Start Playing

Once the game appears:

```text
🏃 Move Naruto
       ↓
🦘 Jump
       ↓
💠 Collect Chakra
       ↓
⚔️ Defeat Madara
       ↓
🏁 Reach Finish
       ↓
🏆 Win
```

---

# 🎓 Learning Outcomes

This project provides practical understanding of several programming and web-development concepts.

## Programming Concepts

* Variables and constants
* Functions
* Conditional statements
* Arrays
* Loops
* Event handling
* Game-state management

## Web Technologies

* HTML structure
* CSS styling
* CSS positioning
* CSS animations
* JavaScript interaction
* DOM manipulation
* Keyboard event handling

## Game Development Concepts

* Player movement
* Enemy movement
* Gravity
* Jump physics
* Collision detection
* Collectibles
* Lives system
* Game loops
* Win conditions
* Game Over conditions
* Restart functionality

---

# 💡 Key Programming Concepts Demonstrated

### 🔹 Variables

Variables are used to store important game information such as player position, movement values, lives, Chakra count, and game state.

### 🔹 Functions

Functions organize different game operations into reusable blocks.

### 🔹 Conditional Statements

Conditions are used to decide what should happen when Naruto collects Chakra, collides with Madara, loses a life, defeats Madara, or reaches the finish.

### 🔹 Arrays

Arrays can be used to manage collections of game objects such as platforms and Chakra objects.

### 🔹 Event Listeners

Keyboard event listeners detect player input and allow Naruto to respond to keyboard controls.

### 🔹 DOM Manipulation

JavaScript interacts with HTML elements to update the game dynamically.

---

# 🔬 Game State Management

The game maintains different states depending on the player's progress.

```text
🎮 Playing
   ↓
💠 Collecting Chakra
   ↓
⚔️ Fighting Madara
   ↓
🏁 Completing Finish
   ↓
🏆 Victory
```

or:

```text
🎮 Playing
   ↓
💥 Collision
   ↓
❤️ Lose Life
   ↓
❤️ Lives = 0
   ↓
💀 Game Over
```

This allows the game to respond differently depending on the current situation.

---

# 📊 Game Objectives

| Objective         | Purpose                      |
| ----------------- | ---------------------------- |
| 🏃 Move           | Navigate the game area       |
| 🦘 Jump           | Reach platforms and Madara   |
| 💠 Collect Chakra | Increase Chakra score        |
| ⚔️ Defeat Madara  | Complete the enemy challenge |
| ❤️ Protect Lives  | Avoid losing all lives       |
| 🏁 Reach Finish   | Complete the level           |
| 🏆 Win            | Finish the game successfully |

---

# 🔮 Future Improvements

The current project can be expanded with additional features.

### ⚔️ Combat System

Add Naruto attack animations and interactive attack mechanics.

### 🗺️ Multiple Levels

Create multiple stages with different platforms and challenges.

### 👥 More Characters

Add additional Naruto-themed characters.

### 👹 More Enemies

Introduce different enemies with different movement patterns.

### ❤️ Health Bar

Add a health bar alongside the existing lives system.

### ⚡ Power-Ups

Add additional collectible power-ups with different effects.

### 🎵 Sound Effects

Add background music, jump sounds, Chakra collection sounds, and battle effects.

### 📱 Mobile Controls

Add touch-based controls for mobile devices.

### 🏅 High Score

Store and display the player's highest Chakra score.

---

# 🌟 Why This Project?

This project was created as a practical way to combine programming concepts with an interactive game.

Instead of using only theoretical programming examples, the project demonstrates how different technologies can work together:

```text
🐍 Python
    +
🌐 HTML
    +
🎨 CSS
    +
⚡ JavaScript
    ↓
🎮 Interactive Game
```

The project shows how basic programming concepts can be converted into an interactive application.

---

# 📸 Screenshots

Add your game screenshot here:

```text
screenshots/game-output.png
```

Example Markdown:

```markdown
![Naruto vs Madara Game](screenshots/game-output.png)
```

---

# 🛠️ Project Information

| Category               | Details                      |
| ---------------------- | ---------------------------- |
| 🎮 Project             | Naruto vs Madara Mini Game   |
| 🧩 Type                | Browser-Based Platform Game  |
| 🐍 Backend/Environment | Python / Jupyter Notebook    |
| 🌐 Frontend            | HTML                         |
| 🎨 Styling             | CSS                          |
| ⚡ Game Logic           | JavaScript                   |
| 🍥 Theme               | Naruto Anime                 |
| 💠 Main Collectible    | Chakra                       |
| ⚔️ Main Enemy          | Madara                       |
| ❤️ Lives               | 3                            |
| 🏆 Final Goal          | Defeat Madara & Reach Finish |

---

# 📚 Conclusion

**Naruto vs Madara — Mini Browser Game** is a small but practical project that demonstrates how programming, web technologies, game physics, and user interaction can be combined to create an interactive application.

The player controls Naruto, moves through platforms, collects Chakra, manages three lives, fights Madara, and finally reaches the finish area.

The project provides hands-on experience with:

**HTML + CSS + JavaScript + Python/Jupyter + Game Logic + Collision Detection + Basic Physics**

---

# 🍥 Naruto vs Madara ⚔️

```text
       🌀 COLLECT CHAKRA
              ↓
        🦘 JUMP HIGH
              ↓
         ⚔️ DEFEAT MADARA
              ↓
         🏁 REACH FINISH
              ↓
         🏆 NARUTO WINS!
```

### ⭐ If you like this project

Feel free to **Star ⭐ the repository** and explore the code!

**Made with 💻 Code + 🌀 Creativity + 🍥 Anime Inspiration**
