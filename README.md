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
import os, sys

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

#### Life Cycle
The game engine will call function in scene based on the life cycle. So just put your code in the appropriate and you can construct you screen with interaction. Here is the situation and when those functions will be called:
1) call setup() once when object created
2) when entering the scene, call reset()
3) call update() for each frame (so you can change elements for each frame)
4) call afterRender() when frame rendering finished
5) call keyInToggle() when key press detected
6) call timeoutCallback() when define event expired

## Elements
For each game scene, there are elements. Actually, you already know them in the code above. like:

```python
self.elements["KEY_FUNCTION"] = {"type":"text", "message":"Home: Press 'p' to play", "x":30, "y":690, "font":cv2.FONT_HERSHEY_TRIPLEX, "size":1, "color":(255, 255, 255), "thickness":2}
```

You have to give a unique name for each element in each scene. If you need to update the element, you need this unique name to refer to the element. In the example above, "KEY_FUNCTION" is the unique name. 

The game engine support several types of elements: 

### text
Text is simple. You need to add your element with "type":"text". Parameters is as follows:
```
message: Text content of the element (e.g. Home: Press 'p' to play)
x: coordination of x
y: coordination of y
font: font type (please check with opencv)
size: font size
color: font color (format: (r,g,b)
thickness: font thickness 
animate: shake|jump 
```

### jpg

You can try to add this line as first line of setup() in HomeScene: (Certainly, you need to create folder and add file to the directory)
```python
self.elements["BG"] = {"type":"jpg", "file":"./assets/images/intro_bg.jpg", "x":0, "y":0, "w":1280, "h":720}
```
And now you have a beautiful background in you home screen. 

### png
```
self.elements["WIN_MARBLE_U1"] = { "type":"png","file":"./assets/images/marble.png", "x":10, "y":140, "w":80, "h":80}
```

### line
```
self.elements["LINE1"] = { "type":"line",  "x":100, "y":40, "x2":100, "y2":200, "color": (0, 0, 0), "thickness":3 }
```

### box
```
self.elements["O1_BOX"] = { "type":"box", "x":75, "y":20, "w":340, "h":520, "color": (0, 200, 0), "thickness":3 }
```

### rect 
```
self.elements["BOX_YNAME_BG"] = { "type":"rect", "x":100, "y":50, "x2":300, "y2":100, "color":(50,50,50) }
```

### mimage
Sometime you will create some image on your game. And if you need to show in the game scene, you can use mimage. Example here:
```
hand = cv2.resize(hand, (160,160), interpolation = cv2.INTER_AREA)	# hand is part of the webcam captured picture
self.elements["GESTURE"] = { "type":"mimage",  "x":1100, "y":550, "fimg":hand, "timg":self.stage.frame }
```

As a camara game engine, some element is for the captured video stream or still picture:

### pip
To show your capture video stream to somewhere of your screen, you can use this
```
self.elements["PIP"] = {"type":"pip", "x":100, "y":100, "w":480, "h":320}
```

### snapshot
During the game playing, you can save the webcam video stream at a moment to create a snapshot.  
```
self.stage.takeSnapshot()
```

And then you can display the snapshot to the screen:
```
self.elements["PIP_SNAPSHOT"] = { "type":"snapshot", "x":100, "y":100, "w":480, "h":320 }
```


## Future enhancement
I will add more features to this game engine like physics engine, collision detection, augmented reality, sound effect and so on
