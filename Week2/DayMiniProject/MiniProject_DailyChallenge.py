import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
list_of_pairs =[]
target_number   = 3728

for number in list_of_numbers:
    if target_number-number in list_of_numbers:
        pair = [min(number,target_number - number),max(number,target_number-number)]
        if [target_number-number, number] not in list_of_pairs:
            list_of_pairs.append(pair)

for a, b in list_of_pairs:
    print(f'{a} and {b} sums to the {target_number}')