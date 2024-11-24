import heapq
import copy

N = 4

# State space tree node
class Node:
    def __init__(self, x, y, assigned, parent):
        self.parent = parent
        self.pathCost = 0
        self.cost = 0
        self.workerID = x
        self.jobID = y
        self.assigned = copy.deepcopy(assigned)
        if y != -1:
            self.assigned[y] = True

# Custom heap class with push and pop functions
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

# Function to allocate a new search tree node
# Here Person x is assigned to job y
def new_node(x, y, assigned, parent):
    return Node(x, y, assigned, parent)

# Function to calculate the least promising cost
# of node after worker x is assigned to job y.
def calculate_cost(cost_matrix, x, y, assigned):
    cost = 0

    # to store unavailable jobs
    available = [True] * N

    # start from the next worker
    for i in range(x + 1, N):
        min_val, min_index = float('inf'), -1

        # do for each job
        for j in range(N):
            # if job is unassigned
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
                # store job number
                min_index = j

                # store cost
                min_val = cost_matrix[i][j]

        # add cost of next worker
        cost += min_val

        # job becomes unavailable
        available[min_index] = False

    return cost

# Comparison object to be used to order the heap
class Comp:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.cost > other.node.cost

# Print Assignments
def print_assignments(min_node):
    if min_node.parent is None:
        return

    print_assignments(min_node.parent)
    print("Assign Worker {} to Job {}".format(chr(min_node.workerID + ord('A')), min_node.jobID))

# Finds minimum cost using Branch and Bound
def find_min_cost(cost_matrix):
    # Create a priority queue to store live nodes of the search tree
    pq = CustomHeap()

    # initialize heap to dummy node with cost 0
    assigned = [False] * N
    root = new_node(-1, -1, assigned, None)
    root.pathCost = root.cost = 0
    root.workerID = -1

    # Add dummy node to list of live nodes;
    pq.push(root)

    # Finds a live node with least estimated cost,
    # add its children to the list of live nodes and
    # finally deletes it from the list.
    while True:
        # Find a live node with least estimated cost
        min_node = pq.pop()

        # i stores the next worker
        i = min_node.workerID + 1

        # if all workers are assigned a job
        if i == N:
            print_assignments(min_node)
            return min_node.cost

        # do for each job
        for j in range(N):
            # If unassigned
            if not min_node.assigned[j]:
                # create a new tree node
                child = new_node(i, j, min_node.assigned, min_node)

                # cost for ancestors nodes including the current node
                child.pathCost = min_node.pathCost + cost_matrix[i][j]

                # calculate its lower bound
                child.cost = child.pathCost + calculate_cost(cost_matrix, i, j, child.assigned)

                # Add child to list of live nodes;
                pq.push(child)

# Driver code
if __name__ == "__main__":
    # x-coordinate represents a Worker
    # y-coordinate represents a Job
    cost_matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    # Optimal Cost
    optimal_cost = find_min_cost(cost_matrix)
    if optimal_cost is not None:
        print("\nOptimal Cost is {}".format(optimal_cost))
    else:
        print("\nNo optimal solution found.")