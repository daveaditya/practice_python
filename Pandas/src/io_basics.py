import pandas as pd

file_path = '../resources/ZILL-Z77006_MLP.csv'

df = pd.read_csv(file_path)

df.set_index('Date', inplace=True)

df.to_csv('../resources/newcsv2.csv')

print(df.head())

# df.columns = ['Austin_HPI']
#
# print(df.head())

df.rename(columns={'Value': 'Austin_HPI'}, inplace=True)

print(df.head())
