import pandas as pd 
import glob
import os 

files = os.path.join("csv_*")
files = glob.glob(files)
files.sort()
print(list(files))

df = pd.concat(map(pd.read_csv,files), ignore_index=True)

