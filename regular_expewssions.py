import re


def multi_find(patterns, phrase):
    for pat in patterns:
        print('Serching for pattern{}'.format(pat))
        print(re.findall(pat, phrase))

        print('\n')


# test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sdddd'

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_patterns = ['[^!.?]+']


multi_find(test_patterns, test_phrase)
