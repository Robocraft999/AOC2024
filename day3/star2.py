from helpers import *
path, testpath = get_input(3)

sum = 0
do = True
text = ""

for line in open(path):
    text += line.strip()

index = text.find("mul(")
while index > -1:
    try:
        if do:
            first_num = int(text[index+4:].split(",")[0])
            second_num = int(text[index:].split(",")[1].split(")")[0])
            sum += first_num * second_num
    except:
        pass
    new_index = text.find("mul(", index+1)
    dont_index = text.find("don't()", index, new_index)
    if dont_index != -1:
        do_index = text.find("do()", dont_index, new_index)
        if do_index == -1:
            do = False
        else:
            do = True
    if not do:
        do_index = text.find("do()", dont_index)
        if do_index != -1:
            index = do_index
            do = True
        else:
            break

    index = text.find("mul(", index+1)
print(sum)