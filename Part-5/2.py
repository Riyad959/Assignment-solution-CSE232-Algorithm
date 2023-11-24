def knapsake(weight, value, cap):
    n = len(weight)
    bag = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(cap + 1):
            if weight[i - 1] > w:
                bag[i][w] = bag[i - 1][w]
            else:bag[i][w] = max(bag[i - 1][w], value[i - 1] + bag[i - 1][w - weight[i - 1]])

    b_num = bag[n][cap]
    knapsake_item = []
    w = cap
    for i in range(n, 0, -1):
        if bag[i][w] != bag[i - 1][w]:
            knapsake_item.append(i - 1)
            w -= weight[i - 1]

    return b_num, knapsake_item

cap = 50
weight = [10, 20, 30]
value = [50, 120, 70]
b_num, item = knapsake(weight, value, cap)
print(f"max value {b_num}")
print(f"item are {item}")