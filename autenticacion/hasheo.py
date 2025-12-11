import bcrypt

# paso 1. Obtener contraseña en plano
incoming_password = input("Ingrese su contraseña: ").encode('utf-8')

# paso 2. crear un pedazo de sal
salt = bcrypt.gensalt(rounds=12)

# paso3. Hashear la contraseña en plano y dar una sal al hasheo
hashed_password = bcrypt.hashpw(password=incoming_password, salt=salt)
print(f"Contraseña hasheada: {hashed_password}")

# paso 4. Ingresar denuevo la contraseña para confirmar
confirm_password = input("Ingrese su contraseña nuevamente para confirmar: ").encode('utf-8')

# paso 5. Comparar contraseñas
if bcrypt.checkpw(confirm_password, hashed_password):
    print("|Contraseña verificada correctamente.|")
else:
    print("!!Error: Las contraseñas no coinciden.¡¡")