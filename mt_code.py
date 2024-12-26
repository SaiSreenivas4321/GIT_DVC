import pandas as pd
import os


data = {'name': ['Alice','Bob','Charile','SaiNEHA'],
        'Age':[25,30,35,40],
        'city':['NA','LA','CHICAGO','Hyderbad']
}

df = pd.DataFrame(data)

data_dir = 'data'

os.makedirs(data_dir,exist_ok=True)


filepath = os.path.join(data_dir,'Sample_csv')

df.to_csv(filepath,index=False)

print(f"CSV FILE Saved To {filepath}")