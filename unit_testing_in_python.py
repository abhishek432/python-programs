#                             unit testing programs 
#Example 1 (by ajay)---
"""
import unittest
class TestSum(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(sum([1,2,3]),6,"Should be 6")
  def test_sum_tuple(self):
    self.assertEqual(sum((1,2,2)),5,"Should be 5")

if __name__=='__main__':
  #unittest.main()
  unittest.main(argv=['first-arg-is-ignore'],exit=False)
"""

#Example 2 (by me)--

"""
import unittest
  
class SimpleTest(unittest.TestCase):
  
    # Returns True or False. 
    def test(self):        
        self.assertTrue(True)
  
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignore'],exit=False)
    
"""

#Example 3(by ajay)--
"""
import unittest
class TestSum(unittest.TestCase):
    def test_list_int(self):
        data=[1,2,3]
        result=sum(data)
        self.assertEqual(result,6)

if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignore'],exit=False)

"""  
