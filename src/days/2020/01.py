from src.lib.input import getInput
import time

def first(data):
    for a in data:
        for b in data:
            if int(a) + int(b) == 2020:
                return int(a) * int(b)

def second(data):
    for a in data:
        for b in data:
            for c in data:
                if int(a) + int(b) + int(c) == 2020:
                    return int(a) * int(b) * int(c)

if __name__ == '__main__':
    data = getInput(2020, 1)
    
    # Speeds up second part by more then 10x
    data.sort(reverse=True)

    print("Part 1: " + str(first(data)))
    print("Part 2: " + str(second(data)))
    
