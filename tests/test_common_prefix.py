from moving_to_poetry.common_prefix import longestCommonPrefix

def test_longest_common_prefix(self):
    strs = ["flower","flow","flight"]
    strs_bis = ["flower","flow","flight", '']
    pref = longestCommonPrefix(strs)
    assert pref == "fl"
    with self.assertRaises(IndexError):
        longestCommonPrefix(strs_bis)
            