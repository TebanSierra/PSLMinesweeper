#!/usr/bin/python3
'''
@Author: Esteban Sierra Munera
@PersonalEmail: esteban.sierram@gmail.com
@CollegeEmail: esierra5@eafit.edu.co
@CollegeEmail2: esierra@purdue.edu
@LasUpdate: August 27th, 2018

Main script for minesweeper game for PSL
Internship Programming Challenge
'''
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