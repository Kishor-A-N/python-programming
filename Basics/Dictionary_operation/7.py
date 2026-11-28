dates={  
       "a":"28-05-2006",
       "b":"09-10-2006"}
print(dates) #accessing
print(dates.get("c","not found"))
dates["d"]="28-06-2006" #add
dates["a"]="28-05-2005" #update
print(dates)
print(dates.keys())
print(dates.values())
item1={
    "name":"milk",
    "weigth":1,
    "price":49
}
item2={
    "name":"suger",
    "weigth":3,
    "price":90.8
}
item=[item1,item2]
print(item)
print(f"total weigth:{item1["weigth"]+item2["weigth"]}kg")