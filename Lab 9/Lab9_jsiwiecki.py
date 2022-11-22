# Author: Joseph Siwiecki
# Assignment: Lab 9
# Completed: 11/13/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
import random

class Question:
    score = 0
    #initializing the objects
    def __init__(self, question, correct_answer, answers = []):
        self.question = question
        self.correct_answer = correct_answer
        self.answers = answers
    def checkAns(self, userAns):
        if (userAns.lower() == self.correct_answer.lower() or userAns.upper() == self.correct_answer.lower()):
            print("\tCorrect")
            Question.score += 1
        else:
            print(f"\tIncorrect\nCorrect Answer: {self.correct_answer.upper()}")
        return Question.score

class Student:

    #initializing the objects
    def __init__(self, name, id, multipleQuizScores = []):
        self.name = name
        self.idNum = id
        self.current_quiz_score = 0
        self.highest_quiz_score = 0
        self.multipleQuizScores = multipleQuizScores

    #Find the highest quiz score in the list
    def highest(self):
        self.highest_quiz_score = max(self.multipleQuizScores)
        return self.highest_quiz_score
    
    #Find the current quiz score in the list
    def current(self):
        self.current_quiz_score = self.multipleQuizScores[-1]
        return self.current_quiz_score   

#List of Questions
questionBank = [
    Question("What is the name of the tallest mountain in the world?", "b", ["A. Mount Tenpo", "B. Mount Everest", "C. Mount Cameroon", "D. Mount Kinabalu"]),
    Question("Which continent is in all four hemispheres?", "a", ["A. Africa", "B. South America", "C. Asia", "D. Australia"]),
    Question("Which country has the largest population in the world?", "c", ["A. Russia", "B. United States", "C. China", "D. Canada"]),
    Question("What is the name of the tallest man-made building ever built?", "a", ["A. Burj Khalifa", "B. Tokyo Skytree", "C. Aerium", "D. The Palace of Parliament"]),
    Question("which of the seven continents is the largest in the world?", "a", ["A. Asia", "B. North America", "C. Europe", "D. Africa"]),
    Question("Which country is considered the world's largest island?", "b", ["A. Philippines", "B. Greenland", "C. Madagascar", "D. Sea Lion Island"]),
    Question("Which ocean is the smallest ocean in the world?", "d", ["A. Pacific Ocean", "B. Indian Ocean", "C. Antarctic Ocean", "D. Artic Ocean"]),
    Question("what is the largest volcano in the world?", "c", ["A. Taal", "B. Krakatoa", "C. Mauna Loa", "D.  Dukono"]),
    Question("What is the name of the longest river in Africa", "a", ["A. The Nile River", "B. Mississippi River", "C.Yangtze River", "D.Volga River"]),
    Question("In the United States which state is considered the largest?", "d", ["A. California", "B. Texas", "C. Mississippi", "D. Alaska"]),
    Question("Which is the largest country in the world?", "b", ["A. China", "B. Russia", "C. Canada", "D. Monaco"]),
    Question("What country are the \"Spanish Steps\" located in?", "a", ["A. Italy", "B. Spain", "C. England", "D. Austria"]),
    Question("Which ocean is the largest ocean in the world?", "c", ["A. Artic Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Antarctic Ocean"]),
    Question("Which language is the most spoken in the world?", "c", ["A. Hindi", "B. English", "C. Mandarin", "D. Spanish"]),
    Question("What country are the Great Pyramids of Giza located in?", "a", ["A. Egypt", "B. Iran", "C. United States", "D. Saudi Arabia"]),
    Question("Where are the Stonehenge's located?", "d", ["A. Scotland", "B. Ireland", "C. Iceland", "D. England"]),
    Question("What place is considered the coldest place on Earth?", "b", ["A. Alaska", "B. Antarctica", "C. Greenland", "D. Russia"]),
    Question("What is the name of the largest lake in the world?", "a", ["A. Caspian Sea", "B. Lake Victoria", "C. Lake Huron", "D. Lake Superior"]),
    Question("About 90 percent of the world's population lives in which hemisphere?", "c", ["A. Western Hemisphere", "B. Southern Hemisphere", "C. Northern Hemisphere", "D. Eastern Hemisphere"]),
    Question("Which volcano destroyed the ancient city of Pompeii?", "b", ["A. Taal", "B. Mount Vesuvius", "C. Mount Fuji", "D. Krakatoa"])
]

#List of students when they get inputted
studentList = []

print("Welcome to the Test Taking System\nPlease provide your name and Student ID to take the test")
userName = input("Name: ")
userID = int(input("Student ID: "))
firstStudent = {userName, userID}
print("Hello", userName, "! Let's get started. You will be answering 5 questions:")
count = 1
for question in random.sample(questionBank, 5):
    print("Question #" + str(count) + ":")
    print(f"\t{question.question}")
    for option in question.answers:
        print(f"\t\t{option}")
    userInput = input("\t")
    total = question.checkAns(userInput)
    count +=1

scoreList = [] 
testScore = total / 5 * 100
print(f"Score: {testScore}%")
scoreList.append(testScore)

tempStudentInfo = Student(userName, userID, scoreList)
studentList.append(tempStudentInfo)

for student in studentList:
    print(f"\tName: {student.name}")
    print(f"\tID: {student.idNum}")
    print(f"\tCurrent: {student.current()}")
    print(f"\tHighest: {student.highest()}\n")