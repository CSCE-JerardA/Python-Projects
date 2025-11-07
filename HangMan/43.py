#*******************************************************************
# Course:      CSCI 201
#Assignment: Classwork 04-26-2024
# Programmer: Jerard Austin
# Instructor: Dr. Mirek Mystkowski
# Date: April 26th 2024
# Synopsis: This program displays a window from tkinter that displays a game of hangman.
# Test case 1:
# input: 
# expected output: 
# actual output: 
# Test case 2:
# input:
# expected output:
# actual output:
# Test case 3:
# …………….
#*******************************************************************

import tkinter as tk
import random
from string import ascii_uppercase
from tkinter import messagebox


class HangManGame(object):
    def __init__(self, root, fileName):
        # create a word list based on a file
        self.wordList = self.readFile()
        self.secretWord = random.choice(self.wordList).upper()
        self.guess_left = 10
        self.letter_used = ""
        self.guessed_word = "_" * len(self.secretWord)
        self.tLabel = tk.Label(master= root, text="Hangman", height=3)
        self.tLabel.grid(row=0, column=0,columnspan=13, sticky="news")
        self.drawPlane = tk.Canvas(master= root, width=100, height=200)
        self.drawPlane.grid(row = 1, rowspan=3)
        self.gLabel = tk.Label(master=root, text= "Guesses left: " + str(self.guess_left), height=3)
        self.gLabel.grid(row=1, column=7,columnspan=6, sticky="news")
        self.letterLabel = tk.Label(master=root, text=" letters used: " + self.letter_used, height=3)
        self.letterLabel.grid(row=2, column=7,columnspan=6, sticky="news")

        self.wLabel = tk.Label(master=root, text= " ".join(self.guessed_word), height=3)
        self.wLabel.grid(row = 3, column = 7, columnspan = 6, sticky = "news")
        self.buttonList = []
        for n,letter in enumerate(ascii_uppercase):
            b = tk.Button(master=root, text=letter, command=lambda x = letter: self.process_click(x))
            b.grid(row= 4+n//13, column= n%13)
            self.buttonList.append(b)
    def process_click(self, letter):
        self.buttonList[ord(letter) - ord('A')]["state"] = tk.DISABLED
        self.letter_used += letter
        self.letterLabel["text"] = "letters used: " + self.letter_used
        if letter not in self.secretWord:
            self.guess_left -= 1
            self.drawHangman()
        self.gLabel["text"] = "guesses left: " + str(self.guess_left)
        for index, item in enumerate(self.secretWord):
            if item == letter:
                self.guessed_word = self.guessed_word[:index] + letter + self.guessed_word[index +1:]

        self.wLabel["text"] = " ".join(list(self.guessed_word))

        if self.guessed_word.count("_") == 0:
            for b in self.buttonList:
                b["state"] = tk.DISABLED
            tk.messagebox.showinfo("Hangman","Congratulations!, You won! :) ")

        elif self.guess_left == 0:
            for b in self.buttonList:
                b["state"] = tk.DISABLED
            tk.messagebox.showinfo("Hangman", "Sorry! You lost! :( ")

    def drawHangman(self):
        if self.guess_left <= 9:
            self.drawPlane.create_line(10,10,10,190)
        if self.guess_left <= 8:
            self.drawPlane.create_line(10,10,70,10)
        if self.guess_left <= 7:
            self.drawPlane.create_line(70,10,70, 30)
        if self.guess_left <= 6:
            self.drawPlane.create_oval(60, 30, 80, 50)
        if self.guess_left <= 5:
            self.drawPlane.create_line(70,50, 70, 100)
        if self.guess_left <= 4:
            self.drawPlane.create_line(70,60,60,80)
        if self.guess_left <= 3:
            self.drawPlane.create_line(70,60,80,80)
        if self.guess_left <= 2:
            self.drawPlane.create_line(70,100,60,120)
        if self.guess_left <= 1:
            self.drawPlane.create_line(70,100,80,120)
        if self.guess_left <= 0:
            self.drawPlane.create_line(67,45,72,45)
            self.drawPlane.create_oval(61,33,65,37)
            self.drawPlane.create_oval(75, 33, 79,37)



    def readFile(self):
        return ["python", "javascript"]



window = tk.Tk()
game =HangManGame(window, "wordlist.txt")
window.mainloop()
