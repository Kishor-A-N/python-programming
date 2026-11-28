cities={
    "mysuru":"mysuru pak",
    "bengaluru":"coffee",
    "tumkuru":"chikken",
    "davanagere":"benne dose",
    "mangalore":"fish kabab"
}
print(cities)
cities["dharwad"]="peda"
cities["bengaluru"]="tea"

del cities["mangalore"]
print(cities)
print(cities.keys())
print(cities.values())
frind1={
    "name":"hithes",
    "subject":"maths",
    "food":"uppitu"
}
frind2={ 
        "name":"chiru",
        "subject":"kannada",
        "food":"chikken"
        }
frinds=[frind1,frind2]
print(frinds)
print("favorite food:"+frind1["food"])
print(f"favorite food: {frind1["food"]}")