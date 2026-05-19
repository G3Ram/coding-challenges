"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique. The result can be in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]  (or [4,9])
"""

# Solution


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    if not nums1 or not nums2:
        return []
    nums1 = sorted(set(nums1))
    nums2 = sorted(set(nums2))
    i = j = 0
    n1 = len(nums1)
    n2 = len(nums2)
    result =[]
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))        # expected: [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # expected: [9,4] or [4,9]
    print(intersection([1, 2, 3], [4, 5, 6]))         # expected: []
    print(intersection([4,7,9,7,6,7], [5,0,0,6,1,6,2,2,4]))
