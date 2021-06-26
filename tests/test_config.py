import pytest

class NotInRange(Exception):
    def __init__(self, message = "Value not in range"):
        self.message = message
        super().__init__(self.message)

    with pytest.raises(NotInRange):
        if a not in range(10,20):
            print('Exception occured')
            raise NotInRange

def hello():
    a = 1
    assert True
    
def test_ing():
    a = 2
    b = 2
    assert True
