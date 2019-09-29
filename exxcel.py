import sys
import pandas as pd
import clipboard

filename = str(sys.argv[1])

columnname = str(sys.argv[2])

df = pd.read_excel(filename)
string = ''
for i in df.index:
    if len(df.index)-1 > i:
        string += str("'"+df[columnname][i]+"'"+","+'\n')
    else:
        string += str("'"+df[columnname][i]+"'")

clipboard.copy(string)