#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. 
#Write the collected data to a text file. Ask another question until the user chose to exit.

#set filename to save the quiz data
#display welcome message
#begin an infinite loop that asks the user for questions and choices
#ask the user for correct answer

#open the file in append mode to save the questions and choices
#ask the user if they want to add a question
#if yes, continue asking questions
#if no, end the program
#display goodbye message

filename = "quiz_data.txt"

print("/nWelcome to the Quiz Creator!")

while True:
  print("/nEnter your quiz questions and choices:")

question = input("Question: ")
choice_a = input("A.) ")
choice_b = input("B.) ")
choice_c = input("C.) ")
choice_d = input("D.) ")
