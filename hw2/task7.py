def unbounded_knapsack(items, capacity):
    # Необходимо привести веса к целым, чтобы воспользоваться динамическим программированием
    scale_degree = max(
        len(str(weight).split('.')[1]) if '.' in str(weight) else 0
        for weight, _ in items.values()
    )
    scale = 10**scale_degree
    dp = [0] * (int(capacity * scale) + 1)
    items_selected = [{} for _ in range(int(capacity * scale) + 1)]

    for item, (weight, value) in items.items():
        weight_int = int(weight * scale)
        for w in range(weight_int, int(capacity * scale) + 1):
            if dp[w] < dp[w - weight_int] + value:
                dp[w] = dp[w - weight_int] + value
                items_selected[w] = items_selected[w - weight_int].copy()
                items_selected[w][item] = items_selected[w].get(item, 0) + 1

    return dp[int(capacity * scale)], items_selected[int(capacity * scale)]

init_items = {
    "laptop": (3.0, 1500),
    "camera": (1.0, 800),
    "phone": (1.0, 600),
    "watch": (0.5, 300),
    "headphones": (0.2, 200),
    "tablet": (2.0, 900),
    "wallet": (0.1, 100),
}

init_capacity = int(input("Введите размер рюкзака: "))

max_value, selected_items = unbounded_knapsack(init_items, init_capacity)

print(f"Максимальная ценность, которую можно украсть: {max_value}")
print(f"Словарь с выбранными товарами:\n {selected_items}")