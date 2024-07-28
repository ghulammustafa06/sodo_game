import random
import time
import sys
import json
from datetime import datetime

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_title():
    title = """
    ███████╗ ██████╗ ██████╗  ██████╗     ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
    ███████╗██║   ██║██║  ██║██║   ██║    ██║  ███╗███████║██╔████╔██║█████╗  
    ╚════██║██║   ██║██║  ██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
    ███████║╚██████╔╝██████╔╝╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    """
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
            Question("What does GUI stand for?", "graphical user interface", 1),
            Question("What does CLI stand for?", "command line interface", 1),
            Question("What does SSD stand for?", "solid state drive", 2),
            Question("What does HTML stand for?", "hypertext markup language", 2),
            Question("What does CSS stand for?", "cascading style sheets", 2),
            Question("What does IDE stand for?", "integrated development environment", 2),
            Question("What does API stand for?", "application programming interface", 2),
            Question("What does JSON stand for?", "javascript object notation", 2),
            Question("What does HTTP stand for?", "hypertext transfer protocol", 1),
            Question("What does HTTPS stand for?", "hypertext transfer protocol secure", 1),
            Question("What does URL stand for?", "uniform resource locator", 2),
            Question("What does DNS stand for?", "domain name system", 2),
            Question("What does LAN stand for?", "local area network", 2),
            Question("What does WAN stand for?", "wide area network", 2),
            Question("What does IP stand for?", "internet protocol", 3),
            Question("What does DNS stand for?", "domain name system", 3),
            Question("What does FTP stand for?", "file transfer protocol", 3),
            Question("What does SSH stand for?", "secure shell", 3),
            Question("What does IoT stand for?", "internet of things", 3),
            Question("What does API stand for?", "application programming interface", 3),
            Question("What does BIOS stand for?", "basic input output system", 3),
            Question("What does SQL stand for?", "structured query language", 3),
            Question("What does OOP stand for?", "object-oriented programming", 3),
            Question("What does MVC stand for?", "model-view-controller", 3),
            Question("What does HTTP stand for?", "hypertext transfer protocol", 3),
            Question("What does URL stand for?", "uniform resource locator", 3),
]

def load_high_scores():
    try:
        with open("high_scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_high_score(name, score, difficulty):
    high_scores = load_high_scores()
    high_scores.append({"name": name, "score": score, "difficulty": difficulty, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    high_scores.sort(key=lambda x: x["score"], reverse=True)
    high_scores = high_scores[:10] 
    with open("high_scores.json", "w") as f:
        json.dump(high_scores, f)

def display_high_scores():
    high_scores = load_high_scores()
    typewriter_effect("\nHigh Scores:")
    for i, score in enumerate(high_scores, 1):
        typewriter_effect(f"{i}. {score['name']} - {score['score']} points ({score['difficulty']}) - {score['date']}")

def choose_difficulty():
    while True:
        difficulty = input("Choose your difficulty (easy/medium/hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        typewriter_effect("Invalid choice. Please choose easy, medium, or hard.")

def power_up():
    power_ups = ["Double Points", "Extra Life", "Skip Question"]
    chosen_power_up = random.choice(power_ups)
    typewriter_effect(f"You've earned a power-up: {chosen_power_up}!")
    return chosen_power_up

def use_power_up(power_up, lives, score):
    if power_up == "Double Points":
        typewriter_effect("Double Points activated for this question!")
        return lives, score * 2
    elif power_up == "Extra Life":
        lives += 1
        typewriter_effect(f"Extra Life used! You now have {lives} lives.")
        return lives, score
    elif power_up == "Skip Question":
        typewriter_effect("Question skipped!")
        return lives, score
    return lives, score

def play_game():
    score = 0
    total_questions = 0
    lives = 3
    streak = 0
    max_streak = 0
    power_ups = []
    
    typewriter_effect("Welcome to the SODO Game - Test your tech knowledge!")
    time.sleep(1)
    
    difficulty = choose_difficulty()
    
    typewriter_effect(f"You've chosen {difficulty} difficulty. Let's begin!")
    time.sleep(1)
    
    random.shuffle(questions)
    
    for question in questions:
        if (difficulty == "easy" and question.difficulty > 1) or \
           (difficulty == "medium" and question.difficulty > 2) or \
           (difficulty == "hard" and question.difficulty > 3):
            continue
        
        total_questions += 1
        typewriter_effect(f"\nQuestion {total_questions}: {question.question}")
        
        if power_ups:
            use_power = input("Do you want to use a power-up? (yes/no): ").lower() == "yes"
            if use_power:
                chosen_power_up = random.choice(power_ups)
                power_ups.remove(chosen_power_up)
                lives, score = use_power_up(chosen_power_up, lives, score)
                if chosen_power_up == "Skip Question":
                    continue
        
        start_time = time.time()
        user_answer = input("Your answer: ").lower()
        end_time = time.time()
        
        time_taken = end_time - start_time
        
        if user_answer == question.answer:
            typewriter_effect("Correct! Well done!")
            score += 1
            streak += 1
            if streak > max_streak:
                max_streak = streak
            
            if time_taken < 5:
                bonus = 2
            elif time_taken < 10:
                bonus = 1
            else:
                bonus = 0
            
            score += bonus
            if bonus > 0:
                typewriter_effect(f"Quick answer bonus: +{bonus} points!")
            
            if streak % 5 == 0:
                new_power_up = power_up()
                power_ups.append(new_power_up)
        else:
            typewriter_effect(f"Incorrect. The correct answer is: {question.answer}")
            lives -= 1
            streak = 0
            if lives == 0:
                typewriter_effect("Game Over! You've run out of lives.")
                break
        
        typewriter_effect(f"Lives remaining: {lives}")
        typewriter_effect(f"Current score: {score}")
        typewriter_effect(f"Current streak: {streak}")
        typewriter_effect(f"Power-ups available: {', '.join(power_ups) if power_ups else 'None'}")
        
        if total_questions % 3 == 0:
            typewriter_effect("\nBonus round! Answer correctly to gain an extra life.")
            bonus_question = random.choice(questions)
            typewriter_effect(f"Bonus Question: {bonus_question.question}")
            bonus_answer = input("Your answer: ").lower()
            if bonus_answer == bonus_question.answer:
                typewriter_effect("Correct! You've earned an extra life!")
                lives += 1
            else:
                typewriter_effect(f"Incorrect. The answer was: {bonus_question.answer}")
        
        time.sleep(1)
    
    typewriter_effect("\nGame Over!")
    typewriter_effect(f"Final Score: {score}")
    typewriter_effect(f"Questions Answered: {total_questions}")
    typewriter_effect(f"Accuracy: {(score / total_questions) * 100:.2f}%")
    typewriter_effect(f"Max Streak: {max_streak}")
    
    player_name = input("Enter your name for the high score table: ")
    save_high_score(player_name, score, difficulty)
    display_high_scores()
    
    return score

if __name__ == "__main__":
    display_title()
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            typewriter_effect("Thank you for playing SODO Game! Goodbye!")
            break