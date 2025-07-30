import numpy as np
import pandas as pd
dir(pd)
type(pd)

#Series
labels = ['a','b','c']
my_list = [10,20,30]
b=pd.Series(data=my_list)
b
b[1]

a=pd.Series(data=my_list,index=labels)
a
a['a']

arr = np.array([10,20,30])
pd.Series(arr)

d = {'a':10,'b':20,'c':30}
pd.Series(d)

pd.Series(data=labels)
pd.Series([sum,print,len])

ser1 = pd.Series(data=[1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']) 
ser1
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
ser2
ser1+ser1

ser3 = pd.Series(data=[1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']) 
ser3
ser1
ser1+ser3

ser1['USA']

fruits1=pd.Series([10,20,30,40],["Apple","Mango","Watermelon","Banana"])
fruits1

fruits2=pd.Series(data=[25,10,42,70,80],index=["Mango","Papaya","Kiwi","Banana","Apple"])
fruits2

data1=[40,50,5,34,20,10,65]
index1=["Watermelon","Papaya","Kiwi","Cherry","Mango","Apple","Grapes"]
fruits3=pd.Series(data1,index1)
fruits3

fruits=fruits1+fruits2+fruits3
fruits

#DataFrames
from numpy.random import randint
np.random.seed(101)
a=randint(1,100,9).reshape(3,3)
a
df=pd.DataFrame(data=a,index=["A","B","C"],columns=["X","Y","Z"])
df
dir(df)
df.index.name="Index"
df

df['X']
df.loc['A']
df.iloc[1]
df.X
detail=[["Ranjinee","Nahva","Nadiya","Kamaru"],[21,22,22,21],["Female","Female","Female","Female"]]
df=pd.DataFrame(detail)
df

d=[["Ranjinee",21,"F"],["Nahva",22,"F"],["Nadiya",22,"F"],["Kamaru",21,"F"]]
df=pd.DataFrame(d,index=[1,2,3,4],columns=["Names","Age","Gender"])
df
df.index

details={"First_Name":["Ranjinee","Nahva","Shijas","Nadiya","Nafeesathul"],"Last_Name":["R","C","U","K P","Kamaru"],"Age":[21,22,22,22,21],"Gender":["Female","Female","Male","Female","Female"]}
df=pd.DataFrame(details)
df
df["Names"]=df["First_Name"]+" "+df["Last_Name"]
df
df[["First_Name","Last_Name","Names","Age","Gender"]]

df.drop("Gender",axis=1,inplace=True)
df.drop(2,axis=0,inplace=True)
df
df.reset_index()
df
df.reset_index(inplace=True)
ind=[1,2,3,4]
df['Index']=ind
df
df.set_index("Index")
df
df.set_index("Index",inplace=True)
df

out=["CSE","CSE","CSE","CSE","CSE","CE","CE","IT","IT","IT"]
inside=[1,2,3,4,5,1,2,1,2,3]
multi_index=pd.MultiIndex.from_tuples(zip(out,inside))
multi_index
d={"Names":["Ranjinee","Nahva","Mittu","Nadiya","Nishal","Kamaru","Shahma","Shafinaz","Harsha","Shahana"],"Maths":[75,71,66,69,72,70,85,81,73,83],"Science":[83,73,81,85,70,72,69,66,71,75]}
marklist=pd.DataFrame(d,index=multi_index)
marklist
marklist["GK"]=0
marklist
marklist.drop("GK",axis=1,inplace=True)


marklist.loc[[("CSE",2),("CE",2),("IT",2)]]
marklist.loc["CSE"].loc[[2,3],["Names","Maths"]]
marklist.loc["CSE"].loc[[2,3]]
marklist.loc["CSE"].loc[[4,5]]
marklist[(marklist["Maths"]>50) & (marklist["Science"]>70)]
marklist[(marklist["Maths"]>50) & (marklist["Science"]>70)]["Names"]
marklist.loc["CSE"].loc[[2,3],["Maths","Science"]]
marklist.index.names=["Department","Roll_No"]
marklist

marklist.xs("CSE")
marklist.xs(("CSE",2))
marklist.xs(1,level="Roll_No")

new_df=pd.DataFrame(randint(1,100,30).reshape(6,5),index="R1 R2 R3 R4 R5 R6".split(),columns="C1 C2 C3 C4 C5".split())
new_df
result=new_df[new_df>40]
result
result.dropna(thresh=3)
result.dropna(inplace=True)
result.fillna(value=0,inplace=True,axis=1)
result
result[["C4"]].fillna(value=result[["C4"]].mean())
result[["C1","C2","C3","C4","C5"]].fillna(value=result[["C1","C2","C3","C4","C5"]].mean())


d={"Departments":["CSE","CSE","CE","IT","CSE","IT","CE","CE","IT","CSE"],"Name":["Ranjinee","Nahva","Mittu","Nishal","Nadiya","kamaru","Shafinaz","Shahma","Harsha","Shahana"],"Total_Marks":[250,261,260,219,230,225,190,211,200,208]}
dep_details=pd.DataFrame(d)
dep_details
dep=dep_details.groupby("Departments")
dir(dep)
dep.sum(numeric_only=True)
dep.mean(numeric_only=True)
dep.median(numeric_only=True)
dep.std(numeric_only=True)
dep.count()
dep.describe()
dep.describe().transpose()
dep.describe().transpose()["CSE"]
dep.describe().loc["CSE"]


table_1={"A":["A0","A1","A2"],"B":["B0","B1","B2"]}
table_2={"C":["C0","C1","C2"],"D":["D1","D2","D3"]}
table_3={"E":["E0","E1","E2"],"F":["F1","F2","F3"]}
df_1=pd.DataFrame(table_1)
df_2=pd.DataFrame(table_2)
df_3=pd.DataFrame(table_3)
pd.concat([df_1,df_2,df_3])
pd.concat([df_1,df_2,df_3],axis=1)

left=pd.DataFrame({"Key_1":["K1","K0","K0","K2"],"Key_2":["K0","K2","K1","K0"],"A":["A0","A1","A0","A2"],"B":["B1","B0","B4","B2"]})
right=pd.DataFrame({"Key_1":["K0","K1","K0","K2"],"Key_2":["K1","K2","K1","K0"],"C":["C2","C1","C0","C2"],"D":["D2","D3","D2","D2"]})
left
right
pd.merge(left,right,how="inner",on=["Key_1","Key_2"])
pd.merge(left,right,how="outer",on=["Key_1","Key_2"])
pd.merge(left,right,how="left",on=["Key_1","Key_2"])
pd.merge(left,right,how="right",on=["Key_1","Key_2"])

right.join(left,on=["Key_1","Key_2"])
right.join(left,how="outer")




d={"Departments":["CSE","CSE","CE","IT","CSE","IT","CE","CE","IT","CSE"],"Name":["Ranjinee","Nahva","Mittu","Nishal","Nadiya","kamaru","Shafinaz","Shahma","Harsha","Shahana"],"Total_Marks":[250,261,260,219,230,225,190,211,200,208]}
dep_details=pd.DataFrame(d)
dep_details
dep_details.head(6)
dep_details.tail(2)
dep_details.info()
dep_details["Departments"].unique()
dep_details["Departments"].nunique()
dep_details["Departments"].value_counts()

def upp(name):
    name=name.upper()
    return name

dep_details["Name"].apply(upp)
dep_details["Total_Marks"].sum()
dep_details["Total_Marks"].max()
dep_details["Total_Marks"].min()
dep_details["Name"].apply(len)
dep_details.columns
dep_details.index
dep_details.sort_values(by="Total_Marks")

new_df=pd.DataFrame(randint(1,100,30).reshape(6,5),index="R1 R2 R3 R4 R5 R6".split(),columns="C1 C2 C3 C4 C5".split())
new_df
result=new_df[new_df>40]
result
result.isnull()
result.isnull().sum()

df1=pd.read_csv("C:\\Users\\lenov\\Downloads\\example1 (1).csv")
df1
df2=pd.read_csv(r"C:\Users\lenov\Downloads\example1 (1).csv")
df2
df3=pd.read_csv("C:/Users/lenov/Downloads/example1 (1).csv")
df3

d={"Departments":["CSE","CSE","CE","IT","CSE","IT","CE","CE","IT","CSE"],"Name":["Ranjinee","Nahva","Mittu","Nishal","Nadiya","kamaru","Shafinaz","Shahma","Harsha","Shahana"],"Total_Marks":[250,261,260,219,230,225,190,211,200,208]}
dep_details=pd.DataFrame(d)
dep_details.to_csv("department.csv",index=False)
import os
os.getcwd()

pd.read_csv("department.csv")

df4=pd.read_excel(r"C:\Users\lenov\Downloads\Excel_Sample (1).xlsx",sheet_name="Sheet1")
df4
dep_details.to_excel("Sample.xlsx",sheet_name="Sheet1",index=False)

df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
df

