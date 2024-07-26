import numpy as np
#find the total revenue
lst1=[500,600,700,550]
lst2=[450,700,800,600]
cat1=np.array(lst1)
cat2=np.array(lst2)
print("total revenue :",cat1+cat2)

#calculate the profit made by a company
rev=np.array([10000,12000,11000,10500])
expenses=np.array([4000,5000,4500,4800])
print("profit:",rev-expenses)

#determine which product in a stor are out of stock(quantity is 0)
inv=np.array([10,0,5,0,20,0])
for i in range(len(inv)):
    if i==0:
        print(np.where(inv==i))

#calculate the total cost of items in a shopping cart
quan=np.array([2,3,4,1])
price_per_item=np.array([10.0,5.0,8.0,12.0])
price=quan*price_per_item
print("total cost of items",price)
