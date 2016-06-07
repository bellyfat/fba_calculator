import package

class FBACalculator(object):

	PACKAGE_TYPES = {
		"SmallStandardMedia": package.SmallStandardMedia,
		"LargeStandardMedia": package.SmallStandardMedia,
		"XLargeStandardMedia": package.SmallStandardMedia,
		"SmallStandardNonMedia": package.SmallStandardNonMedia,
		"LargeStandardNonMedia": package.LargeStandardNonMedia,
		"XLargeStandardNonMedia": package.XLargeStandardNonMedia,
		"SmallOversize": package.SmallOversize,
		"MediumOversize": package.MediumOversize,
		"LargeOversize": package.LargeOversize,
		"SpecialOversize": package.SpecialOversize,
	}	

	def __init__(length, width, height, 
			     weight, is_media, is_apparel, is_pro):
		self._height = self._decimal(height)
        self._length = self._decimal(length)
        self._width = self._decimal(width)
        self._weight = self._decimal(weight)
        self._is_media = is_media
        self._is_apparel = is_apparel
        self._is_pro = is_pro
        # Oversize or Standard
        self._size = package.Package.size(self.length, self.width, 
        	self.height, self.weight)
		self._girth = package.Package.girth(self.length, 
			self.width, self.height)
		self._tier = self._size_tier()

	def _package(self):
		media = "NonMedia"
		if self.is_media:
			media = "Media"
		package = "{tier}{size}{media}".format(
			tier=self.tier, size=self.size, media=media)
		return cls.PACKAGE_TYPES[package]




	def fee(self, pick_pack, weight_handling, thirty_day, order_handling, is_apparel, is_pro):
	    fee = (
	        pick_pack +
	        weight_handling +
	        thirty_day +
	        order_handling)
	    if is_apparel:
	        fee += 0.40
	    if not is_pro:
	        fee += 1.0
	    return Decimal(fee).quantize(TWO_PLACES)


	def _get_outbound_ship_weight(self, weight, dimensional_weight,
	                             standard_oversize, is_media, size_tier):
	    """Calculate the outbound shipping weight

	    Standard-Size Media
	        Packaging weight: 2 (0.125 lb.)
	        Rule: unit weight + packaging weight
	            *Round up to the nearest whole pound
	    Standard-Size Non-Media
	        Packaging weight: (1 lb. or less) 4 oz (0.25 lb.)
	        Rule: unit weight + packaging weight
	            *Round up to the nearest whole pound
	    Standard-Size Non-Media (more than 1 lb.)
	        Packaging weight: 4 oz (0.25 lb.)
	        Rule: max(unit ueight or dimensional weight) + packaging weight
	            *Round up to the nearest whole pound
	    Small, Medium, and Large Oversize
	        Packaging weight: 16 oz (1.00 lb.)
	        Rule: max(unit ueight or dimensional weight) + packaging weight
	            *Round up to the nearest whole pound
	    Special Oversize
	        Packaging weight: 16 oz (1.00 lb.)
	        Rule: unit weight + packaging weight
	            *Round up to the nearest whole pound
	    """
	    if self.is_media:
	        outbound = Decimal(self.weight + PACKAGE_WEIGHT['STND_MEDIA'])
	        return outbound.quantize(Decimal('0'), rounding=ROUND_UP)
	    if standard_oversize == standard:
	        if self.weight <= 1:
	            outbound = Decimal(self.weight + PACKAGE_WEIGHT['STND_NON_SM'])
	        else:
	            outbound = Decimal(
	                Decimal(max(self.weight, dimensional_weight)) +
	                Decimal(PACKAGE_WEIGHT['STND_NON_LG'])
	            )
	    else:
	        if size_tier == SPL_OVER:
	            outbound = Decimal(self.weight + PACKAGE_WEIGHT['OVER'])
	        else:
	            outbound = Decimal(
	                Decimal(max(self.weight, dimensional_weight)) +
	                Decimal(PACKAGE_WEIGHT['SPECIAL'])
	            )
	    return outbound.quantize(Decimal('0'), rounding=ROUND_UP)

	def _size_tier(self):
		if self.size == "Standard":
			size_tier = self._standard(
				self.is_media, self.length, self.width, 
				self.height, self.weight, self.girth)
			return size_tier
		#pacakge is oversize
		size_tier = self._oversize(
			self.is_media, self.length, self.width, 
			self.height, self.weight, self.girth)
		return size_tier
		
	def _standard(self):
		fee_weight = 12/16.0
	    if self.is_media:
	        fee_weight = 14/16.0
	    small = [
	        (fee_weight >= self.weight),
	        (max(self.length, self.width, self.height) <= 15),
	        (min(self.length, self.width, self.height) <= 0.75),
	        (median([self.length, self.width, self.height]) <= 12)]
	    if all(small):
	        return "Small"
	    return "Large"

	def _oversize(self):
		special = [
			(self.girth > 165), 
			(weight > 150), 
			(max(self.length, self.width, self.height) > 108)]
		medium = [
			(weight > 70),
		    (max(self.length, self.width, self.height) > 60),
		    (median([self.length, self.width, self.height]) > 30)]
		if any(special):
		    return "Special"
		if self.girth > 130:
		    return "Large"
		if any(medium):
		    return "Medium"
		return "Small"


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

    @property
    def size(self):
    	return self._size
    
    @property
    def tier(self):
    	return self._tier
    
    @property
    def girth(self):
    	return self._girth
