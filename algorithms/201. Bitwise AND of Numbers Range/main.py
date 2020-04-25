class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n - m
        end_bits = 0
        while diff > 0:
            end_bits += 1
            n = n >> 1
            m = m >> 1
            diff = diff >> 1
        return (n & m) << end_bits

    def rangeBitwiseAnd1(self, m: int, n: int) -> int:
        while n > m:
            n = n & n - 1
        return n


def test(input, expect, fn):
    result = fn(*input)
    if result != expect:
        print(f"fail, input: {input}, result: {result}, expect: {expect}")


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        [[5, 7], 4],
        [[0, 1], 0],
        [[1, 2], 0],
        [[2, 2], 2],
        [[3, 4], 0],
    ]
    for input, expect in test_cases:
        test(input, expect, s.rangeBitwiseAnd)
    for input, expect in test_cases:
        test(input, expect, s.rangeBitwiseAnd1)
