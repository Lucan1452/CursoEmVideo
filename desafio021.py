# Tocando música no python
from pygame import *
mixer.init()
mixer.music.load('desafio021a.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.Clock().tick(10)