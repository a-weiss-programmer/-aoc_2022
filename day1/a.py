
elv_dict = {}
with open("input.txt", "r") as cal_file:
    cal_input = cal_file.readlines()
    num_elves = 0
    cur = 0
    for calorie in cal_input:
        # calorie is empty line
        if calorie == '\n':
            num_elves = num_elves + 1
            elv_dict[num_elves] = cur
            cur = 0
        else:
            cur = cur + int(calorie)


max_calorie = max(elv_dict, key = lambda x : elv_dict[x])

print(elv_dict[max_calorie])

