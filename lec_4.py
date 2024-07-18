# tuple
a = (1,2,6,4,9,2,5)
b = len(a)-1
for index in a:
    print(a[b],end='**')
    b -=1

# dictionary
# dictionary = {'name':'yashika','course':'B.Tech CSE-DS'}
dictionary = {'name':'yashika','course':'B.Tech CSE-DS'}
# insertion 
# if key is already present in the dictionary then the value of the key will get updated
dictionary['college'] = 'ABESIT'
print(dictionary)
dictionary['college'] = 'ABESEC'
print(dictionary)
# retrieve the value
for i in dictionary:
    print(dictionary[i])