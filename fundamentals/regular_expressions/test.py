import re

# test_string = '2022-06-12'
#
# # pattern = re.compile(r"abc")
# # matches = pattern.finditer(test_string)
# matches = re.finditer(r"\d{4}[-/]0[5-7][-/]\d{2}", test_string)
#
# # methods: match(), search(), findall(), finditer()
# # split, sub
#
# for match in matches:
#     print(match)

test_string = """
hello world
python 
12345

Mr Simpson
Mr Gyurov
Mrs. Petrova
Mr. Johnson
angel_slujebna@abv.bg
peter_ivanov@gamil.com
freefire1@abv.org
"""

matches = re.finditer(r'([a-zA-Z0-9_]+)@([a-zA-Z-]+)\.(com|bg|org)', test_string)
for match in matches:
    print(match.group(1))