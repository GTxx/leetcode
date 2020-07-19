from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        if len(A) == 0:
            return True
        A.sort()
        num_cnt_list = [[A[0], 1]]
        for a in A[1:]:
            if num_cnt_list[-1][0] == a:
                num_cnt_list[-1][1] += 1
            else:
                num_cnt_list.append([a, 1])
        num_idx_dict = {}
        for idx, (num, cnt) in enumerate(num_cnt_list):
            num_idx_dict[num] = idx
        for i in range(len(num_cnt_list)):
            num, cnt = num_cnt_list[i]
            if cnt == 0:
                continue
            double_num = num * 2 if num >= 0 else num /2
            if double_num not in num_idx_dict:
                return False
            double_idx = num_idx_dict[double_num]
            if num_cnt_list[double_idx][1] < cnt:
                return False
            num_cnt_list[double_idx][1] -= cnt
        return True
