from solution import Solution


def test1():
    s = Solution()
    assert s.extract("kaido(1)") == ("kaido", 1)
    assert s.extract("kaido(100)") == ("kaido", 100)
    assert s.extract("kaido") == ("kaido", None)
    assert s.extract("kaido(100") == ("kaido(100", None)
    assert s.extract("kaido(a)") == ("kaido(a)", None)


def test2():
    s = Solution()
    nums = []
    s.insert_num(nums, 3)
    assert nums == [0, 0, 0, 1]


def test3():
    s = Solution()
    assert s.get_next_num([1]) == 1
    assert s.get_next_num([1, 0, 0, 1]) == 1


def test4():
    s = Solution()
    assert s.getFolderNames(["pes", "fifa", "gta", "pes(2019)"]) == ["pes", "fifa", "gta", "pes(2019)"]
    assert s.getFolderNames(["gta", "gta(1)", "gta", "avalon"]) == ["gta", "gta(1)", "gta(2)", "avalon"]
    assert s.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]) == ["onepiece",
                                                                                                       "onepiece(1)",
                                                                                                       "onepiece(2)",
                                                                                                       "onepiece(3)",
                                                                                                       "onepiece(4)"]
    assert s.getFolderNames(["wano", "wano", "wano", "wano"]) == ["wano", "wano(1)", "wano(2)", "wano(3)"]
    assert s.getFolderNames(["kaido", "kaido(1)", "kaido", "kaido(1)"]) == ["kaido", "kaido(1)", "kaido(2)",
                                                                            "kaido(1)(1)"]
    assert s.getFolderNames(["(1)", "(2)", "(1)", "(1)", "(1)(1)"]) == ["(1)", "(2)", "(1)(1)", "(1)(2)", "(1)(1)(1)"]
    assert s.getFolderNames(["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(4)", "onepiece", "onepiece"]) == [
        "onepiece", "onepiece(1)", "onepiece(2)", "onepiece(4)", "onepiece(3)", "onepiece(5)"]
    assert s.getFolderNames(['b(1)', 'b', 'b']) == ['b(1)', 'b', 'b(2)']
    assert s.getFolderNames(
        ["v(1)", "r", "k", "e", "h(3)", "t", "b(1)", "s(4)", "n(1)(4)", "u(2)(4)", "c(1)", "v(4)(4)", "f", "m", "y",
         "w", "p", "n", "j", "i", "z", "b", "h", "r", "w", "j", "i", "h(4)", "f", "u(1)", "c", "k", "t(2)(4)", "m",
         "o(3)", "s", "e", "m(3)(4)", "q", "h(1)(3)", "f", "w", "t", "w", "u(1)(2)", "j", "k", "k", "n", "a", "b", "v"]
    ) == ["v(1)", "r", "k", "e", "h(3)", "t", "b(1)", "s(4)", "n(1)(4)", "u(2)(4)", "c(1)", "v(4)(4)", "f", "m",
          "y", "w", "p", "n", "j", "i", "z", "b", "h", "r(1)", "w(1)", "j(1)", "i(1)", "h(4)", "f(1)", "u(1)", "c",
          "k(1)", "t(2)(4)", "m(1)", "o(3)", "s", "e(1)", "m(3)(4)", "q", "h(1)(3)", "f(2)", "w(2)", "t(1)", "w(3)",
          "u(1)(2)", "j(2)", "k(2)", "k(3)", "n(1)", "a", "b(2)", "v"]
    assert s.getFolderNames(['r(1)', 'r', 'r(2)(1)', 'r', 'r', 'r', 'r', 'r(1)', 'r', 'r', 'r(2)', 'r(2)(1)', 'r']) == \
           ['r(1)', 'r', 'r(2)(1)', 'r(2)', 'r(3)', 'r(4)', 'r(5)', 'r(1)(1)', 'r(6)', 'r(7)', 'r(2)(2)', 'r(2)(1)(1)', 'r(8)']
