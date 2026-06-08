from functools import cmp_to_key


def largest_number(nums):
    num_str = list(map(str, nums))

    # custom comparator: sort based on which combination is greater
    def compare(x, y):
        if x + y > y + x:
            return -1  # x should come before y
        elif x + y < y + x:
            return 1  # y should come before x
        else:
            return 0  # order doesn't matter

    num_str.sort(key=cmp_to_key(compare))

    # edge case: if the largest number is "0" return "0"
    if num_str[0] == "0":
        return "0"

    return "".join(num_str)


nums = [3, 30, 34, 5, 9]
print(largest_number(nums))
