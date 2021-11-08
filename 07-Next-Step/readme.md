# Next Steps

Now that the game is mostly working it's time to consider what happens next. As it is this game is really the prototyp for a game. It shows a working concept but it is not a complete game. A complete game has objectives, a story and concept, goals, and rewards. Besides these there are also many improvements that can be made to the existing elements. 

Take a few minutes and think about a concept and story line that would add interest to the exsiting game concept. I need you to bring your ideas to this project. In a job situation your team will want you you to share your ideas. 

## Challenges 

**Challenge 1** 

Set the background. Pygame doesn't seem to have a tiling image fill. You can use an image that fills the screen, or use a background color to fill the background. 

**Challenge 2**

The background is very static and has no life. We need some elements in the background that can add some life and build the environment. You can take this where your concept might want to go. 

I'm going to present the idea of having some clouds floating by in the background. Clouds are Sprites and can be animated in the `all_sprites` group. 

Create a new `Cloud` class. This class can extend `GameObject` or `Sprite`. It should display a cloud image (there are three cloud images in the images folder). Clouds should move slowly left to right. When they get off the right side of the screen they should choose a random image and set their y position to random value and x to -64. From here they continue moving across the screen. 

**Challenge 3** 

The game is growing size. The code base has grown in size. Moving forward it would be good to start dividing the code into modules. A module is a file containing python code. You can import variables, and classes from one module into another. 

```python
# constants.py
lanes = [93, 218, 343]
...

# gameobject.py
import pygame
class GameObject(class GameObject(pygame.sprite.Sprite):
	...

# main.py
import pygame
from gameobject import GameObject
...
```

Use this idea to break your code into a files. Create a `main.py` file that is your main game. It should initialize pygame, create the main window, and define the game loop. It should also import and create the game objects. 

For each of the classes that make up your game create a separate file. 

- GameObject
- Apple
- Strawberry
- Bomb
- Player
- Cloud

Create another file for constants. These are variables and values shared by the other modules. Put values in here like `lanes` and `SCREEN_WIDTH` and `SCREEN_HEIGHT`. 

### Stretch Goals

**Challenge 4**

Add some sound. Games need sound. Pygame supports sound. Add some background sound: https://www.pygame.org/docs/ref/music.html

**Challege 5** 

Add some sound effects. We need a sound when the player picks up a fruit. 

https://pythonprogramming.net/adding-sounds-music-pygame/

**Challenge 6**

Currently there is no score keeping. Keep track of a score and display it using: https://www.pygame.org/docs/ref/font.html

**Challenge 7**

As it is the game quits when the player is hit by a bomb. Reset the game instead. All objects should return their strting positions and the score should be reset to 0. Consider player a sound when the game ends. 

**Challenge 8**

Our sprites are very static. By cycling through a series of images you can create an animated sprite. Take a look at the images in the folder here. 

Your goal is to create a new class that can display a series of images in sequence. Take a clue from these: 

- Animated Sprites or Spriteheet
	- https://inventwithpython.com/pyganim/
	- https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
	- https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
	- https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/
