import fba_calc_refactor as calc

class FBACalculator(object):


	def __init__(length, width, height, 
			   weight, is_media, is_apparel, is_pro):
		size = calc.Package.size(length, width, height, weight)
		girth = calc.Package.girth(length, width, height)
		tier = size_tier(
			size, is_media, length, 
			width, height, weight, girth)

	def size_tier(self, size, is_media, length,
	              width, height, weight, girth):
		if size == standard:
			size_tier = _standard(
				is_media, length, width, 
				height, weight, girth)
			return size_tier
		#pacakge is oversize
		size_tier = _oversize(
			is_media, length, width, 
			height, weight, girth)
		return size_tier
		
	def _standard(self, is_media, length,
	              width, height, weight, girth):
		fee_weight = 12/16.0
	    if is_media:
	        fee_weight = 14/16.0
	    size_tier = LRG_STND
	    small = [
	        (fee_weight >= weight),
	        (max(length, width, height) <= 15),
	        (min(length, width, height) <= 0.75),
	        (median([length, width, height]) <= 12)]
	    if all(small):
	        size_tier = SML_STND
	    return size_tier

	def _oversize(self, is_media, length,
	              width, height, weight, girth):
		special = [
			(girth > 165), 
			(weight > 150), 
			(max(length, width, height) > 108)]
		medium = [
			(weight > 70),
		    (max(length, width, height) > 60),
		    (median([length, width, height]) > 30)]
		size_tier = SML_OVER
		if any(special):
		    size_tier = SPL_OVER
		elif girth > 130:
		    size_tier = LRG_OVER
		elif any(medium):
		    size_tier = MED_OVER
		return size_tier
