from typing import List


def product_of_all_other_items(nums: List[int]) -> List[int]:
    """given a list of integers, return a new list such that
    the element at index i of the new list is the product of
    all the numbers in the given list except the one at i

    without using division
    """

    # product of all numbers up to the nth include n.
    prefix_products = []

    for num in nums:
        if not prefix_products:
            prefix_products.append(num)
        else:
            prefix_products.append(prefix_products[-1] * num)

    # products of all numbers after nth
    suffix_products = []
    for num in reversed(nums):
        if not suffix_products:
            suffix_products.append(num)
        else:
            suffix_products.append(suffix_products[-1] * num)
    suffix_products = list(reversed(suffix_products))

    result = []
    for n in range(len(nums)):
        if n == 0:
            result.append(suffix_products[n + 1])
        elif n == len(nums) - 1:
            result.append(prefix_products[n - 1])
        else:
            result.append(prefix_products[n - 1] * suffix_products[n + 1])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    product_of_all_other_items(nums)
