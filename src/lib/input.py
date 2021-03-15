from pathlib import Path
import os

def getInput(year, day):
    inputFile = Path(os.path.dirname(__file__), '..', '..', 'inputs', str(year), f"{day:0>2}")

    
    with inputFile.open() as f:
        lines = f.readlines()
    
    lines = lines[:-1]
    return lines