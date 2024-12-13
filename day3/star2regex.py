from helpers import *
import re
path = get_input(3)
testpath = "day3/testinput.txt"

text = ""

for line in open(path):
    text += line.strip()

print(sum([sum([int(match[0]) * int(match[1]) for match in re.findall(r"mul\((\d+),(\d+)\)", part.split("don't()")[0])]) for part in text.split("do()")]))