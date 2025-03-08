import common.generate_random_number as random_number

users = []


def user_register():
    """Registra un usuario validando la contraseña y la unicidad del nickname"""
    id = random_number.generate_unique_id(users)
    name = input("Ingrese el nombre: ").strip()
    nickname = input("Ingrese el nickname: ").strip()

    # Verificar si el nickname ya existe
    if any(user["nickname"] == nickname for user in users):
        print("El nickname ya está en uso. Intente con otro.")
        return None

    while True:
        password = input("Ingrese la contraseña: ").strip()
        password2 = input("Confirme la contraseña: ").strip()

        if password != password2:
            print("Las contraseñas no coinciden. Intente de nuevo.")
        else:
            break

    data = {
        "id": id,
        "name": name,
        "nickname": nickname,
        "password": password,  # Idealmente, deberías almacenar un hash de la contraseña
    }

    users.append(data)
    print("Usuario registrado con éxito.")
    return data


# Ejemplo de uso
user_data = user_register()
if user_data:
    print(users)  # Imprime la lista actualizada de usuarios
