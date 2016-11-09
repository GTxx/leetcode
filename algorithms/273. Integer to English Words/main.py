class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit_aph = {
            0: "Zero", 1: "One", 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: "Twelve", 13: "Thirteen", 14: "Fourteeg",
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
            100: 'Hundred', 1000: 'Thousand', 1000000: 'Million',
            1000000000: 'Billion'
        }
        res = ""
        if num == 0:
            return 'Zero'
        if 1000000000 <= num:
            res += " " + self.numberToWords(num/1000000000) + ' Billion'
            num = num % 1000000000
        if 1000000 <= num < 1000000000:
            res += " " + self.numberToWords(num/1000000) + ' Million'
            num = num % 1000000
        if 1000 <= num < 1000000:
            res += " " + self.numberToWords(num/1000) + ' Thousand'
            num = num % 1000
        if 100 <= num < 1000:
            res += " " + digit_aph[num / 100] + ' Hundred'
            num = num % 100
        if 20 < num < 100:
            res += " " + digit_aph[num / 10 * 10]
            num = num % 10
        if 0 < num <= 20:
            res += " " + digit_aph[num]
        return res.strip(" ")

if __name__ == "__main__":
    s = Solution()
    print s.numberToWords(101)
    print s.numberToWords(121)
    print s.numberToWords(1112334123)
    print s.numberToWords(16)
    print s.numberToWords(0)