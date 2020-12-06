import pandas as pd

df = pd.read_excel (r'C:\Users\admin1\Desktop\final_project\BRIDGE_INFO.xlsx')#loading file into df
data = pd.DataFrame(df, columns= ['PLACE'])#printing the only requirement
a= df.head()
b=df.loc[28]
print(data)
print(a)
print(b)

