import xml.etree.ElementTree as ET

datos = '''
<thing>
 <users>
  <user x="2">
   <id>001</id>
   <name>Chuck</name>
  </user>
  <user x="7">
   <id>009</id>
   <name>Brent</name>
  </user>
 </users>
</thing>
'''

cosa = ET.fromstring(datos)
lst=cosa.findall('users/user')

for usuario in lst:
    print('Name', usuario.find('name').text)
    print('Id', usuario.find('id').text)
    print('Attr',usuario.get('x'))
