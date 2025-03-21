prices = [0,3,8,6,8,6,6,8,2,0,2,7]


output=0
max_price=max(prices)
for i in range(len(prices)-1):
    
    if prices[i]>output:
        max_price = max(prices[i+1:])
    if prices[i] < max_price and max_price - prices[i] > output:
        output = max_price - prices[i]  

print(output)

    
