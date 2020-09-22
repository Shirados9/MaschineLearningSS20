import pandas as pd

df = pd.read_csv('../../../tmp/courseid_1594_participants_ml.csv')
# df = pd.read_csv('../../../tmp/courseid_1994_participants_fpk.csv')

# print(df.head())

for index, email in df['E-Mail-Adresse'].iteritems():
    # print(index, email)
    infxyz = email.split('@')[0]
    print('(uid=' + infxyz + ')')