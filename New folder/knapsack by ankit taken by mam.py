capacity=float(input("Enter the size of the knapsack :"));
n=int(input("Enter no. of items in knapsack:"));
items=[]
price=[]
weight=[]
ratio=[]
c=capacity;
for i in range(n):
    items.append(input("Enter items name: "));
    weight.append(int(input("Enter weight: ")));
    price.append(int(input("Enter price: ")));
    ratio.append(price[i]/weight[i]);
choice=int(input("Enter 1 for max weight, 2 for max price,3 for maximum ratio: "))

w=0
psum=0
count=0
while count<n:
    if choice==1:
        mweight=max(weight)
        pos=weight.index(mweight)
    elif choice==2:
        mprice=max(price);
        pos=price.index(mprice);
        mweight=weight[pos];
    else:
        mratio=max(ratio);
        pos=ratio.index(mratio);
        mweight=weight(pos);
    if mweight<=capacity:
        print(items[pos],"inserted into bag")
        psum=psum+price[pos]
        w=mweight+w
        capacity=capacity-w
        count=count+1
    del weight[pos]
    del price[pos]
    del items[pos]
    del ratio[pos]
    if c==w:
        break;







