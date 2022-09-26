import sys
from utilities import writer, string_input, render_stats
from rich.prompt import Prompt
import sys
import os
import time
from rich.progress import track

name = ""

if __name__ == "__main__":
    for i in range(1):
        writer("Computer: Hello welcome to Happy Land! Welcome in, we'd love to have you here. \nTHIS IS HOW OUR GOVERMENT WORKS! We have an open immigration policy so come on in!\n")
        writer("Computer: First of all lets start off with our name!")
        name = Prompt.ask("")
        writer(f'Good luck {name}, have a nice life\n')
        os.system('clear')

        writer("I'll pass you off to the Dianne your local social worker. She'll help you get settled in.\n")
        writer("Dianne: Hello, welcome to Happy Land! I'm Dianne, I'll be the one who'll help you get set up your new life here\n")
        writer("Dianne: First of all, the gov of happy land give free traning to get you a higher skilled job! Which do you want?\n")
        job = Prompt.ask("Job Choice", choices=["Software Developer", "Doctor", "Engineer"])
        writer(f'Nice choice! {job} is a very good choice. I\'ll get you to the provided school now!\n')

        #ascii full screen transition animation
        os.system('clear')
        
        for i in track(range(70), description="Completing School..."):
            time.sleep(.05)  # Simulate work being done

        writer("Dianne: You've completed your traning! Now you'll be able to get a job as a doctor!\n")
        acept_job = Prompt.ask("Do you accept the job?", choices=["Yes", "No"])

        if acept_job == "Yes":
            for i in track(range(70), description=f"Working as a {job}..."):
                time.sleep(.05)  # Simulate work being done
        else:
            writer("Dianne: I'm sorry but you have to accept the job. You'll need to have some money in our society.\n")
            Prompt.ask("Do you accept the job?", choices=["Yes", "No"])
            for i in track(range(70), description=f"Working as a {job}..."):
                time.sleep(.05)
