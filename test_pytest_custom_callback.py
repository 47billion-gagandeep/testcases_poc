import custom_callbacks
import pytest

    
def test_joinsString():
    assert('Gagandeep',custom_callbacks.joinsString('Gagan','deep'))
    assertNotEqual('Gagan',custom_callbacks.joinsString('Gagan','deep'))

def test_uppercase():
    assert('GAGAN',custom_callbacks.upppercase('gagan'))
    assertNotEqual('gagan',custom_callbacks.upppercase('gagan'))

def test_lowercase():
    assert('gagan',custom_callbacks.lowercase('Gagan'))
    assertNotEqual('Gagan',custom_callbacks.lowercase('Gagan'))
    

if __name__ == '__main__':
    '''
    it will automatically called the CustomCallback testcases
    '''
    unittest.main()
    