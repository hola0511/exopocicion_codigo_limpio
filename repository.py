# Paso 1: Definir la clase User
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id  # ID único del usuario
        self.name = name  # Nombre del usuario

# Paso 2: Crear la clase UserRepository
class UserRepository:
    def __init__(self):
        self.users = []  # Lista para almacenar los usuarios

    def add(self, user):
        """Agrega un usuario al repositorio."""
        self.users.append(user)
        print(f'Usuario "{user.name}" agregado.')

    def get_by_id(self, user_id):
        """Busca un usuario por su ID."""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None  # Retorna None si no se encuentra el usuario

    def get_all(self):
        """Obtiene todos los usuarios del repositorio."""
        return self.users

# Paso 3: Ejemplo de uso
# Crear el repositorio de usuarios
repo = UserRepository()

# Agregar usuarios al repositorio
repo.add(User(1, 'Samuel'))
repo.add(User(2, 'Sebastián'))
repo.add(User(3, 'Juan'))

# Mostrar todos los usuarios
print("\nLista de usuarios en el repositorio:")
for user in repo.get_all():
    print(f'ID: {user.user_id}, Nombre: {user.name}')

# Buscar un usuario por ID
user_id_to_find = 2
found_user = repo.get_by_id(user_id_to_find)
if found_user:
    print(f'\nUsuario encontrado: ID {found_user.user_id}, Nombre {found_user.name}')
else:
    print(f'No se encontró un usuario con ID {user_id_to_find}')

