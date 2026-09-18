numbers = [1, 5, 2, 9, 2, 9, 1]

def unique_by_count(arr):
    for number in arr:
        if arr.count(number) == 1:
            return number
    return None

print("число:", unique_by_count(numbers))