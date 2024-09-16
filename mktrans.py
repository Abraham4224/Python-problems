fromstr = "abc"  # Caracteres a reemplazar
tostr = "123"    # Caracteres de reemplazo
deletestr = "xyz"  # Caracteres a eliminar

# Crear la tabla de traducción
table = str.maketrans(fromstr, tostr, deletestr)

# Cadena original
line = "abcxyz"

# Aplicar la traducción
translated_line = line.translate(table)

print(translated_line)  # Salida: "123"
