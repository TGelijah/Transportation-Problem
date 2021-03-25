import numpy


 ## Determine if the model is balance,
 # is supply == demand
def get_balanced_tp(supply, demand, costs):
    total_supply = sum(supply)
    total_demand = sum(demand)
    
    if total_supply < total_demand:
        new_supply = supply + [total_demand - total_supply]
        new_costs = costs
        return new_supply, demand, new_costs
    if total_supply > total_demand:
        new_demand = demand + [total_supply - total_demand]
        new_costs = costs + [[0 for _ in demand]]
        return supply, new_demand, new_costs
    return supply, demand, costs


supply = [120, 80, 60]
demand = [150, 70, 40]
costs = [
    [8, 5, 6],
    [15, 10, 12],
    [3, 9, 10]
]
get_balanced_tp(supply, demand, costs)

## Northwest Corner Method
def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
    return bfs

supply = [120, 80, 60]
demand = [150, 70, 40]
bfs = north_west_corner(supply, demand)
print(bfs)

