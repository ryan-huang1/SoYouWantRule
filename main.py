import sys
from utilities import writer, string_input, render_stats
from rich.prompt import Prompt
import sys
import os
import time
from rich.progress import track
from rich.console import Console
console = Console()

name = ""

if __name__ == "__main__":
    for i in range(1):
        
        console.print("[red underline]Computer:", end = " ")
        writer("Hey there! Glad you're here! In this play through you'll be playing as Aadila, a 22 year old woman from Afghanistan.\n")
        writer("Recently the US government pulled out its troops from Afghanistan and the Taliban took over the country's government. This created a situation which was dangerous to her.\n")
        writer("Her father was a farmer and she grew up tending to crops. She is an only child, her mother passed away during childbirth and her father recently died from a heart attack.\n")
        writer("She is immigrating to Happy Land for a home where she does not live in fear and can start a new life and create a family.\n")
        time.sleep(3)
        os.system("clear")

        print(                                                                                                                              
        "                                                                                           .---.                     _______       \n"
        ".                     _________   _...._    _________   _...._                             |   |             _..._   \  ___ `'.    \n"
        ".'|                   \        |.'      '-. \        |.'      '-. .-.          .-          |   |           .'     '.  ' |--.\  \   \n"
        "< |                    \        .'```'.    '.\        .'```'.    '.\ \        / /          |   |          .   .-.   . | |    \  '  \n"
        "| |             __      \      |       \      \\      |       \     \\ \      / /            |   |    __    |  '   '  | | |     |  ' \n"
        "| | .'''-.   .:--.'.     |     |        |    | |     |        |    | \ \    / /            |   | .:--.'.  |  |   |  | | |     |  | \n"
        "| |/.'''. \ / |   \ |    |      \      /    .  |      \      /    .   \ \  / /             |   |/ |   \ | |  |   |  | | |     ' .' \n"
        "|  /    | | `] __ | |    |     |\`'-.-'   .'   |     |\`'-.-'   .'     \ `  /              |   |`] __ | | |  |   |  | | |___.' /'  \n"
        "| |     | |  .'.''| |    |     | '-....-'`     |     | '-....-'`        \  /               |   | .'.''| | |  |   |  |/_______.'/   \n"
       "| |     | | / /   | |_  .'     '.             .'     '.                 / /                '---'/ /   | |_|  |   |  |\_______|/    \n"
       "| '.    | '.\ \._,\ '/'-----------'         '-----------'           |`-' /                      \ \._,\ '/|  |   |  |              \n"
       "'---'   '---'`--'  `[]                                                '..'                        `--'  `] '--'   '--'              \n\n")

        console.print("[red underline]Computer:", end=" ")
        writer("Hello welcome to Happy Land! Welcome in, we'd love to have you here. \n")
        writer("Right now you don’t have to pay anything just focus on getting on your feet. In six months if you still wanna live here you will fill out a form to become a citizen. \nThis comes with a fine. This is even given to people who have grown up here, it’s usually given to them at 20 and a half. \n")
        writer("To vote you must be a citizen and have a high school education or an equivalent. \nOh don’t worry about not having it, we have free schooling to get you caught up with what you need to know! Our classes will fit around your schedule! \n")
        writer("We have our elections every two and a half years, but in the middle of that we have another election to see how the Top rat is doing and if an impeachment is desired. \nOh and after you’ve been a citizen for 5 years you can run for president too! I’m getting ahead of myself anyway!\n") 
        os.system("clear")
        console.print("[red underline]Computer:", end=" ")
        writer("The government of happy land is a representative democracy, like I said our elections are every 2 and a half years and the maximum terms allowed is 4. \n")
        writer("We really value community work here so anyone who is capable will have to do 20 hours of community service every year. \n")
        writer("Other values that are important is always use your voice when you can and vote! \nSome of the government’s responsibilities are freedom of speech, protection of rights, restriction of police, reading of rights in court, and right to an attorney. \n")
        writer("Oh Oh I almost forgot the best part! We have free healthcare (not including gambling addictions), gambling facilities, and free education. \n")
        writer("I am so excited for you. I think you're gonna love it here! I'm gonna hand you off to ")
        console.print("[blue underline]Dianne", end="")
        writer(". She will help you with your job, good luck! \n")

        os.system("clear")

        console.print("[blue underline]Dianne:", end=" ")
        writer("First of all lets start off with our name!")
        name = Prompt.ask("")
        console.print("[blue underline]Dianne:", end=" ")
        writer(f'Hi {name}, it\'s so nice to meet you!\n')
        os.system('clear')
        console.print("[blue underline]Dianne:", end=" ")
        writer("I'm Dianne, I'll be the one who'll help you get set up your new life here\n")
        writer("First of all, the gov of happy land give free traning to get you a higher skilled job! Which do you want?\n")
        job = Prompt.ask("Job Choice", choices=["Software Developer", "Doctor", "Engineer"])
        console.print("[blue underline]Dianne:", end=" ")
        writer(f'Nice choice! Being a {job} is great! I\'ll get you to the provided school now!\n')

        #ascii full screen transition animation
        os.system('clear')
        
        for i in track(range(70), description="Completing School..."):
            time.sleep(.05)  # Simulate work being done

        console.print("[blue underline]Dianne:", end=" ")
        writer("You've completed your traning! Now you'll be able to get a job as a doctor!\n")
        acept_job = Prompt.ask("Do you accept the job?", choices=["Yes", "No"])

        if acept_job == "Yes":
            for i in track(range(70), description=f"Working as a {job}..."):
                time.sleep(.05)  # Simulate work being done
        else:
            console.print("[blue underline]Dianne:", end=" ")
            writer("I'm sorry but you have to accept the job. You'll need to have some money in our society.\n")
            Prompt.ask("Do you accept the job?", choices=["Yes", "No"])
            for i in track(range(70), description=f"Working as a {job}..."):
                time.sleep(.05)
