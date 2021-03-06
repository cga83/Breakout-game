# Breakout game using Python
## Introduction 
### What is this game ?
This is my version of the famous breakout game. There are different bricks that you have to destroy with a Ball. Your goal is not to lose the Ball by moving the Platform.
You can move the Platform using the right arrow and left arrow of your keyboard. But first, to start the game, you have to click on the "Enter" key of your keyboard.

Here, on the following picture, you can see how the environment of the game looks like. It is written on the screen, in French:
> Press the "Enter" key of your keyboard to start the game.
![Alt text](breakoutgame.png?raw=true "How the environment of the game looks like")

When you start the game, you have three lives. When you lose the Ball, you also lose one life.
Your score increments each time you break a Brick.

Here, on the following picture, you can what happens when you miss the Ball. The number of lives decrease. It is written on the screen, in French:
> You have one remaining life. Press the "Enter" key of your keyboard to start the game.
![Alt text](breakoutgame1.png?raw=true "How the environment of the game looks like")



### The code
This code was written in Python. There is a graphic interface which was done using the library tkinter.

#### The classes
The code is divided into four classes:
- the Ball class,
- the Border class,
- the Platform,
- the Brick.

Each class has different methods.

1. Ball Class:
- Initialization : the ball is created
- Move : the ball moves to its new coordinates

2. Class Border:
- Initialization : the border is created
- BallPosition : if the ball touches one border, it changes its direction

3. Platform Class:
- Initialization: the platform is created
- Move: the plaform moves to its new position or stays where it is if the new position is outside the border
- BallPosition: if the ball touches the platform, it changes its direction

4. Brick Class:
- Initialization: the bricks are created
- Show: if the ball has already touch a brick, this brick should be hidden. Otherwise, it should appear.
- BallPosition: if the ball touches a brick, the brick should be hidden and the score should be incremented.


### To-do list
- Add a "High Score" button. When you click on this button, you have access to the three highest score (and the names of the players who got these scores).
