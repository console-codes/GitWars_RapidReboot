def process():
    nums = [1, 2, 3, 4]
    for x in nums:
        if x % 2 == 0:
            nums.remove(x)
    print(nums)

process()
