def knapsack(weights, values, capacity):
    n = len(weights)
    bag = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            current_weight, current_value = weights[i - 1], values[i - 1]
            
            without_current_item = bag[i - 1][w]
            with_current_item = bag[i - 1][w - current_weight] + current_value if current_weight <= w else 0
            bag[i][w] = max(with_current_item, without_current_item)
    return bag[n][capacity]

weights = [2, 1, 4, 3]
values = [3, 1, 5, 6]
capacity = 8
max_value = knapsack(weights, values, capacity)
print(f"maximum value can store {max_value}")