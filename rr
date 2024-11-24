def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1)
        )


n = int(input("Enter the number of items: "))

print("Enter the values (profits) of the items separated by commas:")
val = list(map(int, input().split(',')))

print("Enter the weights of the items separated by commas:")
wt = list(map(int, input().split(',')))

W = int(input("Enter the capacity of the knapsack: "))

max_profit = knapSack(W, wt, val, n)
print(f"The maximum profit is: {max_profit}")
