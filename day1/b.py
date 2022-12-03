
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


top_three_cal = 0
for i in range(3):
    max_calorie_index = max(elv_dict, key = lambda x : elv_dict[x])
    top_three_cal = top_three_cal + elv_dict[max_calorie_index]
    del elv_dict[max_calorie_index]

print(top_three_cal)

