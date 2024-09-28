import hashlib

# Función simple para hashear contraseñas con SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Diccionario para almacenar los usuarios y contraseñas hasheadas
usuarios_contraseñas = {}

# Llenar el diccionario con 5 usuarios y contraseñas hasheadas
for i in range(1, 6):
    usuario = f"usuario{i}"
    contraseña = f"password{i}"
    usuarios_contraseñas[usuario] = hash_password(contraseña)

# Imprimir las contraseñas hasheadas
print("\nUsuarios y contraseñas almacenadas en formato hash (SHA-1):")
for usuario, contraseña_hash in usuarios_contraseñas.items():
    print(f"Usuario: {usuario}, Contraseña (Hash): {contraseña_hash}")


# Lista para almacenar los usuarios y contraseñas en formato hash (SHA-1)
usuarios_contraseñas = []

# Llenar la lista con 5 usuarios y contraseñas hasheadas
for i in range(1, 6):
    usuario = f"usuario{i}"
    contraseña = f"password{i}"
    contraseña_hash = hash_password(contraseña)
    usuarios_contraseñas.append((usuario, contraseña_hash))

# Imprimir las contraseñas hasheadas
print("Usuarios y contraseñas almacenadas en formato hash (SHA-1):")
for usuario, contraseña_hash in usuarios_contraseñas:
    print(f"Usuario: {usuario}, Contraseña (Hash): {contraseña_hash}")