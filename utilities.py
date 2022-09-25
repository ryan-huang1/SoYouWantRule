import sys, time, os
from yachalk import chalk

# message = "Computer: Hello world, nice to meet you. \n\
# Me : Nice to meet you too. \n\
# Computer: Goodbye."

def typewriter(message) :
    char_per_line = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(13):
        try:
            char_per_line[i] = len(message[i])
        except:
            char_per_line[i] = 0

    print(char_per_line)

    writen_per_line = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    writen = ["", "", "", "", "", "", "", "", "", "", "", "", ""]

    for i in range(13):
        for j in range(char_per_line[i]):
            writen_per_line[i] += 1
            sys.stdout.write(message[i][j])
            writen[i] += message[i][j]
            sys.stdout.flush()
            time.sleep(0.1)
            print(writen)
        print()
        time.sleep(.8)
    
    # for char in message:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()

    #     if char !="\n":
    #         time.sleep (0.07)
    #     else:
    #         time.sleep (1)

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

def string_input(prompt):
    typewriter(prompt)
    user_input = input()
    message = user_input[0].upper() + user_input[1:]
    return message

os.system ("clear") #clear
typewriter(["hello", "hello", "hello"])
print(chalk.blue("Hello world!"))
