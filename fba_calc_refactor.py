# Amazon FBA Revenue Calculator
# For how the fees are calculated see:
#   https://services.amazon.com/fulfillment-by-amazon/pricing.htm
# run calculate_fees(
#   length,
#   width,
#   height,
#   unit_weight,
#   is_apparel=False,
#   is_media=False,
#   is_pro=True
# )
# Credit to hamptus for supplying me a base to work with.
#   You can check out his current version here @
#   github.com/hamptus/fbacalculator/blob/master/fbacalculator/


import math
from abc import ABCMeta, abstractmethod
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP

"""Structure

classes
    abstract Package
        abstract Media
        - SmallStandardMedia
        - LargeStandardMediaOne
        - LargeStandardMediaTwo
        abstra NonMedia
        - SmallStandardNonMedia
        - LargeStandardNonMediaOne
        - LargeStandardNonMediaTwo
        abstract Oversize
        - SmallOversize
        - MediumOversize
        - LargeOversize
        - SpecialOversize
    - Product
"""

def median(alist):
    alist.sort()
    sortedlist = alist
    n = len(sortedlist)
    mid = n/2
    if (n % 2) == 0: 
        mid2 = n/2 - 1
        return (sortedlist[mid] + sortedlist[mid2])/2.0
    return  sortedlist[mid]


class Product(object):


    self __init__(self, height, length, width, weight, 
                  is_media=False, is_apparel=False, is_pro=False):
        self._height = self._decimal(height)
        self._length = self._decimal(length)
        self._width = self._decimal(width)
        self._weight = self._decimal(weight)
        self._is_media = is_media
        self._is_apparel = is_apparel
        self._is_pro = is_pro
        self._size = self.standard_or_oversize()

    def _decimal(self, num):
        try:
            return Decimal(num)
        except:
            raise TypeError("Please provide Decimal compatible values.")

    def standard_or_oversize():
        if any(
            [(weight > 20),
            (max(self.length, self.width, self.height) > 18),
            (min(self.length, self.width, self.height) > 8),
            (median([self.length, self.width, self.height]) > 14)]
        ):
            return "Oversize"
        return "Standard"

    @property
    def height(self):
        return self._height

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def is_media(self):
        return self._is_media
    
    @property
    def is_apparel(self):
        return self._is_apparel
    

    @property
    def is_pro(self):
        return self._is_pro



class Package(metaclass=ABCMeta):


    def __init__(self):
        pass

    @abstractmethod
    def get_30_day(standard_oversize, cubic_foot):
        raise NotImplementedError




class StandardPackage(Package):

    def __init__(self):
        self._pick_pack = Decimal("1.06")
        

class SmallStandard(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.25)
        self._weight_handling = Decimal(0.50)


class SmallStandardMedia(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.125)
        self._weight_handling = Decimal(0.50)


class LargeStandardOne(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.125)
        self._weight_handling = Decimal(0.50)

class LargeStandardTwo(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.125)
        self._weight_handling = Decimal(0.50)


class LargeStandardMediaOne(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.125)
        self._weight_handling = Decimal(0.50)


class LargeStandardMediaTwo(StandardPackage):

    def __init__(self):
        self._package_weight = Decimal(0.125)
        self._weight_handling = Decimal(0.50)


PICK_PACK = {
    "Standard": Decimal("1.06"),
    "SML_OVER": Decimal("4.09"),
    "MED_OVER": Decimal("5.20"),
    "LRG_OVER": Decimal("8.40"),
    "SPL_OVER": Decimal("10.53"),
}
PACKAGE_WEIGHT = {
    "STND_MEDIA": 0.125,
    "STND_NON_SM": 0.25,
    "STND_NON_LG": 0.25,
    "OVER": 1.00,
    "SPECIAL": 1.00,
}
WEIGHT_HANDLING = {
    "SML_STND_MEDIA": Decimal('0.50'),
    "LRG_STND_MEDIA_1": Decimal('0.85'),
    "LRG_STND_MEDIA_2": Decimal('1.24'),
    "SML_STND_NON": Decimal('0.50'),
    "LRG_STND_NON_1": Decimal('0.96'),
    "LRG_STND_NON_2": Decimal('1.95'),
    "SML_OVER": Decimal('2.06'),
    "MED_OVER": Decimal('2.73'),
    "LRG_OVER": Decimal('63.98'),
    "SPL_OVER": Decimal('124.58'),
}
WEIGHT_HANDLING_MULTIPLIERS = {
    "LRG_STND_MEDIA_2": Decimal('0.41'),
    "LRG_STND_NON_2": Decimal('0.39'),
    "SML_OVER": Decimal('0.39'),
    "MED_OVER": Decimal('0.39'),
    "LRG_OVER": Decimal('0.80'),
    "SPL_OVER": Decimal('0.92'),
}

THRESHOLD = {
    "LRG_STND_MEDIA_2": 2,
    "LRG_STND_NON_2": 2,
    "SML_OVER": 2,
    "MED_OVER": 2,
    "LRG_OVER": 90,
    "SPL_OVER": 90,
}
SML_STND = "SML_STND"
LRG_STND = "LRG_STND"
SPL_OVER = "SPL_OVER"
LRG_OVER = "LRG_OVER"
MED_OVER = "MED_OVER"
SML_OVER = "SML_OVER"

standard = "Standard"
oversize = "Oversize"