new = {0:'apple',1:'mango',2:'banana',3:'orange'}
# dict_name.pop() --- deletes value of specified key
new.pop(0)
print(new)
# dict_name.popitem() --- deletes last key value pair
new.popitem()
print(new)
# dict_name.keys() return all the keys of the dictionary
print(new.keys())
# dict_name.values()  return all the values of the dictionary
print(new.values())
# dict_name.items()   --- returns a list of items in form of tuple
print(new.items())

# clear()
# print(new.clear())
# print(new)
# copy() ---- copy 1 dict. to another dict
r = new.copy()
print(r)

# fromkeys()   -----return the dict 

ne = dict.fromkeys('help',89)
print(ne)
# get()
# update()   --- we can use this to add anothere dict. to the existing dictionary
d = {4:'lichi',5:'strawberry'}
new.update(d)
print(new)
