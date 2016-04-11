# Run tests on the samples given by Amazon
# TODO: Add samples from
#   https://services.amazon.com/fulfillment-by-amazon/pricing.htm

from fba_calc import calculate_fees

def tests(test=True):
    # The tests.
    print("Testing Small Standard-Size Media")
    l,w,h,wt = [5.6, 4.9, 0.4, 0.3]
    print(float(calculate_fees(l, w, h, wt, is_media=True)) == 1.56)
    print(float(calculate_fees(l, w, h, wt, is_media=True)), '==', 1.56)


    print("Testing Large Standard-Size Media")
    l,w,h,wt = [7.9, 5.1, 1, 0.7]
    print(float(calculate_fees(l, w, h, wt, is_media=True)) == 1.91)
    print(float(calculate_fees(l, w, h, wt, is_media=True)), '==', 1.91)


    print("Testing Small Standard-Size Non-Media")
    l,w,h,wt = [13.8, 9.0, 0.7, 0.7]
    print(float(calculate_fees(l, w, h, wt)) == 2.56)
    print(float(calculate_fees(l, w, h, wt)), '==', 2.56)

    print("Testing Large Standard-Size Non-Media")
    l,w,h,wt = [3.8, 3.7, 1.9, 0.3]
    print(float(calculate_fees(l, w, h, wt)) == 3.02)
    print(float(calculate_fees(l, w, h, wt)), '==', 3.02)

    print("Testing Small Oversize")
    l,w,h,wt = [15.7, 15.0, 0.4, 0.7]
    print(float(calculate_fees(l, w, h, wt)) == 6.15)
    print(float(calculate_fees(l, w, h, wt)), '==', 6.15)

    print("Testing Medium Oversize")
    l,w,h,wt = [63.0, 11.6, 6.3, 46.6]
    print(float(calculate_fees(l, w, h, wt)) == 25.87)
    print(float(calculate_fees(l, w, h, wt)), '==', 25.87)

    print("Testing Large Oversize")
    l,w,h,wt = [50.3, 30.0, 15.0, 146.0]
    print(float(calculate_fees(l, w, h, wt)) == 117.98)
    print(float(calculate_fees(l, w, h, wt)), '==', 117.98)

    print("Testing Special Oversize")
    print("This example is wrong on Amazon. Should be a Large Oversize.")
    l,w,h,wt = [51.6, 35.6, 19.0, 53.5]
    print(float(calculate_fees(l, w, h, wt)) == 135.11)
    print(float(calculate_fees(l, w, h, wt)), '==', 135.11)
