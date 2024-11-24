import heapq
import copy

N = 4

# Node class represents each state in the search tree
class Node:
    def __init__(self, x, y, assigned, parent):
        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.studentID = x
        self.clubID = y
        self.assigned = copy.deepcopy(assigned)
        if y != -1:
            self.assigned[y] = True

# Custom heap to store and retrieve nodes based on their cost
class CustomHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.cost, node))

    def pop(self):
        if self.heap:
            _, node = heapq.heappop(self.heap)
            return node
        return None

# Create a new node
def new_node(x, y, assigned, parent):
    return Node(x, y, assigned, parent)

# Calculate the cost of completing the assignment after assigning student x to club y
def calculate_cost(cost_matrix, x, y, assigned):
    cost = 0
    available = [True] * N
    for i in range(x + 1, N):
        min_val, min_index = float('inf'), -1
        for j in range(N):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
                min_index = j
                min_val = cost_matrix[i][j]
        cost += min_val
        available[min_index] = False
    return cost

# Comparison function for heap (priority queue)
class Comp:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.cost > other.node.cost

# Function to print the assignments made in the optimal solution
def print_assignments(min_node):
    if min_node.parent is None:
        return
    print_assignments(min_node.parent)
    print(f"Assign Student {chr(min_node.studentID + ord('A'))} to Club {min_node.clubID}")

# Function to find the minimum cost assignment
def find_min_cost(cost_matrix):
    pq = CustomHeap()
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.studentID = -1
    pq.push(root)

    while True:
        min_node = pq.pop()
        if min_node is None:
            return None  # No solution found
        
        i = min_node.studentID + 1
        if i == N:
            print_assignments(min_node)
            return min_node.cost
        
        # Generate children nodes for the next student assignment
        for j in range(N):
            if not min_node.assigned[j]:
                child = new_node(i, j, min_node.assigned, min_node)
                child.pathCost = min_node.pathCost + cost_matrix[i][j]
                child.cost = child.pathCost + calculate_cost(cost_matrix, i, j, child.assigned)
                pq.push(child)

if __name__ == "__main__":
    # Example cost matrix
    cost_matrix = [
        [9, 6, 7, 8],
        [6, 4, 2, 7],
        [5, 8, 10, 8],
        [7, 2, 9, 10]
    ]
    
    optimal_cost = find_min_cost(cost_matrix)
    
    if optimal_cost is not None:
        print(f"\nOptimal Cost is {optimal_cost}")
    else:
        print("\nNo optimal solution found.")
