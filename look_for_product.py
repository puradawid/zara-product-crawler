import background_notifier as background
import crawl_product_size as zara

def create_prediction_process(product, size):
    def check_product_availability():
        result = None
        if product.have_size(size):
            result = "Product is available " + product.to_s()
        return result
    return check_product_availability

import sys
argv = sys.argv
if len(argv) == 3:
    notifier = background.Background(create_prediction_process(zara.ZaraProduct(argv[1]), argv[2]), notification_handler=background.LinuxNotify())
    notifier.start()
    raw_input("Click any key to stop this madness.")
    notifier.stop()
    print("Closing...")
else:
    print """Usage: python look_for_product.py url size
    Where:
      url - URL 'http://zara.com.pl/...' for Zara's product website
      size - desired size like 'XL' 'L' or 'M'"""
