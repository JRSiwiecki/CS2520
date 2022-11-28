# Author: Joseph Siwiecki
# Assignment: Project 4
# Completed: 11/28/2022
# Class: CS 2520.01

# --------------------- TASK 1 ---------------------
import random

class Student:
    #instance variables
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.current_quiz_score = 0
        self.highest_quiz_score = 0
        self.test_count = 0
        

    #gets the current and highest quiz score from the Test class
    def take_test(self, test):
        self.current_quiz_score = test.take_test()
        if self.current_quiz_score > self.highest_quiz_score:   
            self.highest_quiz_score = self.current_quiz_score
        
        self.test_count += 1
    
    def display_individual_stats(self):
        print(" --- TEST STATS --- ")
        print("Student Name:", self.name)
        print("Student ID:", self.id)
        print("Student's Highest Score:", self.highest_quiz_score)
        print("Student's Test Count:", self.test_count)
        print(" ------------------ ")
        
class Question:
    #instance variables
    def __init__(self, question, correct_answer, answers):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

    #returns the checked answer from the test class
    def check_answer(self, guess):
        return guess == self.correct_answer

class Test:
    #indexes for the choices when displayed and the user answer in letter choice
    alpha_index_lookup = {"a":0, "b":1, "c":2, "d":3}
    index_alpha_lookup = {0:"A", 1:"B", 2:"C", 3:"D"}

    #instance variables
    def __init__(self, questions):
        self.score = 0
        self.max_score = len(questions)
        self.questions = questions

    #Displays the questions and multiple choices
    def display_question(self, index):
        try:
            q = self.questions[index]
        except:
            print("Could got grab question")
            return
        else:
            print(str(index+1)+". " + q.question)
            for i in range(len(q.answers)):
                print("\t" + Test.index_alpha_lookup[i] + ". " + q.answers[i])

    #gets the user answer and checks if it is correct or not
    def take_answer(self, question_index, answer):
        #grab the question, if it exists
        try:
            q = self.questions[question_index]
        except:
            print("Could not grab question")
            return
        else:
            #there are 2 situations to consider:
            #1 - the user entered in the answer as words (we already have it then)
            case_1_correct = q.check_answer(answer)
            
            #2 - the user entered in the answer's letter
            case_2_correct = False
            try:
                answer_index = Test.alpha_index_lookup[answer.lower()]
                corresponding_answer = q.answers[answer_index]
                case_2_correct = q.check_answer(corresponding_answer)
            except:
                pass

            if case_1_correct or case_2_correct:
                print("Correct!")
                self.score += 1
            else:
                print("Wrong answer, the answer is:", q.correct_answer)

    #user input and getting final score
    def take_test(self):
        self.score = 0
        for i in range(len(self.questions)):
            self.display_question(i)
            answer = input("Answer: ")
            self.take_answer(i, answer)
        
        # if self.score > 5:
        #     self.score -= 5
        
        print("Your score is",self.score,"/",self.max_score)
        return self.score

#Lists of the Questions
questionBank = [
    Question("What is the name of the tallest mountain in the world?", "Mount Everest", ["Mount Tenpo", "Mount Everest", "Mount Cameroon", "Mount Kinabalu"]),
    Question("Which continent is in all four hemispheres?", "Africa", ["Africa", "South America", "Asia", "Australia"]),
    Question("Which country has the largest population in the world?", "China", ["Russia", "United States", "China", "Canada"]),
    Question("What is the name of the tallest man-made building ever built?", "Burj Khalifa", ["Burj Khalifa", "Tokyo Skytree", "Aerium", "The Palace of Parliament"]),
    Question("which of the seven continents is the largest in the world?", "Asia", ["Asia", "North America", "Europe", "Africa"]),
    Question("Which country is considered the world's largest island?", "Greenland", ["Philippines", "Greenland", "Madagascar", "Sea Lion Island"]),
    Question("Which ocean is the smallest ocean in the world?", "Artic Ocean", ["Pacific Ocean", "Indian Ocean", "Antartic Ocean", "Artic Ocean"]),
    Question("what is the largest volcano in the world?", "Mauna Loa", ["Taal", "Krakatoa", "Mauna Loa", "Dukono"]),
    Question("What is the name of the longest river in Africa?", "The Nile River", ["The Nile River", "Mississippi River", "Yangtze River", "Volga River"]),
    Question("In the United States which state is considered the largest?", "Alaska", ["California", "Texas", "Mississippi", "Alaska"]),
    Question("Which is the largest country in the world?", "Russia", ["China", "Russia", "Canada", "Monaco"]),
    Question("What country are the \"Spanish Steps\" located in?", "Italy", ["Italy", "Spain", "England", "Austria"]),
    Question("Which ocean is the largest ocean in the world?", "Pacific Ocean", ["Artic Ocean", "Atlantic Ocean", "Pacific Ocean", "Antartic Ocean"]),
    Question("Which language is the most spoken in the world?", "Mandarin", ["Hindi", "English", "Mandarin", "Spanish"]),
    Question("What country are the Great Pyramids of Giza located in?", "Egypt", ["Egypt", "Iran", "United States", "Saudi Arabia"]),
    Question("Where are the Stonehenge's located?", "England", ["Scotland", "Ireland", "Iceland", "England"]),
    Question("What place is considered the coldest place on Earth?", "Antartica", ["Alaska", "Antartica", "Greenland", "Russia"]),
    Question("What is the name of the largest lake in the world?", "Caspian Sea", ["Caspian Sea", "Lake Victoria", "Lake Huron", "Lake Superior"]),
    Question("About 90 percent of the world's population lives in which hemisphere?", "Northern Hemisphere", ["Western Hemisphere", "Southern Hemisphere", "Northern Hemisphere", "Eastern Hemisphere"]),
    Question("Which volcano destroyed the ancient city of Pompeii?", "Mount Vesuvius", ["Taal", "Mount Vesuvius", "Mount Fuji", "Krakatoa"])
]

def task1_test():
    test = Test(random.sample(questionBank, 5))

    student_list = []
    score_list = []
    overall_test_count = 0

    joseph = Student("Joseph", 0)
    jon = Student("Jon", 1)
    sara = Student("Sara", 2)
    denise = Student("Denise", 3)
    ary = Student("Ary", 4)

    student_list.append(joseph)
    student_list.append(jon)
    student_list.append(sara)
    student_list.append(denise)
    student_list.append(ary)

    for student in student_list:
        print("\n-------------")
        print("Taking test for Student", student.name)
        
        if student.id == 0:
            student.take_test(test)
            score_list.append(student.current_quiz_score)
            print("Retaking test...")
            student.take_test(test)
            score_list.append(student.current_quiz_score)
            print("Retaking test...")
            student.take_test(test)
            score_list.append(student.current_quiz_score)
            overall_test_count += 3
            continue
        
        elif student.id == 1:
            student.take_test(test)
            score_list.append(student.current_quiz_score)
            print("Retaking test...")
            student.take_test(test)
            score_list.append(student.current_quiz_score)
            overall_test_count += 2
            continue   
        
        student.take_test(test)
        score_list.append(student.current_quiz_score)
        overall_test_count += 1
        print("-------------\n")
        
        
    joseph.display_individual_stats()
    jon.display_individual_stats()
    sara.display_individual_stats()
    denise.display_individual_stats()
    ary.display_individual_stats()

    average_score = sum(score_list) / len(score_list)

    print("Average Test Score out of", overall_test_count, "tests taken by", len(student_list), "students is", average_score)

# --------------------- TASK 2 ---------------------