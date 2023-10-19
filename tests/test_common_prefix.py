"""Import pytest module to automate the tests of my 
function"""

import pytest
from moving_to_poetry.common_prefix import longest_common_prefix

strs = ["flower","flow","flight"]
strs_bis = ["flower","flow","flight", '']

pref = longest_common_prefix(strs)

def test_longest_common_prefix():
    """tests the limits of the 
    longest_common_previx function"""
    assert pref == "fl"
    with pytest.raises(IndexError):
        longest_common_prefix(strs_bis)
            