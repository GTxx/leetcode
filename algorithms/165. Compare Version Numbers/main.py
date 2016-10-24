class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        sub_version1 = [int(i) for i in version1.split('.')]
        sub_version2 = [int(i) for i in version2.split('.')]
        if len(sub_version1) < len(sub_version2):
            sub_version1 += [0] * (len(sub_version2) - len(sub_version1))
        elif len(sub_version1) > len(sub_version2):
            sub_version2 += [0] * (len(sub_version1) - len(sub_version2))
        if sub_version1 > sub_version2:
            return 1

        elif sub_version1 == sub_version2:
            return 0
        else:
            return -1

        # version1_1, version1_2 = self.split_version(version1)
        # version2_1, version2_2 = self.split_version(version2)
        # comp1 = version1_1 - version2_1
        # comp2 = version1_2 - version2_2
        # if comp1 < 0:
        #     return -1
        # elif comp1 == 0:
        #     if comp2 < 0:
        #         return -1
        #     elif comp2 == 0:
        #         return 0
        #     else:
        #         return 1
        # else:
        #     return 1

    def split_version(self, version):
        if '.' not in version:
            version += '.0'
        return [int(i) for i in version.split('.')]

if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("0.1", '1.1'))
    print(s.compareVersion("1", '0'))
    assert(s.compareVersion("0.1", '0.0.1') == 1)
    assert(s.compareVersion("1.0", '1') == 0)
