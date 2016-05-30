# Run tests on the samples given by Amazon
# TODO: Add samples from
#   https://services.amazon.com/fulfillment-by-amazon/pricing.htm

from fba_calc import calculate_fees
<<<<<<< HEAD
import unittest


class TestingPackages(unittest.TestCase):

    def test_small_stnd_media(self):
        l,w,h,wt = [7.5, 5.3, 0.6, 0.15]
        package = float(calculate_fees(l, w, h, wt, is_media=True))
        self.assertEqual(package, 1.56)

    def test_lrg_stnd_media(self):
        # updated
        # FAILING: For some reason this one is getting
        # converted to large media standard 2 weight tier.
        l,w,h,wt = [6.5, 5.2, 1.5, 0.1]
        package = float(calculate_fees(l, w, h, wt, is_media=True))
        self.assertEqual(package, 1.91)

    def test_small_stnd_non(self):
        # updated
        l,w,h,wt = [6.93, 6, 0.6, 0.53]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 2.56)

    def test_large_stnd_non(self):
        l,w,h,wt = [3.8, 3.7, 1.9, 0.3]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 3.02)

    def test_small_oversize(self):
        l,w,h,wt = [15.7, 15.0, 0.4, 0.7]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 6.15)

    def test_medium_oversize(self):
        l,w,h,wt = [63.0, 11.6, 6.3, 46.6]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 25.87)

    def test_large_oversize(self):
        l,w,h,wt = [50.3, 30.0, 15.0, 146.0]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 117.98)
    
    def test_special_oversize(self):
        #example is wrong
        l,w,h,wt = [51.6, 35.6, 19.0, 53.5]
        package = float(calculate_fees(l, w, h, wt, is_media=False))
        self.assertEqual(package, 135.11)

class TestingProduct(unittest.TestCase):


    def test__decimal(self):
        pass

    def test_standard_or_oversize(self):
        pass

if __name__ == '__main__':
    unittest.main()