import random

questions = {
    "What language is primarily used for system programming?": {
        "a": "C",
        "b": "Java",
        "c": "Python",
        "d": "PHP",
        "correct": "a"
    },
    "Which of the following is a high-level programming language?": {
        "a": "Assembly",
        "b": "Python",
        "c": "C++",
        "d": "HTML",
        "correct": "b"
    },
    "What is the file extension of a Java source code file?": {
        "a": ".jav",
        "b": ".class",
        "c": ".java",
        "d": ".jar",
        "correct": "c"
    },
    "Which of the following is NOT a valid HTML tag?": {
        "a": "<div>",
        "b": "<span>",
        "c": "<paragraph>",
        "d": "<a>",
        "correct": "c"
    },
    "Which language is used for styling web pages?": {
        "a": "HTML",
        "b": "CSS",
        "c": "JavaScript",
        "d": "Python",
        "correct": "b"
    },
    "What programming language is known for its use in web development?": {
        "a": "Java",
        "b": "C#",
        "c": "PHP",
        "d": "JavaScript",
        "correct": "d"
    },
    "Which of the following is a server-side scripting language?": {
        "a": "JavaScript",
        "b": "HTML",
        "c": "Python",
        "d": "PHP",
        "correct": "d"
    },
    "Which of the following is a dynamically typed language?": {
        "a": "Java",
        "b": "C",
        "c": "Python",
        "d": "PHP",
        "correct": "c"
    },
    "What does CSS stand for in web development?": {
        "a": "Computer Style Sheet",
        "b": "Cascading Style Sheet",
        "c": "Creative Style Sheet",
        "d": "Colorful Style Sheet",
        "correct": "b"
    },
    "What is the syntax used to declare a variable in Python?": {
        "a": "var",
        "b": "int",
        "c": "str",
        "d": "None of the above",
        "correct": "d"
    },
    "Who developed the C programming language?": {
        "a": "Dennis Ritchie",
        "b": "Guido van Rossum",
        "c": "Bjarne Stroustrup",
        "d": "Larry Wall",
        "correct": "a"
    },
    "Which data type in Java is used for text?": {
        "a": "int",
        "b": "double",
        "c": "String",
        "d": "char",
        "correct": "c"
    },
    "What does the acronym HTML stand for?": {
        "a": "Hyperlinks and Text Markup Language",
        "b": "Home Tool Markup Language",
        "c": "Hyper Text Markup Language",
        "d": "Hyperlink Terminal Markup Language",
        "correct": "c"
    },
    "Which of the following is NOT a valid CSS property?": {
        "a": "color",
        "b": "height",
        "c": "weight",
        "d": "margin",
        "correct": "c"
    }
}

def run_quiz(questions):
    score = 0
    
    for question in questions:
        print(question)
        for option, value in questions[question].items():
            if option != 'correct':
                print(f"{option}: {value}")
        
        answer = input("Enter your answer: ").lower()
        
        if answer == questions[question]['correct']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    
    print(f"You scored {score} out of {len(questions)}")

run_quiz(questions)