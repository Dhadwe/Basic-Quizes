import random
import time


Geography = [
    {"Question": "What is the capital of France?", "Answer": "Paris"},
    {"Question": "What is the largest continent by area?", "Answer": "Asia"},
    {"Question": "Which river is the longest in the world?", "Answer": "The Nile"},
    {"Question": "What is the samllest country in the world?", "Answer": "Vatican city"},
    {"Question": "Which desert is the largest in the world?", "Answer": "Sahara Desert"},
    {"Question": "What is the tallest mountian in the world?", "Answer": "Mount Everest"},
    {"Question": "Which ocean is the largest?", "Answer": "Pacific Ocean"},
    {"Question": "How many continents are there?", "Answer": "7"},
    {"Question": "what is the capital of Australia?", "Answer": "Canberra"},
    {"Question": "Which country has the most natural lakes?", "Answer": "Canada"},
    {"Question": "What is the longest mountain range in the world?", "Answer": "The Andes"},
    {"Question": "Which country is both a continent and a country?", "Answer": "Australia"},
    {"Question": "What is the capital of Japan?", "Answer": "Tokyo"},
    {"Question": "Which is the most populous country in the world?", "Answer": "India"},
    {"Question": "what isthe largest country by land area", "Answer": "Russia"},
    {"Question": "Which African country has the largest population?", "Answer": "Nigeria"},
    {"Question": "Which sea is the saltiest in the world?", "Answer": "The Dead Sea"},
    {"Question": "What is the smallest continent?", "Answer": "Australia"},
    {"Question": "what country has the longest coastline?", "Answer": "canada"},
    {"Question": "What is the capital of Canada", "Answer": "Ottawa"},
    {"Question": "Which strait seperates europe from Africa?", "Answer": "The Strait of Gibraltar"},
    {"Question": "What is the largest lake in the world?", "Answer": "The Caspian Sea"},
    {"Question": "Which country contains the Amazon rainforest?", "Answer": "Brazil"},
    {"Question": "What is the capital of South Africa?", "Answer": "Pretoria"},

]

History = [
    {"Question": "Who was the first president of the US?", "Answer": "George Washington"},
    {"Question": "in what year did WW2 end", "Answer": "1945"},
    {"Question": "What empire was ruled by Julius Caesar?", "Answer": "The roman empire"},
    {"Question": "Who was the first woman to win a Nobel Prize?", "Answer": "Marie Curie"},
    {"Question": "In what year did the Berlin wall fall?", "Answer": "1989"},
    {"Question": "Who was the first person to walk on the moon?", "Answer": "Neil Armstrong"},
    {"Question": "Which ancient wonder was located in Alexandria, egypt?", "Answer": "The lighthouse of Alexandria"},
    {"Question": "who was the longest reigning British Monarch?", "Answer": "Queen Elizabeth 2"},
    {"Question": "In what year did the Titanic sink?", "Answer": "1912"},
    {"Question": "Which civilisation built Machu Picchu", "Answer": "The Inca"},
    {"Question": "who was the leader of Nazi Germany during WW2", "Answer": "Adolf Hitler"},
    {"Question": "In what year did the French Revolution begin?", "Answer": "1789"},
    {"Question": "Which country did Christopher Columbus sail for?", "Answer": "Spain"},
    {"Question": "who was the first Emperor of china?", "Answer": "Qin Shi Huang"},
    {"Question": "What war was fought between the north and the south of the US", "Answer": "The American Civil War"},
    {"Question": "which ancient civilisation built the pyramids at Giza?", "Answer": "The Ancient Egyptians"},
    {"Question": "In what year did WW1 begin", "Answer": "1914"},
    {"Question": "Who invented the telephone", "Answer": "Alexander Grahm Bell"},
    {"Question": "Which empire as the largest in history by land area?", "Answer": "The mongol Empire"},
    {"Question": "Who was the first president of South africa after aparatheid", "Answer": "nelson Mandela"},
    {"Question": "In what year did the US declare independence?", "Answer": "1776"},
    {"Question": "Who was the Egyptian queen who allied with julius Ceasar", "Answer": "Ceopatra"},
    {"Question": "Which war saw the use of the first atomic bomb?", "Answer": "WW2"},
    {"Question": "Who wrote the Communist Manifesto?", "Answer": "Karl Marx and the Friedrich Engels"},


]


Science = [
    {"Question": "What is the chemical symbol for water?", "Answer": "H2O"},
    {"Question": "how many bones are in the adult human body?", "Answer": "206"},
    {"Question": "What planet is known as the red planet?", "Answer": "Mars"},
    {"Question": "What is the most abundant gas in Earth's atmosphere?", "Answer": "Nitrogen"},
    {"Question": "Who developed the theory of general relativity", "Answer": "Albert Einstein"},
    {"Question": "What is the powerhouse of the cell?", "Answer": "the mitochondria"},
    {"Question": "How many planets are in our solar system", "Answer": "8"},
    {"Question": "what is the atomic number of carbon?", "Answer": "6"},
    {"Question": "What force keeps planets in orbit around the sun?", "Answer": "Gravity"},
    {"Question": "What is the hardest natural substance on Earth?", "Answer": "Diamond"},
    {"Question": "What part of the cell contains DNA?", "Answer": "The nucleus"},
    {"Question": "what is the chemical symbol for gold?", "Answer": "Au"},
    {"Question": "How many chromosomes do humans have?", "Answer": "46"},
    {"Question": "What is the name of the process by which water turns into vapour", "Answer": "Evaporation"},
    {"Question": "What is the most abundant element in the universe?", "Answer": "Hydrogen"},
    {"Question": "What type of energy does the sun produce?", "Answer": "Nuclear energy"},
    {"Question": "what is the name of the galaxy we live in?", "Answer": "The milky way"},
    {"Question": "What is the pH of a neutral substance", "Answer": "7"},
    {"Question": "What is the smallest planet in our solar system?", "Answer": "Mercury"},
    {"Question": "What organ produces insulin in the human body?", "Answer": "The pancreas"},
    {"Question": "what is the chemical symbol for oxygen?", "Answer": "O"},
]

all_subjects = Science + Geography + History

def start_screen():
    print("*******" * 5)
    print("Welcome to the BASIC quiz")
    time.sleep(0.5)
    print("*******" * 5)
    print("If you do bad here you highkey suck dawg idek atp")
    time.sleep(1)
    print("*******" * 5)
    print("all you have to do is choose what subject you wanna get quizzed on")
    print("and then answer the questions presented to you")
    time.sleep(0.5)
    print("*******" * 5)
    print("After you finish the quiz you will be presented with your score and how long it took you to finish the quiz")
    time.sleep(0.25)
    print("*******" * 5)
    time.sleep(0.25)
    print("*******" * 5)
    time.sleep(0.25)
    print("*******" * 5)
    time.sleep(0.25)
    print("*******" * 5)
    print("So lets get started")
    

def choose_quiz():
    print("please enter a number corresponding to one of the following choices:")
    print("1. Science \n2. Geography \n3. History \n4. all_subjects")
    try:
        choice = int(input( ))
    except:
        "please enter a number"
        choose_quiz()

    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        return choice
    else:
        print("please enter 1, 2, 3 or 4")
        choose_quiz()

def get_questions(choice):
    if choice == 1:
        questions = Science
    elif choice == 2: 
        questions = Geography
    elif choice == 3:
        questions = History
    elif choice == 4:
        questions = all_subjects
    return random.sample(questions,10)


def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return True
    else:
        return False

def show_results(time_elapsed, score):
    print(f"you took {time_elapsed:.2f} seconds to finish this quiz")
    time.sleep(0.25)
    if score == 10:
        print(score)
        print("outstanding")
    elif score >= 7:
        print(score)
        print("great")
    elif score >= 5:
        print(score)
        print("good job")
    elif score >= 3:
        print(score)
        print("start studying")
    else:
        print(score)
        print("horrible")

def main_quiz():
    start_screen()
    choice = choose_quiz()
    questions = get_questions(choice)
    score = 0
    starting_time = time.time()
    for q in questions:
        print(q["Question"])
        user_answer = input("")
        result = check_answer(user_answer, q["Answer"])
        if result == True:
            print("Thats correct")
            score += 1
        else:
            print(f"Thats incorrect. The correct answer is {q['Answer']}")
    end_time = time.time()
    time_elapsed = (end_time - starting_time)
    show_results(time_elapsed, score)


main_quiz()