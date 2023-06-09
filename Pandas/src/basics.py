import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

web_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [43, 53, 34, 45, 64, 34],
    'Bounce_Rate': [65, 72, 62, 64, 54, 66]
}

df = pd.DataFrame(web_stats)

# print(df)

# print(df['Visitors'])
# print(df.Visitors)

# print(df[['Day', 'Visitors']])

# print(df.Visitors.tolist())

print(np.array(df[['Day', 'Visitors']]))

df = pd.DataFrame(np.array(df[['Day', 'Visitors']]))
print(df)
