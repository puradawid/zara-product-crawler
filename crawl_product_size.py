# ZARA PRODUCT SIZE CRAWLER - reads zara page and finds sizes available (or tests against given)
#
# Who cares about license? Do whatever you want with this code.

import os;
import urllib2;
import sys;
from lxml import html;
import lxml.cssselect

USER_AGENT_FAKE = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36'

# Simple class toa wrap up reading functionallity of reading HTML page using HTTP
class DOMPageContent:
    _url = None

    def __init__(self, url):
        self._url = url;

    def read(self):
        request = urllib2.Request(self._url);
        request.add_header('User-Agent', USER_AGENT_FAKE)
        return html.fromstring(urllib2.urlopen(request).read().decode("iso-8859-2"))

# Wrapper class for a data storage and read - fetch all HTML page and looks for size nodes
# maps text from nodes directly
class ZaraProduct:
    _sizes = None

    def __init__(self, url):
        self._page_content = DOMPageContent(url)

    def sizes(self):
        if self._sizes is None:
            self._sizes = self._page_content.read().cssselect('tr.product-size:not(.disabled) td.size-name')
            self._sizes = map(lambda e : e.text, self._sizes);
        return self._sizes;

    def have_size(self, size):
        return size in self.sizes()

# Command line handling
if len(sys.argv) >= 2 and sys.argv[1] == 'test':
    test_url = 'http://www.zara.com/pl/pl/kobieta/spodnie/zobacz-wi%C4%99cej/%C5%BCakardowe-spodnie-typu-culotte-c733898p3956074.html'
    product = ZaraProduct(test_url)
    assert product.sizes() is not None
elif len(sys.argv) >= 3 and sys.argv[2]:
    desired_size = sys.argv[2]
    product = ZaraProduct(sys.argv[1]);
    print product.have_size(sys.argv[2]);
else:
    product = ZaraProduct(sys.argv[1]);
    print product.sizes();
