import sys, time, os
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

def render_stats():
    os.system('clear')
    size = os.get_terminal_size().columns-22
    spaces = " " * size
    print(f'{spaces}┌────────────────────┐\n{spaces}│Total Budget: xxx   │\n{spaces}│                    │\n{spaces}│Health Care: xxx    │\n{spaces}│Social Services: xxx│\n{spaces}│Defence: xxx        │\n{spaces}│Education: xxx      │\n{spaces}│Discretionary: xxx  │\n{spaces}├─────────────────── │\n{spaces}│Satisfaction: xx    │\n{spaces}│Stablity: xx        │\n{spaces}│Economy: xx         │\n{spaces}└────────────────────┘')

os.system ("clear") #clear
render_stats()
