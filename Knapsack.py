def knapsack(values, weights, W):
    n = len(values)
    
    # Step 1: Create the DP table with n+1 rows and W+1 columns
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 2: Fill the DP table
    for i in range(1, n + 1):
        current_value = values[i - 1]
        current_weight = weights[i - 1]

        for w in range(1, W + 1):
            if current_weight <= w:
                exclude_item = dp[i - 1][w]
                include_item = current_value + dp[i - 1][w - current_weight]
                dp[i][w] = max(exclude_item, include_item)
            else:
                dp[i][w] = dp[i - 1][w]

    # Step 3: Backtrack to find which items are included
    selected_items = []
    total_value = dp[n][W]
    w = W  # Start from the maximum weight

    for i in range(n, 0, -1):
        # If the value in dp[i][w] is different from dp[i-1][w], item i was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Subtract 1 to get the 0-indexed item
            w -= weights[i - 1]  # Reduce the capacity by the weight of the included item

    # Step 4: Return the maximum value and the selected items
    return total_value, selected_items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

max_value, selected_items = knapsack(values, weights, W)
print(f"Maximum value that can be carried: {max_value}")
print(f"Selected items (0-indexed): {selected_items}")
