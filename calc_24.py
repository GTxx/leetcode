from copy import copy

def pailie(lst):
    res = []
    length = len(lst)
    for i in range(length):
        for j in range(i+1, length):
            lst_tmp = copy(lst)
            a = lst[i]
            b = lst[j]
            lst_tmp.remove(a)
            lst_tmp.remove(b)
            res.append((a, b, lst_tmp))
    return res


class Literal(object):
    def __init__(self, a, literal=None):
        self.val = a
        if not literal:
            self.literal = '{}'.format(a)
        else:
            self.literal = literal

def lst_2_literal(lst):
    return [Literal(i) for i in lst]

def calc(lst, total):
    if len(lst) == 1:
        if lst[0].val == total:
            return lst[0].literal
        elif lst[0] == -total:
            return '-{}'.format(lst[0].literal)
        else:
            return False
    else:
        for a, b, rem_lst in pailie(lst):
            # import ipdb; ipdb.set_trace()
            res = calc([Literal(a.val+b.val, '({}+{})'.format(a.literal, b.literal))] + rem_lst, total)
            if res:
                return res

            res = calc([Literal(a.val-b.val, '({}-{})'.format(a.literal, b.literal))] + rem_lst, total)
            if res:
                return res

            res = calc([Literal(a.val*b.val, '({}*{})'.format(a.literal, b.literal))] + rem_lst, total)
            if res:
                return res
            if b.val!=0 and abs(a.val) > abs(b.val):
                res = calc([Literal(a.val/b.val, '({}/{})'.format(a.literal, b.literal))] + rem_lst, total)
                if res:
                    return res

            if a.val!=0 and abs(b.val) > abs(a.val):
                # res = calc([b/a] + rem_lst, total, ['{}/{}'.format(b, a)] + s)
                res = calc([Literal(b.val/a.val, '({}/{})'.format(b.literal, a.literal))] + rem_lst, total)
                if res:
                    return res

            return False


def calc1(lst, total):
    lst_literal = lst_2_literal(lst)
    return calc(lst_literal, total)
