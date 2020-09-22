f = open("../../../tmp/fake_course_members.csv", "r")
for line in f:
    # print(line)
    line_items = line.split(',')
    # print(line_items)
    email = line_items[2]
    inf_part = email.split('@')[0]
    print('(uid=' + inf_part + ')')
