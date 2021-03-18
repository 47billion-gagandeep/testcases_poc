import custom_callbacks
import unittest

class CustomCallback(unittest.TestCase):
    
    def test_joinsString(self):
        self.assertEquals('Gagandeep',custom_callbacks.joinsString('Gagan','deep'))
        self.assertNotEqual('Gagan',custom_callbacks.joinsString('Gagan','deep'))

    def test_uppercase(self):
        self.assertEqual('GAGAN',custom_callbacks.upppercase('gagan'))
        self.assertNotEqual('gagan',custom_callbacks.upppercase('gagan'))
    
    def test_lowercase(self):
        self.assertEqual('gagan',custom_callbacks.lowercase('Gagan'))
        self.assertNsotEqual('Gagan',custom_callbacks.lowercase('Gagan'))
        
if __name__ == '__main__':
    '''
    it will automatically called the CustomCallback testcases
    '''
    unittest.main()
    