class Solution:
    def is_ipv4(self, IP: str) -> bool:
        four_digit = IP.split(".")
        if len(four_digit) != 4:
            return False
        for digit in four_digit:
            try:
                if int(digit) > 255 or int(digit) < 0:
                    return False
                elif int(digit) == 0 and digit != "0":
                    return False
                elif int(digit) != 0 and digit.startswith("0"):
                    return False
                elif digit.startswith("-"):
                    return False
            except ValueError as e:
                return False
        return True

    def is_ipv6(self, IP: str) -> bool:
        digits = IP.split(":")
        if len(digits) != 8:
            return False
        for digit in digits:
            try:
                if int(digit, 16) > 65535 or int(digit, 16) < 0:
                    return False
                elif len(digit) > 4:
                    return False
                elif digit.startswith("-"):
                    return False
            except ValueError as e:
                return False
        if digits[0] != "0" and digits[0].startswith("0"):
            return False
        return True

    def validIPAddress(self, IP: str) -> str:
        if self.is_ipv6(IP):
            return "IPv6"
        elif self.is_ipv4(IP):
            return "IPv4"
        else:
            return "Neither"


if __name__ == "__main__":
    s = Solution()
    assert s.is_ipv4("172.16.254.1")
    assert not s.is_ipv4("172.16.254.01")
    assert not s.is_ipv4("256.256.256.256")
    assert s.is_ipv6("2001:0db8:85a3:0:0:8A2E:0370:7334")
    assert s.is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
    assert s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6"
    assert s.validIPAddress("256.256.256.256") == "Neither"
    assert s.validIPAddress("172.16.254.1") == "IPv4"
    assert s.validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334") == "Neither"
    assert s.validIPAddress("192.0.0.1") == "IPv4"
    assert s.validIPAddress("0.0.0.0") == "IPv4"
