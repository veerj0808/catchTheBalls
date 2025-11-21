THE CATCH BALL GAME


1. Purpose Behind the Research 
Purpose of the Research:
The purpose of this project was to study how interactive graphical applications are built using Python’s Tkinter library. The aim was to understand user-event handling, real-time animations, object movement, collision detection, and GUI state management. The research focused on exploring how simple games can be designed using loops, timers, and canvas-based objects.

2. Data Collected 
During development and testing, various gameplay metrics and behavior patterns were observed, including:
Ball fall speed trends
Player reaction time (how quickly the basket moves)
Score patterns (average balls caught in the given time)
Collision detection accuracy
Lag or frame-drop points during fast movement
User interaction responses (keyboard arrow controls)

This data helped improve:
Difficulty balance
Ball spawning speed
Basket movement sensitivity
Overall gameplay smoothness and fairness

Data Description
This project does not use external datasets, but it generates its own runtime data during gameplay. The data is created dynamically by the game logic and is used to update visuals, scoring, and time tracking. Below is a detailed breakdown of the data involved:
1. Game State Data
These values are stored internally in variables and updated throughout the game:

Variable
Type
Description
score
Integer
Tracks how many balls the player has successfully caught.
time_left
Integer
Countdown timer showing remaining game duration (in seconds).
game_running
Boolean
Indicates whether the game is active, paused, or finished

2. Ball Data
Balls are not stored in a file; they are generated randomly and tracked in memory.
Each ball is represented by:
A canvas object ID
Random X-position
Fixed size (30px diameter)
Random color
Constant downward velocity

These are stored in:
self.ball
3. Player (Basket) Data
The basket is represented by:
Canvas rectangle coordinates
Movement controlled by left/right arrow keys
Updated position stored internally by Tkinter

4. Event-Generated Data
During the game, the following data is continuously generated and updated:
Collision detection values
Ball positions
Basket position
Number of removed/caught balls
Whether a ball hit the basket or missed

5. Data Creation Process
All data is created programmatically within the script:
The spawn_ball() function creates new ball objects with random attributes.


The update_ball() function updates movement, detects collisions, and removes balls.
Timer data is generated using after() events.
Score and game status are updated in real time and displayed on-screen.

How to Use

Follow these steps to install, run, and use the Catch the Balls game:
1. Download or Clone the Repository
   
git clone https://github.com/veerj0808/catchTheBalls.git
Or download the ZIP file and extract it.

2. Install Requirements
   
This game uses Python’s built-in Tkinter library, so no external packages are required.
Make sure you have:
Python 3.8 or above
Tkinter installed (included by default in most Python installations)

3. Run the Game
   
Navigate to your project folder and run:
python catch_ball_game.py

4. Gameplay Instructions
   
Use LEFT ← and RIGHT → arrow keys to move the basket.
Catch the falling balls to score points.
Avoid missing too many balls.
You have 20 seconds to score as high as possible.
Use Pause/Resume button to control gameplay.
After time runs out, the final score will appear with a replay option.

Contact Information

If you have questions, suggestions, or want to collaborate, feel free to reach out:
Name: Veer Jain
 Email: veerj0808@gmail.com
 GitHub: https://github.com/veerj0808
 Contact Purpose: Bug reports, game improvements, feature requests, or general queries.

License

This project is released under the MIT License, which allows users to freely use, modify, distribute, and share the code as long as proper credit is given to the original author.
You are free to:
 Use the code for personal, academic, or commercial projects
 Modify or expand the game
 Distribute your version
 
You must:

 Include the original copyright notice
 Include the MIT License in any redistributed version
For full legal details, see the included LICENSE file.

Notes

This project is a simple Python–Tkinter–based arcade game developed for learning and demonstration purposes.
All graphics (balls, basket, canvas) are generated using basic Tkinter shapes—no external images or assets are used.
The game is optimized to run smoothly on most systems without additional dependencies.
You can customize:

Game speed
Ball colors
Basket size
Timer duration
Difficulty level (spawn rate, movement speed)
The code is intentionally written in a clean and modular way, making it easy for students to modify for college projects or further research.

Feedback, improvements, and pull requests are welcome!



