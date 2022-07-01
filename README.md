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

```python
(code here)
```

### Webcam
...

## Future enhancement
I will add more features to this game engine like physics engine, collision detection, augmented reality, sound effect and so on
