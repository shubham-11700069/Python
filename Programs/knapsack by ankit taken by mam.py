capacity=float(input("Enter the size of the knapsack"));
n=int(input("Enter no. of items in pool:"));
items=[]
price=[]
weight=[]
ratio=[]
for i in range(n):
    items.append(input("Enter items name: "));
    weight.append(input("Enter weight: "));
    price.append(input("Enter price: "));
    ratio.append(price[i]/weight[i]);
choice=int(input("Enter 1 for maximum, 2 for max value,3 for maximum ratio: "))

w=0,psum=0
if choice==1:
    while w<=capacity:
        mweight=max(weight)
        pos=weight.index(mweight)
        if mweight<=capacity:
            print(item[pos],"inserted into bag")
            psum=psum+price[pos]
            weight.remove(pos)
            price.remove(pos)
            item.remove(pos)
            w=mweight
            capacity=capacity-w
        else:
            break






