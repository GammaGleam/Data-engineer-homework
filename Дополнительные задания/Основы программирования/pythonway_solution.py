def sum_target(nums, target):
    for index in range(len(nums)):
        first_element = nums[index]
        second_element = target - first_element

        if second_element in nums and index != nums.index(second_element):
            answer = [index, nums.index(second_element)]
            return answer

    # no pair was found
    return None
