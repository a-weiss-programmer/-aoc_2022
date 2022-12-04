assignment_contents = []
with open("input.txt", "r") as assign_file:
    assignment_contents = assign_file.readlines()


total_in_each_other = 0
for assignment in assignment_contents:
    section1, section2 = assignment.strip().split(",")

    sec_1_nums = section1.split("-")
    sec_2_nums = section2.split("-")

    range_1 = range(int(sec_1_nums[0]), int(sec_1_nums[1]) + 1)
    range_2 = range(int(sec_2_nums[0]), int(sec_2_nums[1]) + 1)

    if len(set(range_1).intersection(range_2)) or len(set(range_2).intersection(range_1)) > 0:
        total_in_each_other += 1

print(total_in_each_other)


