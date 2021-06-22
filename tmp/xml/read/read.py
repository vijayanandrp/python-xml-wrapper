"""
URL - https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2
"""
import xml.etree.ElementTree as ET
import re

tree = ET.parse('movies.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

# to get all elements in the entire tree
all_elem = [(elem.tag, elem.attrib, elem.text[:10])
            for elem in root.iter()]
print(all_elem)

# for movie in root.iter('movie'):
#     print(movie.attrib)

# for desc in root.iter('description'):
#     print(desc.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)
"""
{'favorite': 'True', 'title': 'Batman Returns'}
{'favorite': 'False', 'title': 'Reservoir Dogs'}
"""

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
"""
{'multiple': 'Yes'}
{'multiple': 'Yes'}
{'multiple': 'Yes'}
"""


# Tip: use '...' inside of XPath to return the parent element of the current element.
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)
"""
{'favorite': 'True', 'title': 'THE KARATE KID'}
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'False', 'title': 'ALIEN'}
"""

# ########## MODIFY / FIX ###############

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf.tag, b2tf.attrib)
"""
movie {'favorite': 'False', 'title': 'Back 2 the Future'}
"""
b2tf.tag = 'newmovie'
b2tf.attrib['title'] = 'Back to the Future'
print(b2tf.tag, b2tf.attrib)
"""
newmovie {'favorite': 'False', 'title': 'Back to the Future'}
"""


# Fixing attributes
for form in root.findall("./genre/decade/movie/format"):
    # print(form.attrib, form.text)
    match = re.search(',', form.text)
    if match:
        form.set('multiple', 'Yes')
    else:
        form.set('multiple', 'No')


# ######### ADD SUB ELEMENT ############
for decade in root.findall('./genre/decade'):
    print(decade.attrib)
    for year in decade.findall('./movie/year'):
        print(year.text)


for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib, movie.find("./year").text)

"""
{'favorite': 'False', 'title': 'X-Men'} 2000 {'category': 'Action'} {'years': '1990s'}
{'favorite': 'FALSE', 'title': 'American Psycho'} 2000 {'category': 'Action'} {'years': '1990s'}
"""

# Goal is to add action 2000s movie and thriller 2000s movies

# create a sub element under the action
action = root.find("./genre[@category='Action']")
new_decade = ET.SubElement(action, 'decade')
new_decade.attrib["years"] = "2000s"

# moving the element
xmen = root.find("./genre/decade/movie[@title='X-Men']")
new_decade = root.find("./genre[@category='Action']/decade[@years='2000s']")
new_decade.append(xmen)

# delete the old one
old_decade = root.find("./genre[@category='Action']/decade[@years='1990s']")
old_decade.remove(xmen)

# create a sub element under the action
action = root.find("./genre[@category='Thriller']")
new_decade = ET.SubElement(action, 'decade')
new_decade.attrib["years"] = "2000s"

# moving the element NOTE @ for attrib and without @ meant for text.
amer_psy = root.find("./genre/decade/movie[@title='American Psycho']")
new_decade = root.find("./genre[@category='Thriller']/decade[@years='2000s']")
new_decade.append(amer_psy)

# delete the old one
old_decade = root.find("./genre[@category='Thriller']/decade[@years='1980s']")
old_decade.remove(amer_psy)

# ########## WRITE ###############

print(" ===================== newmovie.xml ====================")
# Write out the tree to the file again
tree.write('newmovie.xml')

tree = ET.parse('newmovie.xml')
root = tree.getroot()

for form in root.findall('./genre/decade/movie/format'):
    print(form.tag, form.attrib, form.text)

for decade in root.findall('./genre/decade'):
    print(decade.attrib)
    for year in decade.findall('./movie/year'):
        print(year.text)
