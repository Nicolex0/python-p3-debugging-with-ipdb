def plus_two(num):
    num = num + 2 
    return num

class TestIpdbDebugging:
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        assert plus_two(3) == 5

