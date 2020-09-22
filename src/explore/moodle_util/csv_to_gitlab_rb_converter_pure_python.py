"""Read participant list of a Moodle course and convert the email
address "infzyz@hs-worms.de"  to "(uid=infxyz)". Writes output
into the console."""

f = open('../../../tmp/fake_course_members.csv', 'r')
for line in f:
    line_items = line.split(',')
    print('(uid=' + line_items[2].split('@')[0] + ')')
