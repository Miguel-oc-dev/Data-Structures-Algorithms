def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def two_pointers_example(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Lógica que depende del problema
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
