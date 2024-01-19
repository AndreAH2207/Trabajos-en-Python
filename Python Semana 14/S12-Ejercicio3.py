class Cancion:
    def __init__(self, nombre, genero, cantante):
        self.nombre = nombre
        self.genero = genero
        self.cantante = cantante

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def listar_canciones(self):
        for cancion in self.canciones:
            print(f"Nombre: {cancion.nombre}, Genero: {cancion.genero}, Cantante: {cancion.cantante}")

playlists = []

def main():
    while True:
        print("Menú:")
        print("1. Crear Playlist")
        print("2. Agregar canción a Playlist")
        print("3. Listar canciones en Playlist")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_playlist = input("Ingrese el nombre de la Playlist: ")
            nueva_playlist = Playlist(nombre_playlist)
            playlists.append(nueva_playlist)
            print(f"Playlist '{nombre_playlist}' creada.")
        
        elif opcion == "2":
            print("Listado de Playlists: ")
            for playlist in playlists:
                print(playlist.nombre)

            print ("")    
            nombre_playlist = input("Ingrese el nombre de la Playlist a la que desea agregar la canción: ")
            cancion_nombre = input("Ingrese el nombre de la canción: ")
            cancion_genero = input("Ingrese el género de la canción: ")
            cancion_cantante = input("Ingrese el cantante de la canción: ")
            
            for playlist in playlists:
                if playlist.nombre == nombre_playlist:
                    nueva_cancion = Cancion(cancion_nombre, cancion_genero, cancion_cantante)
                    playlist.agregar_cancion(nueva_cancion)
                    print(f"Canción '{cancion_nombre}' agregada a la Playlist '{nombre_playlist}'.")
                    break
            else:
                print(f"No se encontró la Playlist.")
        
        elif opcion == "3":
            print("Listado de Playlists: ")
            for playlist in playlists:
                print(playlist.nombre)
            
            nombre_playlist = input("Ingrese el nombre de la Playlist que desea listar: ")
            
            for playlist in playlists:
                if playlist.nombre == nombre_playlist:
                    print(f"Canciones en la Playlist '{nombre_playlist}':")
                    playlist.listar_canciones()
                    break
            else:
                print(f"No se encontró la Playlist '{nombre_playlist}'.")
        
        elif opcion == "4":
            break

main()   