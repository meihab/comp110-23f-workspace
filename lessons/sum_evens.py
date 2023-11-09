"""Practice summing over lists"""

def sum_evens_of_list(input_list: list[int]):
    """Loop over a list a and sum all even elements"""
    sum_total: int = 0
    i: int = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0 :
            sum_total = sum_total + input_list[i]
        i += 1
    return sum_total

print(sum_evens_of_list([1, 2, 3, -2, -3, 0, -9, -8, 4]))