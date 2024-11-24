def knapsack(wt, val, W, n, t):

    if n == 0 or W == 0:  
        return 0

    if t[n][W] != -1:
        return t[n][W]
    
    if wt[n-1] <= W:  

        t[n][W] = max(
            val[n-1] + knapsack(wt, val, W-wt[n-1], n-1, t),  
            knapsack(wt, val, W, n-1, t)  
        )
    else:
        t[n][W] = knapsack(wt, val, W, n-1, t)
    
    return t[n][W] 

def menu():
    print("\nKnapsack Problem Solver")
    print("1. Input items and capacity")
    print("2. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            
            n = int(input("Enter the number of items: "))
            profit = []   # to store values and weights
            weight = []
            
            # Input values and weights for each item
            for i in range(n):
                val = int(input(f"Enter value of item {i+1}: "))
                wt = int(input(f"Enter weight of item {i+1}: "))
                profit.append(val)
                weight.append(wt)
            
            W = int(input("Enter the maximum weight capacity of the knapsack: "))
            
            # Initialize the memoization table with -1
            t = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
            
            max_profit = knapsack(weight, profit, W, n, t)  # Calls the knapsack() function
            print(f"The maximum profit is: {max_profit}")
        
        elif choice == '2':
            print("Exit!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()