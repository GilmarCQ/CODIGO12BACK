from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Clase que sirve para manejar el comportamiento del auth_user"""

    def create_user(self, correo, nombre, rol, password):
        """Creacion de un superuser sin la necesidad de un comando"""
        if not correo:
            raise ValueError('El usuario debe tener obligatoriamente un correo')
        # normalize; valida que sea un correo valido y elimina los espacios innecesarios
        correo = self.normalize_email(correo)
        # manda a llamar al modelo Usuario e inicia su construccion
        nuevoUsuario = self.model(correo=correo, nombre=nombre, rol=rol)
        # set_password; genera un hash en la contraseña usando bcrypt y el algoritmo SHA256
        nuevoUsuario.set_password(password)
        # permite referenciar a la base de datos por default
        nuevoUsuario.save(using=self.db)
        return nuevoUsuario

    def create_superuser(self, correo, nombre, rol, password):
        """Creacion de un super usuario por consola, se llamara el metodo cuando se haga el uso del comando por consola"""
        usuario = self.create_user(correo, nombre, rol, password)
        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using=self.db)
