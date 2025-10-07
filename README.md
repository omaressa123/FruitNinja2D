# 🍉 Fruit Ninja 2D

A **2D Fruit Slicing Game** built with **Python** and **Pygame** inspired by the popular *Fruit Ninja*.  
The player slices flying fruits with the mouse while avoiding bombs.  
Each sliced fruit gives points — but slicing a bomb ends the game! 💣  

---

## 🎮 Game Overview

**Objective:**  
Slice as many fruits as possible to achieve a high score without hitting bombs or missing too many fruits.

**Gameplay:**  
- Fruits and bombs fly up from the bottom of the screen at random speeds and angles.  
- You “slice” fruits by moving the mouse cursor quickly over them.  
- Slicing a fruit gives +10 points.  
- Missing fruits costs a life.  
- Hitting a bomb ends the game immediately.  

---

## 🧩 Folder Structure

```bash
FruitNinja2D/
│
├── main.py               # Main game loop, initializes and runs everything
├── fruit.py              # Fruit class: movement, physics, slicing detection
├── bomb.py               # Bomb class: explosion logic and animation
├── effects.py            # Handles slicing effects, sound, and particles
│
├── assets/
│   ├── images/
│   │   ├── apple.png
│   │   ├── banana.png
│   │   ├── bomb.png
│   │   └── background.jpg
│   │
│   ├── sounds/
│   │   ├── slice.wav
│   │   ├── bomb.wav
│   │   └── bg_music.mp3
│
└── README.md

pip install pygame

to Run
python main.py



┌───────────────────────┐
│   Start Game          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Spawn Fruit/Bomb      │
│ (random speed & pos)  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Player moves mouse    │
│ → Detect swipe path   │
└───────────┬───────────┘
            │
     ┌──────┴──────────┐
     │ Slice detected? │
     └──────┬──────────┘
            │Yes
            ▼
┌───────────────────────┐
│ Play slice sound      │
│ + Add score           │
│ + Juice particles     │
└───────────┬───────────┘
            │No
            ▼
┌───────────────────────┐
│ Fruit falls uncut     │
│ -1 Life               │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Bomb hit?             │
│ → Game Over           │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Display final score   │
│ Restart or Quit       │
└───────────────────────┘
🎧 Sounds and Visuals

Slice Effect: slice.wav

Explosion: bomb.wav

Background Music: bg_music.mp3

Juice Animation: Triggered on slice

Background: Wooden board (background.jpg)

🧠 Features

✅ Random fruit & bomb spawning
✅ Gravity physics simulation
✅ Swipe detection with mouse
✅ Sound & particle effects
✅ Score & life display
✅ Game over & restart system

🧾 Future Enhancements

Combo detection system

Power-ups (slow motion, double points)

Difficulty levels

Leaderboard (save best scores)

Animated fruit halves after slicing

🧠 Learning Outcomes

Applying 2D game physics (gravity, velocity).

Handling mouse input and collision detection.

Managing sprites, images, and sound effects.

Designing real-time game loops with frame rate control.

💡 Credits

Developed using Python + Pygame
Inspired by the original Fruit Ninja by Halfbrick Studios.
