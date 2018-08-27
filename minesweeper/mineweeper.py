#!/usr/bin/python3
import gameplay as gp

canPlay = False

while(not canPlay):
    try:
        h, w, m = input("Insert Height, Width an Number of mines: ").split()
        canPlay = True
    except ValueError:
        print("Enter all the data.")

game = gp.GamePlay(int(h), int(w), int(m))
game.printBoard()

while(game.isPlaying()):
    msg = game.play()
    game.printBoard()

print(msg)