import csv
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn
# %matplotlib inline

# Shanghai_data = pd.read_csv('ShanghaiPM20100101_20151231.csv')

# Shanghai_data.head()



with open('ShanghaiPM20100101_20151231.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(texts[1])