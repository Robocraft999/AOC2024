from helpers import *
path, testpath = get_input(3)

sum = 0
text = ""

for line in open(path):
    text += line.strip()

index = text.find("mul(")
while index > -1:
    try:
        first_num = int(text[index+4:].split(",")[0])
        second_num = int(text[index:].split(",")[1].split(")")[0])
        sum += first_num * second_num
    except:
        pass
    index = text.find("mul(", index+1)

print(sum)