class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ip_list = str_2_ip(s, 4)
        remove_duplicate_ip = list(set([ipstr_2_int(ip) for ip in ip_list]))
        return [int_2_ipstr(ip) for ip in remove_duplicate_ip]


def valid_ip_field(s):
    valid_ip_list = [str(i) for i in range(256)]
    return True if s in valid_ip_list else False


def get_pre_ip_field(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [(s, '')]
    elif len(s) == 2:
        return [(s[0], s[1]), (s, '')]
    elif len(s) >= 3:
        if valid_ip_field(s[0:3]):
            return [(s[0], s[1:]), (s[0:2], s[2:]), (s[0:3], s[3:])]
        else:
            return [(s[0], s[1:]), (s[0:2], s[2:])]


def get_valid_ip_field(s):
    res = get_pre_ip_field(s)
    return [(ip, rem_str) for ip, rem_str in res if valid_ip_field(ip)]


def str_2_ip(s, ip_field_num):
    if len(s) < ip_field_num:
        return []
    elif ip_field_num == 1:
        if valid_ip_field(s):
            return [s]
        else:
            return []
    else:
        res = []
        pre_ip_field = get_valid_ip_field(s)
        for ip, rem_str in pre_ip_field:
            for rem_ip in str_2_ip(rem_str, ip_field_num-1):
                res.append('{}.{}'.format(ip, rem_ip))
        return res

def ipstr_2_int(s):
    ip_field_list = s.split('.')
    res = 0
    for ip_field in ip_field_list:
        res = res*256 + int(ip_field)
    return res

def int_2_ipstr(ip):
    res = []
    for i in range(4):
        a = ip % 256
        ip = (ip-a)//256
        res.append(str(a))
    res.reverse()
    return '.'.join(res)
