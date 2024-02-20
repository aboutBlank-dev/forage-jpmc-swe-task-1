import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  #I have one concern with the tests for getDataPoint().
  #I am not too familiar with bid/ask prices, but I don't think that (bid/ask)/2 will ALWAYS be the way we want to calculate the price(implementation might change).
  #The getDataPoint tests are testing implementation details (price = (bid/ask)/2), meaning that if the implementation changes, the test will fail.
  #Does that make it a "bad" test?
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, quote['top_bid']['price'])
        self.assertEqual(ask_price, quote['top_ask']['price'])
        self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2.0)  

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
        _, _, _, price = getDataPoint(quote)
        self.assertEqual(price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2.0)

  def test_getRatio_calculateRatio(self):
    price_a = 120.48
    price_b = 121.68
    self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

  #Ensure that the return value is a float and therefore no precision is lost. 
  def test_getRatio_ensureFloat(self):
    ratio = getRatio(120.48, 121.68)
    self.assertTrue(isinstance(ratio, float))

  def test_getRatio_zeroDivision(self):
    try:
        self.assertIsNone(getRatio(120.48, 0))
    except ZeroDivisionError:
        self.fail("getRatio() raised ZeroDivisionError.")

if __name__ == '__main__':
    unittest.main()
