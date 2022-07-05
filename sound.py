import multiprocessing
from threading import Thread
from playsound import playsound

def playBackgroundMusicByThread(file):
	play_thread = multiprocessing.Process(target=playBackgroundMusic, args=[file])
	play_thread.start()
	return play_thread

def playBackgroundMusic(file):
    while True:
        playsound(file)

def playFxMusicByThread(file):
	play_thread = Thread(target=playFxMusic, args=[file])
	play_thread.start()
	return play_thread

def playFxMusic(file):
    playsound(file)