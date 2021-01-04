import unittest
import Unittesting_cap as cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = "test python"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Test Python')
    
if __name__ == '__main__':
    unittest.main()