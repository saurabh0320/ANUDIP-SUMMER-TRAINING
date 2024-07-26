import numpy as np
my_lst=[1,2,3,4,5]
ar=np.array(my_lst)
print("first element is :",ar[0])
print("last element is :",ar[-1])
arr=np.zeros(10,dtype='int')
print(arr)
arr_1=np.ones(10,dtype='int')
print(arr_1)
arr_2=np.ones(10,dtype='int')*5
print(arr_2)
arr_3=np.arange(2,11).reshape(3,3)
print(arr_3)

