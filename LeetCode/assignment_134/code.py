def gas_station(gas, cost):
    total_energy = 0 
    cur_energy = 0
    start = 0
    for i in range(len(gas)):
        total_energy += gas[i] - cost[i]
        cur_energy += gas[i] - cost[i]
        if cur_energy < 0: 
            start = i + 1
            cur_energy = 0
    return start if total_energy >= 0 else -1

def gas_station(gas, cost): 
    if sum(cost) > sum(gas): 
        return -1 
    
    tank = start = 0 
    for i in range(len(gas)): 
        tank += gas[i] - cost[i]
        if tank < 0: 
            tank = 0 
            start = i + 1
    return start 

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gas_station(gas, cost))
