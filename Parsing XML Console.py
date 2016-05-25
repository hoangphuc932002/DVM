from bs4 import BeautifulSoup
sinp = raw_input("File name:")
Source = BeautifulSoup(open(sinp),'xml')
finp = raw_input("Search:")
channels = Source.findAll(finp)
for x in channels:
    print x.find('name').string,':=>',x.description.string
