capicity=float(input("ENTER THE  CAPICITY OF THE KNAPSAP/;"));
c=capicity;
n=int(input("ENTER THE NUMBER OF ITEM IN THE POOL:"));
items=[];
price=[];
weight=[];
ratio=[];
for i in range(n):
    items.append(input("input items name:"));
    weight.append(float(input("enter  the weight:")));
    price.append(float(input("enter the price:")));
    ratio.append(price[i]/weight[i]);
choice=int(input("enter 1 for maximun weight, 2 for maximum value, 3 for maximum ratio"));
w=0;
psum=0;
count=0;
while count<n:
    if choice==1:
        mweight=max(weight);
        pos=weight.index(mweight);
    elif choice==2:
        mprice=max(price);
        pos=price.index(mprice);
        mweight=weight[pos];
    else:
        mratio=max(ratio);
        pos=ratio.index(mratio);
        mweight=weight(pos);
    if mweight<=capicity:
        print(items[pos], " inserted into bag");
        psum=psum+price[pos];
        w=mweight+w;
        capicity=capicity-w;
        count=count+1;
    del weight[pos]
    del price[pos];
    del items[pos];
    del ratio[pos];
    if c==w:
          break;
