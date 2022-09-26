import time
from rich.progress import track

for i in track(range(70), description="Completing School..."):
    time.sleep(.05)  # Simulate work being done