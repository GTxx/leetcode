from typing import List


class Solution:
    def extract(self, name: str) -> (str, int):
        num_s = []
        if name.endswith(")"):
            idx = len(name) - 1
            find_suffix_num = False
            while True:
                if name[idx] == ")":
                    idx -= 1
                    continue
                if name[idx] == "(":
                    find_suffix_num = True
                    break
                else:
                    if not name[idx].isdigit():
                        break
                    else:
                        num_s.append(name[idx])
                        idx -= 1
            if find_suffix_num:
                return name[:idx], int("".join(reversed(num_s)))
        return name, None

    def get_next_num(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if num == 0:
                return idx
        return len(nums)

    def insert_num(self, nums: List[int], num: int):
        if num < len(nums):
            nums[num] = 1
        else:
            for _ in range(num-len(nums)):
                nums.append(0)
            nums.append(1)

    def getFolderNames(self, names: List[str]) -> List[str]:
        prefix_nums = {}
        assigned_name = set()
        res = []
        for name in names:
            if name in assigned_name:
                # update prefx_nums
                nums = prefix_nums[name]
                next_num = self.get_next_num(nums)
                self.insert_num(nums, next_num)
                prefix_nums[name] = nums
                #
                new_name = name + "(" + str(next_num) + ")"
                assigned_name.add(new_name)
                # update prefix_nums for new name
                new_name_nums = prefix_nums.get(new_name, [])
                self.insert_num(new_name_nums, 0)
                prefix_nums[new_name] = new_name_nums
                #
                res.append(new_name)
            else:
                assigned_name.add(name)
                nums = prefix_nums.get(name, [])
                self.insert_num(nums, 0)
                prefix_nums[name] = nums
                res.append(name)
                pre_name, num = self.extract(name)
                if num and pre_name:
                    next_num = num
                    nums = prefix_nums.get(pre_name, [])
                    self.insert_num(nums, next_num)
                    prefix_nums[pre_name] = nums
        return res

