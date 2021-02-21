import random
import sys
import time
class Hangman :
    def __init__(self):
        self.board = []
        self.lives = 6
        self.words = ["charmander", "jigglypuff","staryu","pikachu","butterfree","onix","squirtle"]
        self.choosed_word = ''

    def main(self):
        print("Welcome!")
        start_game = input("Star new game Yes/No").lower()
        if start_game == 'yes' :
            print("The game has started!")
            time.sleep(2)
            print("You have 6 lives! Good Luck!")
            time.sleep(2)
            print("-----------------------------")
            self.choosed_word = random.choice(self.words)
            self.setup()
            self.play()
        else :
            sys.exit("Goodbye!")
    def setup(self):
        for ch in range(len(self.choosed_word)):
            self.board.append("_")
    def play(self):
        guessed_words = []
        while self.lives > 0 :
            letter = input("Guess a letter:")
            if letter in self.choosed_word and letter not in guessed_words:
                guessed_words.append(letter)
                self.new_board(letter)
                self.check()

            elif letter in guessed_words:
                print("You already wrote that letter! Try another one!")
            else:
                guessed_words.append(letter)
                print("Its wrong! Try another letter")
                self.lives -=1
            print(self.board)
        print ("Game over! The word was:" +  self.choosed_word)

    def new_board (self,letter):
        for i, ch in enumerate(self.choosed_word):
            if letter == ch:
                self.board[i] = letter

    def check(self):

        if self.board == list(self.choosed_word):
            print("Good job! You won!")
            sys.exit("Goodbye!")



new_game = Hangman()
new_game.main()

