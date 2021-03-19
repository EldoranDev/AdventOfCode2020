from src.lib.input import getInput

import re

def first(data):
    count = 0

    for line in data:
        charMap = {}
        match = re.search('([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)', line)
        
        for char in match.group(4):
            if char not in charMap:
                charMap[char] = 0
            charMap[char] += 1
        
        char = match.group(3)

        if char in charMap and charMap[char] >= int(match.group(1)) and charMap[char] <= int(match.group(2)):
            count += 1

    return count


def second(data):
    count = 0

    for line in data:
        match = re.search('([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)', line)

        char = match.group(3)
        pw = match.group(4)

        if (pw[int(match.group(1))-1] == char and pw[int(match.group(2))-1] != char) or (pw[int(match.group(1))-1] != char and pw[int(match.group(2))-1] == char):
            count += 1

    return count

if __name__ == '__main__':
    data = getInput(2020, 2)


    print("Part 1: " + str(first(data)))
    print("Part 2: " + str(second(data)))
    
