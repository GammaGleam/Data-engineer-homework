def sum_target_dict(nums, target):
    dict_nums = {}
    for index in range(len(nums)):
        if nums[index] not in dict_nums:
            dict_nums[nums[index]] = [index]
        else:
            value = dict_nums[nums[index]]
            dict_nums[nums[index]] = [value] + [index]

    for index in range(len(nums)):
        first_element = nums[index]
        second_elemet = target - first_element

        if second_elemet in dict_nums:
            value = dict_nums[second_elemet]

            for index_val in value:
                if index != index_val:
                    answer = [index, index_val]
                    return answer
