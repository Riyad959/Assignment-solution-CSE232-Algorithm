def bin_packing(items, cap):
    bags = []
    item_num = 1

    for i in range(len(items)):
        item = items[i]
        added_to_bag = False

        for j in range(len(bags)):
            bag = bags[j]
            if bag['weight'] + item <= cap:
                bag['items'].append(item_num)
                bag['weight'] += item
                added_to_bag = True
                break

        if not added_to_bag:
            bags.append({'items': [item_num], 'weight': item})

        item_num += 1

    return bags

items = [4, 8, 1, 4, 2, 1]
cap = 10
result = bin_packing(items, cap)
for i in range(len(result)):
    bag = result[i]
    print(f"bag {i + 1}: Items {bag['items']} (Total Weight: {bag['weight']})")