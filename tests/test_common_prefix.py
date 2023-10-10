import pytest
from moving_to_poetry.common_prefix import longestCommonPrefix

strs = ["flower","flow","flight"]
strs_bis = ["flower","flow","flight", '']

pref = longestCommonPrefix(strs)

def test_longest_common_prefix():
    assert pref == "fl"
    with pytest.raises(IndexError):
        longestCommonPrefix(strs_bis)
            