# Next Steps

Now that the game is mostly working it's time to consider what happens next. As it is this game is really the prototyp for a game. It shows a working concept but it is not a complete game. A complete game has objectives, a story and concept, goals, and rewards. Besides these there are also many improvements that can be made to the existing elements. 

Take a few minutes and think about a concept and story line that would add interest to the exsiting game concept. I need you to bring your ideas to this project. In a job situation your team will want you you to share your ideas. 

## Challenges 

This game was roughly based on the game Smove by Simple Machine. They seem to be out of business but the game is still on the App Store: https://apps.apple.com/in/app/smove/id968818637. You can read a review of the game here: https://www.tapsmart.com/games/review-smove/. Here is a video showing game play: https://www.pinterest.co.uk/pin/346143921336777890/ Smove. 

In this game the player avoids all obstacles and tries to pickup "prizes" that appear periodically in one of the 9 intersections.

YOu can implement your own ideas or try and implement these ideas in your version of the game.

**Challenge 0**

Make the game your own. I need to see your ideas! think about what you can do to make the game more unique and interesting. This can be done in a few areas. 

- Change the art. Look for some new art changing the characters can change the whole feel and dynamic. Do you think our audience would respond more to an anime theme? Pokemon? or something more abstract? 
- Change the size of the screen. Currently the screen is 500 by 500. This is was an arbitrary decision. Mobile games are popular. How would the game play at 375 x 667 (iPhone8 dimensions)

Here are some resources you can explore: 

- Images
	- https://opengameart.org
	- https://itch.io/game-assets/free
	- https://craftpix.net/freebies/
- Audio
	- https://mixkit.co/free-sound-effects/game/
	- https://freesound.org
	- [https://artlist.io/sfx/](https://artlist.io/sfx/?utm_source=google&utm_medium=cpc&utm_campaign=13681196073&utm_content=130971734784&utm_term=royalty%20free%20game%20sounds&keyword=royalty%20free%20game%20sounds&ad=530253732404&matchtype=p&device=c&gclid=Cj0KCQiAsqOMBhDFARIsAFBTN3fcskuJ5VhnLC6ioG15zYNgkc15Iw0xZhRmLy1ysSF39yuyEJh5TpwaAuBoEALw_wcB)
	- 


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

Our sprites are very static. By cycling through a series of images you can create an animated sprite. Take a look at the images in the folder here:

- [bomb](../solutions/example-7/images/bomb)
- [pink](../solutions/example-7/images/pink)
- [alien](../solutions/example-7/images/alien)

Your goal is to create a new class that can display a series of images in sequence. Take a clue from these: 

- Animated Sprites or Spriteheet
	- https://inventwithpython.com/pyganim/
	- https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
	- https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
	- https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/

Note! The term spritehseet refers to a single image containing all of the "frames" of animation usually arranged in a grid. I have spritesheets for the are used here ask me an I'll privcide them. Also, you can find spritesheets searching the web. It's a common technology used for games. 