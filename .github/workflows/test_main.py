import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5
        assert add(32, 12) == 44
        assert add(-1, 12) == 11


#if expected output and actual output are same then we will get pass result.
#to run this, we will use pytest.

#type pytest or python -m pytest
