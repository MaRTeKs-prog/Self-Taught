import re

string = 'Привидение прошуршало и исчезло в углу.'
m = re.findall('.ло', string, re.IGNORECASE)
print(m)