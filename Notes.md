Source - https://wiki.python.org/moin/PythonXml

## XML

```text
This module helps us format XML data in a tree structure
 which is the most natural representation of hierarchical data. 
 Element type allows storage of hierarchical data structures in memory and has the following properties:

Property	       Description
Tag	               It is a string representing the type of data being stored
Attributes	       Consists of a number of attributes stored as dictionaries
Text String	       A text string having information that needs to be displayed
Tail String	       Can also have tail strings if necessary
Child Elements	       Consists of a number of  child elements stored as sequences
```

#### LXML
```text
lxml - a pythonic, ElementTree-compatible binding for the libxml2 and libxslt libraries that comes
with all sorts of powerful XML (and HTML) tools, well integrated into an easy-to-use Python API

a pythonesque, simple-to-use and very fast XML tree library:
ElementTree - the xml.etree package (new in Python 2.5 but available for older versions,
also see the fast xml.etree.cElementTree and the independent implementation lxml)

lxml - lxml has standards compliant XPath 1.0 support based on libxml2.
It also supports the EXSLT extensions (including Python regular expressions)
and allows calling Python functions from within XPath expressions.

XSLT Support
If not mentioned otherwise, this means XSLT 1.0, not XSLT 2.0.
lxml has excellent (and easy-to-use) XSLT support that is based on libxslt.
It also supports calling into Python code from XSL transformations through both XPath and XSLT extensions.

```

###### Python libraries 
```text
1. xml.etree
2. lxml
3. xmltodict
4. beautifulsoup
5. xmlschema
```


ElementTree is an important Python library that allows you to parse and navigate an XML document.
 Using ElementTree breaks down the XML document in a tree structure that is easy to work with. 
 When in doubt, print it out 
 `print(ET.tostring(root, encoding='utf8').decode('utf8'))` - 
 use this helpful print statement to view the entire XML document at once. 
 It helps to check when editing, adding, or removing from an XML.
