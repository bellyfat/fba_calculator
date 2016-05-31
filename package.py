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
import logging
from numpy import median
from abc import ABCMeta, abstractmethod, abstractproperty
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP

"""classes
    abstract Package
        abstract Media
        - SmallStandardMedia
        - LargeStandardMedia
        - XLargeStandardMedia
        abstra Standard
        - SmallStandardNonMedia
        - LargeStandardNonMedia
        - XLargeStandardNonMedia
        abstract Oversize
        - SmallOversize
        - MediumOversize
        - LargeOversize
        - SpecialOversize
"""

def size(length, width, height, weight):
    """Determine if the package is standard or oversize.

    Args
        :length Decimal: length of package
        :width Decimal: width of package
        :height Decimal: height of package
        :weight Decimal: weight of package
    Return:
        :size str: amazon size of package. "Oversize" or "Standard"
    """
    size = "Standard"
    if any(
        [
            (weight > 20),
            (max(length, width, height) > 18),
            (min(length, width, height) > 8),
            (median([length, width, height]) > 14)
        ]
    ):
        size = "Oversize"
    return size



class Package(metaclass=ABCMeta):

    TWO_PLACES = Decimal("0.01")

    def __init__(self, height, length, width, weight, size,
                  is_media=False, is_apparel=False, is_pro=False):
        self._height = self._decimal(height)
        self._length = self._decimal(length)
        self._width = self._decimal(width)
        self._weight = self._decimal(weight)
        self._is_media = is_media
        self._is_apparel = is_apparel
        self._is_pro = is_pro


    @staticmethod
    def decimal(num):
        """Tries to convert `num` to Decimal

        Args:
            :num Decimal Compatible: 
                a number to be converted to Decimal

        Returns:
            :Decimal(num):
        """
        try:
            return Decimal(num)
        except:
            raise TypeError("Please provide Decimal compatible values.")

    @abstractmethod
    def thirtyday(standard_oversize, cubic_foot):
        raise NotImplementedError

    @staticmethod
    def size(length, width, height, weight):
        """Determine if the package is standard or oversize.

        Args
            :length Decimal: length of package
            :width Decimal: width of package
            :height Decimal: height of package
            :weight Decimal: weight of package
        Return:
            :size str: amazon size of package. "Oversize" or "Standard"
        """
        size = "Standard"
        if any(
            [
                (weight > 20),
                (max(length, width, height) > 18),
                (min(length, width, height) > 8),
                (median([length, width, height]) > 14)
            ]
        ):
            size = "Oversize"
        return size

    @staticmethod
    def cubic_foot(length, width, height):
        return Decimal(length * width * height) / Decimal('1728.0')

    @staticmethod
    def girth(length, width, height):
        gl = (
            max(length, width, height) +
            (median([length, width, height]) * 2) +
            (min(length, width, height) * 2)
        )
        return Decimal(gl).quantize(Decimal("0.1"))

    @classmethod
    def dimensional_weight(cls, length, width, height):
        dimensional_weight = Decimal(
            height * length * width) / Decimal(166.0)
        return Decimal(dimensional_weight).quantize(cls.TWO_PLACES)

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



class StandardPackage(Package):

    def __init__(self, package_type):
        super(StandardPackage, self).__init__()
        self._pick_pack = Decimal("1.06")
        self._size = "Standard"

    
    def thirtyday(self):
        return Decimal('0.5525') * self._cubic_foot()

    @property
    def pick_pack(self):
        return self._pick_pack    
    


class StandardPackageNonMedia(StandardPackage):

    def __init__(self):
        super(StandardNonPackage, self).__init__()
        self._order_handling = 0
        self._package_weight = Package._decimal("0.25")

    @property
    def order_handling(self):
        return self._order_handling
    

class SmallStandardNonMedia(StandardPackageNonMedia):

    def __init__(self):
        self._weight_handling = Decimal("0.50")
        self._package_type = "SmallStandardNonMedia"

    @property
    def package_type(self):
        return self._package_type
    

    @property
    def weight_handling(self):
        return self._weight_handling


class LargeStandardNonMedia(StandardPackage):

    def __init__(self):
        self._weight_handling = Decimal("0.96")
        self._package_type = "LargeStandardNonMedia"

    @property
    def package_type(self):
        return self._package_type
    
    @property
    def weight_handling(self):
        return self._weight_handling


class XLargeStandardNonMedia(StandardPackage):

    def __init__(self):
        self._weight_handling = Decimal("1.95")
        self._weight_handling_multiplier = Decimal("0.39")
        self._threshold = Decimal("2")
        self._package_type = "XLargeStandardNonMedia"

    @property
    def package_type(self):
        return self._package_type
    
    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier

    @property
    def threshold(self):
        return self._threshold
    
    


class MediaPackage(StandardPackage):

    def __init__(self):
        super(MediaPackage, self).__init__()
        self._order_handling = 0
        self._package_weight = Package._decimal("0.125")

    @property
    def order_handling(self):
        return self._order_handling

    @abstractproperty
    def weight_handling(self):
        return self._weight_handling


class SmallStandardMedia(MediaPackage):

    def __init__(self):
        self._weight_handling = Decimal("0.50")
        self._package_type = "SmallStandardMedia"

    @property
    def package_type(self):
        return self._package_type

    @property
    def weight_handling(self):
        return self._weight_handling

class LargeStandardMedia(StandardPackage):

    def __init__(self):
        self._weight_handling = Decimal("0.85")
        self._package_type = "LargeStandardMedia"

    @property
    def package_type(self):
        return self._package_type

    @property
    def weight_handling(self):
        return self._weight_handling


class XLargeStandardMedia(StandardPackage):

    def __init__(self):
        self._weight_handling = Decimal("1.24")
        self._weight_handling_multiplier = Decimal("0.41"),
        self._threshold = Decimal("2")
        self._package_type = "XLargeStandardMedia"

    @property
    def package_type(self):
        return self._package_type

    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier
 

class OversizePackage(Package):

    def __init__(self):
        self._order_handling = Decimal("0")
        self._size = "Oversize"
        self._package_weight = Package._decimal("1.00")
        super(OversizePackage, self).__init__()

    def thirtyday(self):
        return Decimal('0.4325') * self._cubic_foot()
    
    @property
    def size(self):
        return self._size

    @property
    def order_handling(self):
        return self._order_handling
        
    @property
    def package_weight(self):
        return self._package_weight

    @abstractproperty
    def pick_pack(self):
        pass

    @abstractproperty
    def weight_handling(self):
        pass
    
    @abstractproperty
    def weight_handling_multiplier(self):
        pass

    @abstractproperty
    def threshold(self):
        pass

class SmallOversizePackage(OversizePackage):

    def __init__(self):
        self._pick_pack = Decimal("4.09")
        self._weight_handling = Decimal("2.06")
        self._weight_handling_multiplier = Decimal("0.39")
        self._threshold = Decimal("2")
        super(SmallOversizePackage, self).__init__()
        self._package_type = "SmallOversizePackage"

    @property
    def package_type(self):
        return self._package_type

    @property
    def pick_pack(self):
        return self._pick_pack
    
    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier

    @property
    def threshold(self):
        return self._threshold
    
class MediumOversizePackage(OversizePackage):

    def __init__(self):
        self._pick_pack = Decimal("5.20")
        self._weight_handling = Decimal("2.73")
        self._weight_handling_multiplier = Decimal("0.39")
        self._threshold = Decimal("2")
        super(MediumOversizePackage, self).__init__()
        self._package_type = "MediumOversizePackage"

    @property
    def package_type(self):
        return self._package_type

    @property
    def pick_pack(self):
        return self._pick_pack
    
    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier

    @property
    def threshold(self):
        return self._threshold

class LargeOversizePackage(OversizePackage):

    def __init__(self):
        self._pick_pack = Decimal("8.40")
        self._weight_handling = Decimal("63.98")
        self._weight_handling_multiplier = Decimal("0.80")
        self._threshold = Decimal("90")
        super(LargeOversizePackage, self).__init__()
        self._package_type = "LargeOversizePackage"

    @property
    def package_type(self):
        return self._package_type

    @property
    def pick_pack(self):
        return self._pick_pack
    
    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier

    @property
    def threshold(self):
        return self._threshold


class SpecialOversizePackage(OversizePackage):

    def __init__(self):
        self._pick_pack = Decimal("10.53")
        self._weight_handling = Decimal("124.58")
        self._weight_handling_multiplier = Decimal("0.92")
        self._threshold = Decimal("90")
        super(SpecialOversizePackage, self).__init__()
        self._package_type = "SpecialOversizePackage"

    @property
    def package_type(self):
        return self._package_type

    @property
    def pick_pack(self):
        return self._pick_pack
    
    @property
    def weight_handling(self):
        return self._weight_handling
    
    @property
    def weight_handling_multiplier(self):
        return self._weight_handling_multiplier

    @property
    def threshold(self):
        return self._threshold

 
