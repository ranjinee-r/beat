#Import pandas as pd.
import pandas as pd

#Read Salaries.csv as a dataframe called sal.
sal=pd.read_csv(r"C:\Users\lenov\OneDrive\Desktop\Beat\python\Notes\pandas_exercise\Salaries.csv")
sal

#Check the head of the DataFrame.
sal.head()

#Use the .info() method to find out how many entries there are.
sal.info()

#What is the average BasePay ?
sal["BasePay"].mean()

#What is the highest amount of OvertimePay in the dataset ? 
sal["OvertimePay"].max()

#What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). 
'''new_sal=sal[["EmployeeName","JobTitle"]]
new_sal1=new_sal.set_index("EmployeeName")
new_sal1.loc["JOSEPH DRISCOLL"] '''

sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]

#How much does JOSEPH DRISCOLL make (including benefits)? 
#sal[["EmployeeName","TotalPayBenefits"]].set_index("EmployeeName").loc["JOSEPH DRISCOLL"]
sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"]

#What is the name of highest paid person (including benefits)?
"""sal1=sal.set_index("TotalPayBenefits")
maximum=sal["TotalPayBenefits"].max()
sal1.loc[maximum] """

sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()]

#What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
"""sal1=sal.set_index("TotalPayBenefits")
minimum=sal["TotalPayBenefits"].min()
sal1.loc[minimum] """

sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()]

#What was the average (mean) BasePay of all employees per year? (2011-2014) ?
sal1=sal.groupby("Year")
sal1["BasePay"].mean()

#How many unique job titles are there?
sal["JobTitle"].nunique()

#What are the top 5 most common jobs?
sal["JobTitle"].value_counts().head() #d

#How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
sal1=sal[sal["Year"]==2013]["JobTitle"].value_counts().to_frame()
sal1
sal1[sal1["count"]==1].count()

#How many people have the word Chief in their job title? (This is pretty tricky)
sal.info()
def chief(a):
    if "Chief" in a:
        return a
sal["JobTitle"].apply(chief).count()

#Bonus: Is there a correlation between length of the Job Title string and Salary?
sal["length"]=sal['JobTitle'].apply(len)
sal[['length','TotalPayBenefits']].corr()
