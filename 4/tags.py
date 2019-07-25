import os
from collections import Counter
import urllib.request
import re
# prep
tempfile = os.path.join('./', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile, encoding='utf8') as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tag_counter = Counter(re.findall("<category>(\w*)</category>", content))
    return tag_counter.most_common(10)
