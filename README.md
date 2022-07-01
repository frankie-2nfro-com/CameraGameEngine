# CameraGameEngine
A simple webcam game engine developed in a [AiCore project](https://github.com/frankie-2nfro-com/ComputerVisionRockPaperScissors). And this repository is extracting the generic game engine into a separate project. 

## How to use
Clone this repository in the same level of your game repository. For example, your game directory is in /games/mygame1:
```
cd /games
git clone https://github.com/frankie-2nfro-com/CameraGameEngine.git
```

Install opencv packages in your environment (recommend create a seperate conda environment):
```
pip install opencv_contrib_python
```

Then, you can start coding. 

## Sample Code

### Start up
To test your environment and setup, you can create a python file e.g. main.py with the following code:
```python
import os, sys

game_engine_path = os.path.abspath('../CameraGameEngine')
sys.path.insert(1, game_engine_path)
from camera_game_engine import CameraGameEngine

class DemoGame(CameraGameEngine):
	def setup(self):
		print("Game start.....")

if __name__ == '__main__':
	DemoGame('Demo Game')
```
Run your program and you should see a new window pop up with a still capture of your webcam. Good luck! 

If you cannot see this result, just check if the computer webcam work properly or try to change your camera id in this line:

```python
if __name__ == '__main__':
	DemoGame('Demo Game', 1)    # specify your proper webcam id by second parameter
```

Or you can refer to my [Demo Game Sample](https://github.com/frankie-2nfro-com/DemoGame).

### Game Scene
GameScene class is screen of the game, you can create different screen of you game and jump to and fro as you game design. The class simply provides skeleton life cycle template to your child classes. Let's create a simple story board as (Home) -> (Playing) -> (GameOver).

#### HomeScene (create a python file as home_scene.py)

```python
from camera_game_engine import GameScene
import cv2

class HomeScene(GameScene):
	def setup(self):
		self.elements["KEY_FUNCTION"] = {"type":"text", "message":"Home: Press 'p' to play", "x":30, "y":690, "font":cv2.FONT_HERSHEY_TRIPLEX, "size":1, "color":(255, 255, 255), "thickness":2}
			
	def reset(self):
		self.stage.setCapture(False) 

	def keyInToggle(self, key):
		if key & 0xFF == ord('p'):
			self.stage.jumpScene("PLAYING")
		elif key & 0xFF == ord('q'):			
			self.stage.quit()
```

#### PlayingScene (create a python file as playing_scene.py)

```python
from camera_game_engine import GameScene
import cv2

class PlayingScene(GameScene):
	def setup(self):
		self.elements["KEY_FUNCTION"] = {"type":"text", "message":"Press 'p' to finish", "x":30, "y":690, "font":cv2.FONT_HERSHEY_TRIPLEX, "size":1, "color":(255, 255, 255), "thickness":2}
			
	def reset(self):
		self.stage.setCapture(True) 

	def keyInToggle(self, key):
		if key & 0xFF == ord('p'):
			self.stage.jumpScene("GAMEOVER")
```

#### GameoverScene (create a python file as gameover_scene.py)

```python
from camera_game_engine import GameScene
import cv2

class GameoverScene(GameScene):
	def setup(self):
		self.elements["KEY_FUNCTION"] = {"type":"text", "message":"Game Over: Press 'p' to play again", "x":30, "y":690, "font":cv2.FONT_HERSHEY_TRIPLEX, "size":1, "color":(255, 255, 255), "thickness":2}
			
	def reset(self):
		self.stage.setCapture(False) 

	def keyInToggle(self, key):
		if key & 0xFF == ord('p'):
			self.stage.jumpScene("HOME")
```

#### Update the main program

```python
game_engine_path = os.path.abspath('../CameraGameEngine')
sys.path.insert(1, game_engine_path)
from camera_game_engine import CameraGameEngine

from home_scene import HomeScene
from playing_scene import PlayingScene
from gameover_scene import GameoverScene

class DemoGame(CameraGameEngine):
	def setup(self):
		self.registerScene("HOME", HomeScene(self))
		self.registerScene("PLAYING", PlayingScene(self))
		self.registerScene("GAMEOVER", GameoverScene(self))
		self.initScene("HOME")

if __name__ == '__main__':
	DemoGame('Demo Game', 1)
```

And now you create a game layout with home scene, playing scene and game over scene. The code is pretty simple. Just run and have a look.

## Elements
(to be added)

## Future enhancement
I will add more features to this game engine like physics engine, collision detection, augmented reality, sound effect and so on
