from bs4 import BeautifulSoup

x = """<foo>
   <bar>
      <type foobar="1"/>
      <type foobar="2"/>
   </bar>
</foo>"""

y = BeautifulSoup(x, features="lxml")
print(y.foo.bar.type["foobar"])
# u'1'

print(y.foo.bar.findAll("type"))
# [<type foobar="1"></type>, <type foobar="2"></type>]

print(y.foo.bar.findAll("type")[0]["foobar"])
# u'1'
print(y.foo.bar.findAll("type")[1]["foobar"])
# u'2'
