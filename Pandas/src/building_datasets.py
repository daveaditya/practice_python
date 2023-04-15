import quandl as Quandl
import pandas as pd

#
# api_key = open('../resources/quandl.txt').read()
#
# df = Quandl.get('FMAC/HPI_AK', authtoken=api_key)
#
# print(df.head())


fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# this is a list of dataframes
# print(type(fiddy_states[0]))

# this is the column of state abbreviations
# print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print('FMAC/HPI_' + abbv)
