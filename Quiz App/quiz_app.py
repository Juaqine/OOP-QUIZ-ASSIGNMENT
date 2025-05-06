#Create the Quiz program that read the output file of the Quiz Creator.
#The user will answer the randomly selected question and check if the answer is correct.

#Import the necessary modules for GUI (tkinter), message boxes, and random choice
#Define the colors used in the app (MAROON, GOLD, YELLOW, WHITE)
#Function to read and prepare quiz questions from a text file
    #Try to open the file and read its content
    #Split the content into question blocks using a delimiter
    #Go through each question block:
        #Skip it if it doesn’t contain a question
        #For each line, extract the question, choices (A–D), and the correct answer
        #Store these in a dictionary and add it to the list
    #Return the final list of formatted questions

#Create the main quiz app using a class
    #Set up the main window (title, size, background color)
    #Add a label to display the current question
    #Create four buttons for answer choices (A to D)
        #Each button checks the selected answer when clicked
    # how the first question as soon as the app starts
    #Function to load and display the current question:
        #If all questions are finished, show the end screen
        #Otherwise, show the question and update the buttons with choices
    #Function to check the selected answer:
        #If correct, increase score and show a message
        #If incorrect, show the correct answer
        #Move to the next question

#Create the end screen using a class
    #Clear the window and set a thank-you message
    #Display the final score
    #Add a button to quit the app
    #Add a button to restart the quiz by reloading questions

#Create the title screen using a class
    #Set up the window title, size, and background
    #Show the quiz title
    #Add a start button to load the questions and begin the quiz

#When the script is run directly:
    #Create the root window
    #Show the title screen
    #Start the main GUI event loop

import tkinter as tk
from tkinter import messagebox
import random

MAROON, GOLD, YELLOW, WHITE = "#800000", "#D4AF37", "#FFD700", "#FFFFFF"
CHOICES = ["A", "B", "C", "D"]

def load_questions(filename):
    try:
        with open(filename, "r") as f:
            raw = f.read().strip().split("=== QUESTION START ===")
    except FileNotFoundError:
        return []

    questions = []
    for block in raw:
        if "Q:" not in block:
            continue
        data = {}
        for line in block.strip().splitlines():
            if line.startswith(("Q:", "A:", "B:", "C:", "D:", "ANSWER:")):
                key, value = line.split(": ", 1)
                data["question" if key == "Q" else key.lower()] = value.strip().upper() if key == "ANSWER" else value.strip()

 
        choices = [(ch, data[ch.lower()]) for ch in CHOICES]
        random.shuffle(choices)

        new_data = {"question": data["question"]}
        correct_text = data[data["answer"].lower()]
        for i, (label, text) in enumerate(choices):
            new_label = CHOICES[i]
            new_data[new_label.lower()] = text
            if text == correct_text:
                new_data["answer"] = new_label

        questions.append(new_data)

    random.shuffle(questions)
    return questions

class QuizApp:
    def __init__(self, root, questions):
        self.root, self.questions = root, questions
        self.score = self.current = 0
        self.total = len(questions)
