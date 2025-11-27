# Catch the Balls Game

![Catch the Balls]() 
<img width="1280" height="832" alt="Screenshot 2025-11-27 at 4 00 04 PM" src="https://github.com/user-attachments/assets/68273c4b-bf68-4f13-b452-d5bf61706d9c" />
<img width="563" height="452" alt="Screenshot 2025-11-27 at 4 00 27 PM" src="https://github.com/user-attachments/assets/96d4257f-69c8-4595-9c0c-cba63326d1ae" />
<img width="1280" height="804" alt="Screenshot 2025-11-27 at 4 00 40 PM" src="https://github.com/user-attachments/assets/234e5627-3097-422e-b6d3-458ec6fb4618" />

## Purpose of the Project
The purpose of this project was to study how interactive graphical applications are built using Python’s **Tkinter** library. The main goals were:

- Understand **user-event handling** and real-time animations.
- Implement **object movement** and **collision detection**.
- Manage **GUI state** and game logic.
- Explore **loops, timers, and canvas-based graphics** for game development.

This project demonstrates how a simple arcade game can be designed and enhanced in Python.

---

## Data Collected
During development and testing, the following gameplay metrics and behavior patterns were observed:

- Ball fall speed trends  
- Player reaction time (basket movement responsiveness)  
- Score patterns (average balls caught per session)  
- Collision detection accuracy  
- Lag or frame drops during fast movement  
- User interaction responses via arrow keys  

This data was used to improve:

- Difficulty balance  
- Ball spawning speed  
- Basket movement sensitivity  
- Overall gameplay smoothness and fairness  

---

## Data Description

The game generates **runtime data dynamically**. No external datasets are used. Key data tracked:

### 1. Game State Data
| Variable       | Type    | Description                                  |
|----------------|--------|----------------------------------------------|
| `score`        | Integer | Number of balls successfully caught         |
| `time_left`    | Integer | Countdown timer (seconds)                   |
| `game_running` | Boolean | Game status: active, paused, or finished   |

### 2. Ball Data
- Randomly generated in memory  
- Each ball has:
  - Canvas object ID  
  - Random X-position  
  - Fixed size (30px diameter)  
  - Random color  
  - Constant downward velocity  

Tracked via: `self.ball`

### 3. Player (Basket) Data
- Represented as a **canvas rectangle**  
- Movement controlled by left/right arrow keys  
- Updated position stored internally by Tkinter

### 4. Event-Generated Data
- Collision detection values  
- Ball positions  
- Basket position  
- Number of balls caught or missed  
- Whether a ball hits the basket or not  

### 5. Data Creation Process
- `spawn_ball()` creates new ball objects with random attributes  
- `update_ball()` moves balls, detects collisions, and removes them  
- Timer events handled via `after()`  
- Score and game status updated in real-time  

---

## How to Use

### 1. Download or Clone
git clone https://github.com/veerj0808/catchTheBalls.git

Or download the ZIP and extract.

2. Install Requirements
	•	Python 3.8 or above
	•	Tkinter (usually included in Python installation)
No external libraries required.

3. Run the Game
python catch_ball_game.py

4. Gameplay Instructions
	•	Use LEFT ← and RIGHT → arrow keys to move the basket
	•	Catch falling balls to score points
	•	Avoid missing too many balls
	•	Game duration: 20 seconds
	•	Use Pause/Resume button to control gameplay
	•	After time runs out, final score is displayed with a replay option

⸻

Contact Information
	•	Name: Veer Jain
	•	Email: veerj0808@gmail.com
	•	GitHub: https://github.com/veerj0808￼

Feel free to contact for:
	•	Bug reports
	•	Game improvements
	•	Feature requests
	•	Collaboration opportunities

⸻

License

This project is released under the MIT License:
	•	Use for personal, academic, or commercial projects
	•	Modify or expand the game
	•	Distribute your version

Requirements:
	•	Include original copyright notice
	•	Include MIT License in redistributed versions

For full legal details, see the included LICENSE file.

⸻

Notes
	•	Simple Python-Tkinter arcade game for learning and demonstration
	•	Graphics generated using basic Tkinter shapes (no external images)
	•	Optimized to run smoothly on most systems
	•	Customizable:
	•	Game speed
	•	Ball colors
	•	Basket size
	•	Timer duration
	•	Difficulty level (spawn rate, movement speed)
	•	Code is clean and modular for easy modification and experimentation

Feedback, improvements, and pull requests are welcome!
