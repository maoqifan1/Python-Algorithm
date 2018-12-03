# graph
graph = dict()
graph["you"] = ["alice", "bob", "claire"]

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}
# cost form 
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# hash map which is used to save parent nodes 
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
# a array which is used to record the node that have been processed
processed = []

# a function which is used to find the lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

if __name__ == "__main__":
    node  = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if cost[n] > new_cost:
                cost[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)