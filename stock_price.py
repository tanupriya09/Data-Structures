def stock_price(a):
    profit=0
    for i in range(len(a)):
        if i==len(a)-1:
            return profit
        if a[i]>a[i+1]  :
            i+=1
        else:
            buy = a[i]
            for j in range(i,len(a)):
                if buy>=a[j]:
                    j+=1
                else:
                    sell=a[j]
                    current_profit=sell-buy
                    if current_profit>profit:
                        profit=current_profit
    return profit

arrs = [[7,1,5,3,6,4],[1,2,3,4,5],[5,4,3,2,1],[5,5,5,5],[5],[3,5,7,1,5],[6,9,1,5],[0,0,1,0,0,2],
       [1,2,3,4,1,2,14,63,53,5,3,24,4,42,4,345,42,4,224,3]]
for a in arrs:
    print(stock_price(a))

