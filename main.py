import pygame
import cmpt120image as img # Helper functions from cmpt120image.py
import draw                # Your image processing module
import csv
import random

###############################################################
# Keep this block at the beginning of your code. Use caution before you modify.
# If you want to hardcode to speed up development, you can do so

# For example, set just ENV = "v" if coding in VS Code.
# You'll need to uncomment before submission!
def init_env():
    print("\nWelcome! Before we start...")
    env = input("Are you using VS Code (v), Replit (r) or IDLE (i)? ").lower()
    while env not in "vri":
        print("Environment not recognized, type again.")
        env = input("Are you using VS Code (V), Replit (r) or IDLE (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the play_sound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def play_sound(soundfilename, env):
    if env == "v" or env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
#ENV = init_env()
###############################################################

def get_words():
    """
    Reads the blackfoot.csv file and returns a list of words.
    """
    words = []
    try:
        with open('blackfoot.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row: # Ensure row is not empty
                    words.append(row[0])
    except FileNotFoundError:
        print("Error: blackfoot.csv not found. Make sure it is in the same folder.")
    return words

def learn_mode(env, words, num_to_learn):
    """
    Mode 1: Learn
    Displays images and plays audio for the first 'num_to_learn' words.
    """
    print(f"\n--- LEARN MODE ---")
    print(f"Learning the first {num_to_learn} words.")
    
    # Slice the list to get only the words we are learning
    current_words = words[:num_to_learn]
    
    for word in current_words:
        # 1. Create a white canvas (400x300)
        canvas = img.get_white_image(400, 300)
        
        try:
            # 2. Load the image
            image_pixels = img.get_image("images/" + word + ".png")
            
            # 3. Draw image randomly on canvas
            draw.distribute_items(canvas, image_pixels, 1)
            
            # 4. Show image
            img.show_image(canvas)
            
            # 5. Play sound
            play_sound(word, env)
            
            # 6. Wait for user
            input(f"Word: {word}. Press Enter to continue...")
            
        except Exception as e:
            print(f"Error loading resources for {word}: {e}")

def play_mode(env, words, num_to_learn):
    """
    Mode 2: Play (Seek-and-Count Game)
    """
    print("\n--- PLAY MODE ---")
    
    # Filter words to only those currently being learned
    available_words = words[:num_to_learn]
    
    # Need at least 3 words to play
    if len(available_words) < 3:
        print("You need to learn at least 3 words to play!")
        return

    try:
        rounds = int(input("How many rounds would you like to play? "))
    except ValueError:
        print("Invalid input. Returning to menu.")
        return

    score = 0

    for i in range(rounds):
        print(f"\nRound {i+1} of {rounds}")
        
        # 1. Create challenge list: 3 random unique words from available_words
        challenge_list = random.sample(available_words, 3)
        
        # 2. Randomly select one word as the "spoken word"
        spoken_word = random.choice(challenge_list)
        
        # 3. Create white canvas
        canvas = img.get_white_image(400, 300)
        
        correct_answer = 0
        
        # 4. Process each word in the challenge list
        for word in challenge_list:
            # Load image
            item = img.get_image("images/" + word + ".png")
            
            # --- Transformations ---
            # A. Random Color
            rand_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            item = draw.recolor_image(item, rand_color)
            
            # B. Random Minify (True/False)
            if random.choice([True, False]):
                item = draw.minify(item)
            
            # C. Random Mirror (True/False)
            if random.choice([True, False]):
                item = draw.mirror(item)
                
            # D. Random Count (1 to 4)
            count = random.randint(1, 4)
            
            # If this is the spoken word, record the count as the answer
            if word == spoken_word:
                correct_answer = count
            
            # Draw items on canvas
            draw.distribute_items(canvas, item, count)
            
        # 5. Display canvas and play sound
        img.show_image(canvas)
        play_sound(spoken_word, env)
        
        # 6. Ask user for answer
        try:
            guess = int(input(f"Listen to the sound. How many objects matching that sound do you see? "))
            if guess == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.")
        except ValueError:
            print(f"Invalid input. The correct answer was {correct_answer}.")
            
    print(f"\nGame Over! Final Score: {score}/{rounds}")

def settings_mode(current_num, total_words):
    """
    Mode 3: Settings
    Change the number of words to learn.
    """
    print("\n--- SETTINGS ---")
    print(f"Current number of words to learn: {current_num}")
    print(f"Total available words: {total_words}")
    
    try:
        new_num = int(input(f"Enter new number (3 - {total_words}): "))
        if 3 <= new_num <= total_words:
            return new_num
        else:
            print(f"Number must be between 3 and {total_words}.")
            return current_num
    except ValueError:
        print("Invalid input.")
        return current_num

def main():
    # Initialize the image system
    img.init()
    
    # Setup Environment
    env = init_env()
    
    # Load Words
    words = get_words()
    if not words:
        return # Exit if CSV failed
        
    # Default number of words to learn
    num_to_learn = 3
    
    # Main Menu Loop
    running = True
    while running:
        print("\nMAIN MENU")
        print("1. Learn")
        print("2. Play")
        print("3. Settings")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            learn_mode(env, words, num_to_learn)
        elif choice == '2':
            play_mode(env, words, num_to_learn)
        elif choice == '3':
            num_to_learn = settings_mode(num_to_learn, len(words))
        elif choice == '4':
            print("Goodbye!")
            running = False
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()






