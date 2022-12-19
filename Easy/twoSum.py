def twoSum(nums, target):

    for i in range(len(nums)):
        another = target - nums[i]
        if another in nums:
            try:
                j = nums.index(another)
                if i != j:
                    return [i, j]
            except ValueError as e:
                # There has no item in list
                continue
    return []


def main ():
    nums = [2,7,11,15]
    target = 9

    print(twoSum(nums, target))

if __name__ == '__main__':
    main()
    print("hi")