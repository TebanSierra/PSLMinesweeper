#!/usr/bin/python3
import gameplay as gp


h, w, m = input("Insert Height, Width an Number of mines: ").split()
game = gp.GamePlay(int(h), int(w), int(m))

game.printBoard()

while(game.isPlaying()):
    game.play()
    game.printBoard()

