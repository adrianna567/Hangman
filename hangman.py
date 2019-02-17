'''
OBJECTIVE: 
    The objective is to create a hangman game
ALGORITHM:
    First we need to write the three functions in our program 
    The first function that will be defined is the function that randomly selects a word from the text dictionary we will create. 
    The second function defined is the function that takes as input from the user which will be each letter guessed
    The third function defined will be the one that will take the letters guessed correctly and turns it into a string 
    In order for the first function to work we need to create a text file that the program can reference. 
    Next we need to make sure we are working in the main module 
    Now we need to create the various variables we are going to use to store the data the user enters.
    We need a variable for the word the computer picks. 
    we will also need to create a set of data that holds the letters guessed wrong and another one for letters guessed correctly. 
    Next we need to display an introduction to the program so users will know what to do. 
    Next we will build a repetitive system, so that the user will keep guessing words 
    Next we will code the game itself
    The first step is to have the user guess a word.
    Next we will create different options whether the user guessed correct or incorrect
    The next step is to print out the number of guesses that the user has left and what they currently have guessed correctly in the word 
    The final step is a conditional statement at the end that lets them know if they won or not
    PSUEDOCODE: 
        This is taking the algorithm we just wrote and adding what code we can use to complete each step 
        First we need to write the three functions in our program 
        We will use the define function tool to create the functions 
        The first function that will be defined is the function that randomly selects a word from the text dictionary we will create.
        We will use the open() function and the .readlines() functions to bring the text file into the program
        The second function defined is the function that takes an input from the user which will be  each letter guessed
        We will use the input() function to bring the users input into the program 
        The third function defined will be the one that will take the letters guessed correctly and turns it into a string 
        We will use a list and loop to check which letter they guessed and put it in the order of the word
        Create a text file that the program can reference 
        We will use LiClispe to create the text file 
        Next we need to make sure we are working in the main module
        We will use a conditional statement to check if we are working in the main module 
        Then, create the various variables we are going to use to store the data the user enters. 
        We need a variable for the word the computer picks. 
        We will also need to create a list that holds the letters guessed wrong and another list for letters guessed correctly.
        Next we need to print an introduction to the program so users will know what to do. 
        Next we need to create a loop that allows the user to keep guessing 
        We will use a while loop to repeat the game
        Next we will code the game itself
        The first step is to have the user guess a word. 
        Next we will create different options whether the user guessed correct or incorrect
        The next step is to print out the number of guesses that the user has left and what they currently have guessed correctly in the word 
        We will use the .format() function format the print statement 
        The final step is a conditional statement that will print if the user won or not
'''

import random 

def pick_random_word(): 
    """
    This function picks a random word from the words dictionary. 
    """
    # open the word dictionary
    with open("word.txt.",'r') as f:
            words = f.readlines() 
            
    # generate a random index 
    # -1 because len(words) is not a valid index into the list 'words' 
    index = random.randint(0, len(words) - 1) 
    
    # print out the word at that index 
    word = words[index].strip() 
    return word 
def ask_user_for_next_letter(): 
    #This function gets a letter fuess from the user 
    letter = input("Guess your letter: ") 
    return letter.strip().upper() 

def generate_word_string(word, letters_guessed): 
    #This function generates the word display that shows which letters 
    #have been guessed correctly
    output = [] 
    for letter in word: 
        if letter in letters_guessed: 
            output.append(letter.upper()) 
        else:
            output.append("_") 
    return " ".join(output) 

#This condition checks that the module we are using is currently the main module

if __name__ == '__main__':
    WORD = pick_random_word() 
    
    letters_to_guess = set(WORD) 
    correct_letters_guessed = set()
    incorrect_letters_guessed = set() 
    num_guesses = 0 
    
    print("Welcome to Hangman!") 
    #This loop repeats the guessing sequence until the user guesses all the word 
    #or until the user runs out of guesses 
    while (len(letters_to_guess) > 0) and num_guesses < 6: 
        guess = ask_user_for_next_letter() 
        guess = guess.lower() 
        # check if we already guessed that 
        # letter 
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed: 
            # print out message 
            print("You already guessed that letter.") 
            continue 
        # if the guess was correct 
        if guess in letters_to_guess:
            # update the letters_to_guess
            letters_to_guess.remove(guess) 
            # update the correct letters guessed 
            correct_letters_guessed.add(guess) 
        else: 
            incorrect_letters_guessed.add(guess) 
            # only update the number of guesses 
            # if you guess incorrectly 
            num_guesses += 1
            
        word_string = generate_word_string(WORD, correct_letters_guessed) 
        print(word_string) 
        print("You have {} guesses left".format(6 - num_guesses))
        
    # tell the user they have won or lost 
    if num_guesses < 6: 
        print("congratulations! You correctly guessed the word {}".format(WORD)) 
    else:
        print("Sorry, you lose! Your word was {}".format(WORD))
        