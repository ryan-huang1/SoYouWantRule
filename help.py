from utilities import typewriter, string_input

def intro():
    typewriter("Welcome to So You Want to Rule! \n")
    typewriter("As an aspiring ruler, you must make decisions that will affect your political future. \n")
    typewriter("You'll need to get yourself elected, and then to stay in power. \n")
    typewriter("Make enought people happy, and you'll be a success! \n")
    name = string_input("Let's start with your name: ")
    typewriter("Good luck, " +name+ ".")