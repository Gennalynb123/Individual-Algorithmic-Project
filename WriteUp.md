{% include navigation.html %}

**3a)** This program, created on Scratch, codes for a space themed maze game. Upon pressing space, the rocket ship will start to follow the movement of the user’s mouse, allowing them to navigate their way through space in efforts to save an alien named Gobo, who is surrounded by a cluster of asteroids. The user will have to collect four stars within the map and make direct contact with Gobo to win. The user will not be able to save Gobo without collecting all the stars beforehand. While navigating through space, the user will have to avoid all contact with the asteroids. Any contact will result in a loss of a life, and a reset position to the start of the map. The user will be provided three lives. A win or lose screen will pop up depending on whether or not the user succeeds.


**3b)**
1st section:
(“or” statements continue to asteroid 7; photo cut off for viewing purposes)
![image](https://user-images.githubusercontent.com/89223650/161892996-b7897eff-54a3-434d-a1c3-ed0a95a7ef33.png)


Second Section:
![image](https://user-images.githubusercontent.com/89223650/161893024-7163aa6c-04b9-4fa8-9fa9-a0ec0050693c.png)

(code for asteroid)
The first section of code provided shows how the data of "Lives" is changed and updated. When the game starts, the amount of lives is set to 3 (not shown in the code segment). Whenever the rocket ship comes into contact with an asteroid, the function "Reset" is called, which resets the position of the rocket ship and updates the value of "Lives" by -1. The second section of code provided shows how the amount of lives is being tracked in order for the program to know when the user loses. Whenever the amount of lives reaches 0, the program is signaled to hide the asteroid for the losing screen. This same tracking of the amount of "lives" is used for the other sprites in the program to signal when to hide. Without a "Lives" counter, it would be difficult to sync all of my sprites together to "hide" and "show" in unison at the time I intend for. By creating "if" functions that run under the condition "Lives = 0", I am able to sync all of my sprites together and create functions that I want called specifically for, in this case, the losing screen.

**3c) **
![image](https://user-images.githubusercontent.com/89223650/161893097-1253b9ff-c6d6-4212-82d6-9dbf5ab31b70.png)


Call for Lose function if Lives = 0

The code above is from one of the asteroid sprites. The “Lose” function allows the losing screen to be shown without the asteroids being in the frame. This “Lose” function contains a forever loop which continuously checks if Lives = 0, essentially checking if the user has lost. The function will continue checking this until the condition is true. If this condition is true, then the function will signal the asteroid to hide, allowing the losing screen to be shown without the asteroid in the frame. It also stops other scripts in the sprite in order to prevent bugs and collisions within the code of that sprite. The function is called when the green flag is pressed, and it runs only if Lives = 0.

**3d)** The first call of the function “Lose” is called when the green flag is clicked. It will only be called if the variable counter lives = 0. If lives = 0, then the first part of the code will be called. The rocket ship will hide. Another call of the function “Lose” is called when the green flag is clicked, only if “stars left” is greater than 0 and the rocket ship is touching gobo. If this is true, then the second segment of the function “Lose” will be called. The function “reset” will be called, resetting the position of the rocket ship and lowering the “lives” counter by 1. This prevents the function “Lose” from being called 24/7 after the green flag is clicked, and makes it so that the function is only called when necessary.
