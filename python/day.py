fav_day=input("Enter your fav day: ")
count=0
today=input("Enter today: ")
days_left=int(input("How many days list: "))
days=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
index_of_today=days.index(today)
for i in range(0,days_left):
    x=(index_of_today+i)%7
    if days[x]==fav_day:
        count+=1
count


