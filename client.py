from decimal import Decimal


def get_outbound_ship_weight(unit_weight, dimensional_weight,
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
    if is_media:
        outbound = Decimal(unit_weight + PACKAGE_WEIGHT['STND_MEDIA'])
        return outbound.quantize(Decimal('0'), rounding=ROUND_UP)
    if standard_oversize == standard:
        if unit_weight <= 1:
            outbound = Decimal(unit_weight + PACKAGE_WEIGHT['STND_NON_SM'])
        else:
            outbound = Decimal(
                Decimal(max(unit_weight, dimensional_weight)) +
                Decimal(PACKAGE_WEIGHT['STND_NON_LG'])
            )
    else:
        if size_tier == SPL_OVER:
            outbound = Decimal(unit_weight + PACKAGE_WEIGHT['OVER'])
        else:
            outbound = Decimal(
                Decimal(max(unit_weight, dimensional_weight)) +
                Decimal(PACKAGE_WEIGHT['SPECIAL'])
            )
    return outbound.quantize(Decimal('0'), rounding=ROUND_UP)




def get_cost(pick_pack, weight_handling, thirty_day, order_handling, is_apparel, is_pro):
    costs = (
        pick_pack +
        weight_handling +
        thirty_day +
        order_handling
    )

    if is_apparel:
        costs += 0.40

    if not is_pro:
        costs += 1.0
    return costs.quantize(TWO_PLACES)

