import sys, time, os
from yachalk import chalk

# message = "Computer: Hello world, nice to meet you. \n\
# Me : Nice to meet you too. \n\
# Computer: Goodbye."

def typewriter(message) :
    for char in message:
        sys.stdout. write (char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep (0.07)
        else:
            time.sleep (1)

def string_input(prompt):
    typewriter(prompt)
    user_input = input()
    message = user_input[0].upper() + user_input[1:]
    return message

def render_stats(prompt):

    os.system('clear')
    size = os.get_terminal_size().columns-23
    spaces = " " * size

    stats_table = ["┌─────────────────────┐", "│Total Budget: xxx    │", "│                     │", "│Health Care: xxx     │", "│Social Services: xxx │", "│Defence: xxx         │", "│Education: xxx       │", "│Discretionary: xxx   │", "├──────────────────── │", "│Satisfaction: xx     │", "│Stablity: xx         │", "│Economy: xx          │", "└─────────────────────┘"]

    for i in range(13):
        try:
            empty_size = size - len(prompt[i])
            space_dynamic = " " * empty_size
            print(prompt[i] + space_dynamic + stats_table[i])
        except IndexError:
            print(spaces + stats_table[i])

os.system ("clear") #clear
render_stats(["hello", "hello", "hello"])
print(chalk.blue("Hello world!"))
