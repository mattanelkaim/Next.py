from itertools import combinations

"""
There are bills, value=quantity:
20$=3, 10$=5, 5$=2, 1$=5
Find all combinations to get 100$ (without duplicates)
"""
TARGET_VALUE = 100
BILLS = {
    1: 5,
    5: 2,
    10: 5,
    20: 3
}


# Append the x y times, where y is the value and x is the key
values = [x for x, y in BILLS.items() for _ in range(y)]

possible_combs = []
possible_options = 0  # Counter

for i in range(1, len(values) + 1):
    current_comb = set(combinations(values, i))

    for comb in current_comb:
        if sum(comb) == TARGET_VALUE:
            possible_combs.append(comb)
            possible_options += 1

print(f"Total of {possible_options} combinations to get ${TARGET_VALUE}:")
for i in possible_combs:
    print(i)
