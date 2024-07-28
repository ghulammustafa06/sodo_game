import random
import time
import sys

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_title():
    title = """Sodo Game  """
    print(title)

class Question:
    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

        
        questions = [
    Question("What does CPU stand for?", "central processing unit", 1),
    Question("What does GPU stand for?", "graphics processing unit", 1),
    Question("What does RAM stand for?", "random access memory", 1),
    Question("What does PSU stand for?", "power supply", 1),
    Question("What does SSD stand for?", "solid state drive", 2),
    Question("What does HTML stand for?", "hypertext markup language", 2),
    Question("What does CSS stand for?", "cascading style sheets", 2),
    Question("What does API stand for?", "application programming interface", 3),
    Question("What does BIOS stand for?", "basic input output system", 3),
    Question("What does SQL stand for?", "structured query language", 3),
    Question("What does HTTP stand for?", "hypertext transfer protocol", 1),
    Question("What does HTTPS stand for?", "hypertext transfer protocol secure", 1),
    Question("What does URL stand for?", "uniform resource locator", 2),
    Question("What does LAN stand for?", "local area network", 2),
    Question("What does WAN stand for?", "wide area network", 2),
    Question("What does IP stand for?", "internet protocol", 3),
    Question("What does DNS stand for?", "domain name system", 3),
    Question("What does FTP stand for?", "file transfer protocol", 3),
    Question("What does SSH stand for?", "secure shell", 3),
    Question("What does IoT stand for?", "internet of things", 3),
]