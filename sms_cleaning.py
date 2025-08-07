import pandas as pd

# Veri setini indir
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_table(url, header=None, names=['label', 'message'])

print("İlk 5 veri:")
print(df.head())
