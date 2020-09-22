import pandas as pd
import random as rand

MAX_LINES = 10000

name = []
first_name = []
e_mail = []
for n in range(MAX_LINES):
    name.append('Name' + str(rand.randrange(1, 10000)))
    first_name.append('FirstName' + str(rand.randrange(1, 10000)))
    e_mail.append('inf' + str(rand.randrange(1, 100000)) + '@hs-worms.de')

df = pd.DataFrame()
df['First Name'] = first_name
df['Name'] = name
df['Inf E-Mail'] = e_mail

# print(df.head())

# df.to_csv('../../../tmp/fake_course_members.csv', index=None)
df.to_csv('../../../tmp/fake_course_members.csv')
