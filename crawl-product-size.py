import urllib2;
import sys;
from lxml import html;
import lxml.cssselect

def load_page(url): 
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36')
    return urllib2.urlopen(request).read().decode("iso-8859-2");

def parse_to_tree(markup):
    return html.fromstring(markup)

def find_sizes(root_element):
    return map(lambda element : element.text, root_element.cssselect('tr.product-size:not(.disabled) td.size-name'))

if sys.argv[1] == 'test': 
    test_url = 'http://www.zara.com/pl/pl/kobieta/spodnie/zobacz-wi%C4%99cej/%C5%BCakardowe-spodnie-typu-culotte-c733898p3956074.html'

    assert len(load_page(test_url)) > 0
    assert parse_to_tree(load_page(test_url)) is not None
    assert find_sizes(parse_to_tree(load_page(test_url))) is not None
else:
    print find_sizes(parse_to_tree(load_page(sys.argv[1])))
