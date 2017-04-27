import unittest
from get_delete_data import get_data
class TestURL(unittest.TestCase):

  # Test for primes
  def testURL(self):
    # file is present locally
    result = get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
    self.assertTrue(result[0])
    # file is not present locally
    result = get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
    self.assertTrue(result[0])
    # the URL points to a file that exists;
    result = get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
    self.assertTrue(result[0])
    # URL does not point to a file that exists
    result = get_data('https://data.seattle.gov/resource/4x5-26gy.csv')
    self.assertTrue(result[0])
    #delete file
    result = delete_data('https://data.seattle.gov/resource/4xy5-26gy.csv')
    self.assertTrue(result[0])