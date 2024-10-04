import json 

datos = '''
[
 { "id" : "001",
 "x" : "2",
 "nombre" : "Chuck"
 } ,
 { "id" : "009",
 "x" : "7",
 "nombre" : "Brent"
 }
 ]'''

info=json.loads(datos)
print('Total de usuarios:', len(info))

for item in info:
    print('Id',item['id'])
    print('X',item['x'])
    print('Nombre', item['nombre'])
