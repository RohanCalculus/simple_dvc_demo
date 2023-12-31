import pytest

class NotInRange(Exception):
    def __init__(self, message="Value not in range! Choose an appropriate value."):
        self.message=message
        super().__init__(self.message)

def test_generic():
    a = 2
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
        
def test_something():
    a = 2
    b = 2
    assert True