import xml.etree.ElementTree as ET
tree = ET.parse('countries.xml')
# root = ET.fromstring(country_data_as_string)
root = tree.getroot()
print(root.tag)
for e in root:
    #print(e.tag)
    attribs = e.attrib
    print(e[0].text)
    print(attribs['name'])

print(root[0][1].text)
