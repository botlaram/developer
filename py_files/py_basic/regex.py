import re

content = '''Tata Motors International Business
A Block, Shivasagar Estate,
Dr. Annie Besant Road,
Worli, Mumbai - 400018
Contact: +91(22) 67577200


Domestic Business
Tata Motors Ltd
4th Floor, Ahura Centre
82 Mahakali Caves Road
MIDC, Andheri East
Mumbai - 400093
Contact: 022 - 62407101
Email: ramakrishna@gmail'''



##findall,search,split,finditer

## search for word tata
# pattern=re.compile(r'Tata')

## search for matching one or more words
# pattern= re.compile(r'bai*')

## search for matching any character
# pattern=re.compile(r'.ie')

## any word starts with use ^
# pattern=re.compile(r'^Tata')

## any word ends with use $
# pattern=re.compile(r'mail$')

## either or
# pattern=re.compile(r'Contact|Email')


print("\n << eg 2 special sequences >> \n")
#================================================================
##example 2

## search for para Start with use \A
# pattern=re.compile(r'\ATata')

## search for letter which Starts with use \b
# pattern=re.compile(r'\bMum')
pattern=re.compile(r'\b40')

matches=pattern.finditer(content)
for match in pattern.finditer(content):
    print(match)
