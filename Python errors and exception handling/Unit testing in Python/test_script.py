import unittest
import main_script

class Testing(unittest.TestCase):
    def test_word(self):
        str = 'python'
        result = cap.func(str)
        self.assertEqual(result, 'PYTHON')
        
    def test_sentences(self):
        str = 'python if fun'
        result = cap.func(str)
        self.assertEqual(result, 'PYTHON IS FUN')

if __name__=='main':
    unittest.main()
    
    
    
        