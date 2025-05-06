#Reset the Quiz Data for Quiz Creator and Quiz App
#It removes all the questions 

filename = "quiz_data.txt"

with open(filename, "w") as file:
    pass  # This will empty the file

print("🧹 Quiz data has been reset! 'quiz_data.txt' is now empty.")
