# Obtención de datos
paises = input("Ingrese varios paises, separados por comas: ")

# Pasamos texto a lista
paises = paises.replace(',',' ').lower().split()

# Pasamos lista a set para eliminar repeticiones
paises = set(paises)

# pasamos set a lista para luego ordenar alfabéticamente
paises = list(paises)
paises.sort()

# Pasamos lista a cadena, agregamos ", " y ponemos
# mayus cada primera letra de cada país
paises = ', '.join(paises).title()

# Imprimimos por consola
mensaje = f"Los paises ingresados son: {paises}"
print(mensaje)
