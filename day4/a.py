assignment_contents = []
with open("input.txt", "r") as assign_file:
    assignment_contents = assign_file.readlines()


total_in_each_other = 0
for assignment in assignment_contents:
    section1, section2 = assignment.strip().split(",")

    sec_1_nums = section1.split("-")
    sec_2_nums = section2.split("-")

    range_1 = set(range(int(sec_1_nums[0]), int(sec_1_nums[1]) + 1))
    range_2 = set(range(int(sec_2_nums[0]), int(sec_2_nums[1]) + 1))

    if range_1.issubset(range_2) or range_2.issubset(range_1):
        total_in_each_other += 1

print(total_in_each_other)

