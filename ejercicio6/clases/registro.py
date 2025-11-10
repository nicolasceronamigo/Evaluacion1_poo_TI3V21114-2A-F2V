from clases.usuario import Usuario

class Registro:
    def __init__(self):
        self.lista_usuarios: list[Usuario] = []
    
    #Método para determinar si un usuario existe en el registro
    def usuario_existe(self, nombre: str):
        for usuario in self.lista_usuarios:
            if nombre == usuario.nombre:
                return usuario
        return None
    
    #Método para registrar usuario
    def registrar_usuario(self, nombre, contraseña):
        if not self.usuario_existe(nombre):
            usuario = Usuario(nombre, contraseña)
            self.lista_usuarios.append(usuario)
            return f"Usuario {nombre} registrado con éxito"
        return f"Error, el Usuario {nombre} ya está registrado"
    
    #Método para iniciar sesión
    def iniciar_sesion(self, nombre, contraseña):
        if self.usuario_existe(nombre):
            if contraseña == self.usuario_existe(nombre).contraseña:
                return f"Acceso autorizado {nombre}"
            return "Error, contraseña incorrecta"
        return f"Error, usuario {nombre} no existe"
    
    #Método para consultar si un usuario está registrado
    def consulta_registro(self, nombre):
        if self.usuario_existe(nombre):
            return f"Usuario {nombre} está registrado"
        return f"Usuario {nombre} no está registrado"