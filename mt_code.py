import pandas as pd
import os


data = {'name': ['Alice','Bob','Charile','SaiNEHA'],
        'Age':[25,30,35,40],
        'city':['NA','LA','CHICAGO','Hyderbad']
}

df = pd.DataFrame(data)


# adding a now row to df for vz SaiNehamehta
new_row_loc = {'name': 'SaiNehamehta','age':30, 'city':"hyd"}
df.loc[len(df.index)] = new_row_loc

new_row_loc2= {'name': 'SaiNehamehta','age':30, 'city':"hyd","Status":"Both almost same and good friends sai marry a similar girl as life parnter"}
df.loc[len(df.index)] = new_row_loc2

data_dir = 'data'

os.makedirs(data_dir,exist_ok=True)


filepath = os.path.join(data_dir,'Sample_csv')

df.to_csv(filepath,index=False)

print(f"CSV FILE Saved To {filepath}")