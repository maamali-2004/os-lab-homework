def maxprofit(lst):
    buy = lst[0]
    max_profit = 0
    for i in range(1, len(lst)):         # min
        if lst[i] <  buy:
            buy = lst[i]
        max_profit = max(max_profit, lst[i] - buy)
    return max_profit
lst = [6, 5, 4, 1, 7, 8, 10] 
print(maxprofit(lst))

