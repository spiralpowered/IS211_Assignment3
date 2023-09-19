import re

matches = re.search('(\d{3})-(\d{3})-(\d{4})', '718-867-5309')

print(matches.group(1))