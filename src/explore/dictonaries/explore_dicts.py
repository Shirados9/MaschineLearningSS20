thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
print(type(thisdict.values()))
print(thisdict.values())

values = thisdict.values()
for x in thisdict.values():
    print(x)
