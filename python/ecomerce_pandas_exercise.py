#Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom.
import pandas as pd
ecom=pd.read_csv(r"C:\Users\lenov\OneDrive\Desktop\Beat\python\Notes\pandas_exercise\Ecommerce Purchases.csv")

#Check the head of the DataFrame.
ecom.head()

#How many rows and columns are there? 
ecom.info()

#What is the average Purchase Price? 
ecom["Purchase Price"].mean()

#What were the highest and lowest purchase prices?
ecom["Purchase Price"].max()
ecom["Purchase Price"].min()

#How many people have English 'en' as their Language of choice on the website?
'''ecom1=ecom.groupby("Language")
ecom1.count().loc["en"]
ecom["Language"].value_counts().loc["en"]'''

ecom[ecom["Language"]=="en"].count()

#How many people have the job title of "Lawyer"?

"""ecom1=ecom.groupby("Job")
ecom1.count().loc["Lawyer"] """

ecom[ecom["Job"]=="Lawyer"].info()

#How many people made the purchase during the AM and how many people made the purchase during PM ?
ecom["AM or PM"].value_counts() #d

#What are the 5 most common Job Titles?
ecom["Job"].value_counts().head() #d

#Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
#ecom[["Lot","Purchase Price"]].set_index("Lot").loc["90 WT"]
ecom[ecom["Lot"]=="90 WT"]["Purchase Price"]

#What is the email of the person with the following Credit Card Number: 4926535242672853
#ecom[["Credit Card","Email"]].set_index("Credit Card").loc[4926535242672853] 
ecom[ecom["Credit Card"]==4926535242672853]["Email"]

#How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?
new_ecom=ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)]
new_ecom

#Hard: How many people have a credit card that expires in 2025?
def exp_date(a):
    if "25" in a:
        return a
ecom["CC Exp Date"].apply(exp_date).count()

sum(ecom["CC Exp Date"].apply(lambda a:a[3:])=='25')

#Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
def providers(a):
    b=a.split("@")
    return b[1]
ecom["Email"].apply(providers).value_counts().head()


