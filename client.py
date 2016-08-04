# AWS Lambda client function.
from fbacalculator import FBACalculator


def lambdahandler(event, context):
    length = event['length']
    width = event['width']
    height = event['height']
    weight = event['weight']
    is_media = event.get('is_media')
    is_apparel = event.get('is_apparel')
    is_pro = event.get('is_pro')
    calculator = FBACalculator(length, width, height,
        weight, is_media, is_apparel, is_pro)
    return calculator.fees()

def handler(length, 
            width, 
            height, 
            weight, 
            is_media=False, 
            is_apparel=False, 
            is_pro=False):
    calculator = FBACalculator(length, width, height,
        weight, is_media, is_apparel, is_pro)
    return calculator.fees()




print(handler(1,1,1,1))

