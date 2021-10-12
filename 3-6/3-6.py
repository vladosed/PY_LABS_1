#create dictionary with 5 countries
from typing import ChainMap


countries_dict = {
    'Ukraine': 'UA',
    'United States': 'US',
    'United Kingdom': 'UK',
    'Poland': 'PL',
    'Russia': 'RU'
}

#create dictionary with capitals
capitals_dict = {
    'UA': 'Kyiv',
    'US': 'Washington',
    'UK': 'London',
    'PL': 'Warsaw',
    'RU': 'Moscow'
}
#add element to countries
countries_dict['France'] = 'FR'

#add element to capitals
capitals_dict['FR'] = 'Paris'

#print sentence for each record in countries
for key, value in countries_dict.items():
    print("Domain for {} is {}".format(key, value))


#print sentesce for each record in capitals
for key, value in capitals_dict.items():
    print("Capital for {} is {}".format(key, value))

#merge senteces together
for key, value in countries_dict.items():
    print("Domain for {} is {}. The capital is {}".format(key, value, capitals_dict[value]))

#add COM, GOV
for key, value in countries_dict.items():
    countries_dict[key] = [value, "COM", "GOV"]

for key, value in countries_dict.items():
    print("Domain for {} is {}. The capital {}".format(key, value, capitals_dict[value[0]]))