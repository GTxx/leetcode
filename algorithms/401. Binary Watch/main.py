class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        def all_posible_choose(lst, n):
            if n == 0:
                return [[]]
            elif n == len(lst):
                return [lst]
            elif n > len(lst):
                return []
            else:
                res = []
                new_lst = lst[1:]
                select_i = all_posible_choose(new_lst, n - 1)
                select_i = [[lst[0]] + x for x in select_i]
                res += select_i

                no_select_i = all_posible_choose(new_lst, n)
                res += no_select_i
                return res

        def get_time(lst):
            hour = 0
            minute = 0
            for i in lst:
                if i.endswith(' h'):
                    hour += int(i.split(' h')[0])
                    if hour > 11:
                        return None
                elif i.endswith(' m'):
                    minute += int(i.split(' m')[0])
                    if minute > 59:
                        return None
            return '{}:{:02}'.format(hour, minute)

        time_list = ['8 h', '4 h', '2 h', '1 h',
                     '32 m', '16 m', '8 m', '4 m', '2 m', '1 m']

        possible = all_posible_choose(time_list, num)
        res = []
        for p in possible:
            time = get_time(p)
            if time:
                res.append(time)
        return res


if __name__ == "__main__":
    s = Solution()
    s.readBinaryWatch(0)
    print s.readBinaryWatch(1)
    print s.readBinaryWatch(2)


