import os
import shutil
from pathlib import Path
from os import system

mi_ruta = Path(Path.cwd(), "Recetas")

# Contar el total de recetas
def contar_recetas(ruta):
    contador = 0

    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


# Mostrar el menú principal
def inicio():
    system("cls")
    print("*" * 50)
    print("*" * 5 + " Bienvenido al Administrador de Recetas " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "x"

    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opción:")
        print("""
        [1] - Leer Receta
        [2] - Crear Receta nueva
        [3] - Crear Categoría nueva
        [4] - Eliminar Receta
        [5] - Eliminar Categoría
        [6] - Salir del programa""")
        eleccion_menu = input()
    return int(eleccion_menu)


# Mostrar las categorías existentes
def mostrar_categorias(ruta):
    print("Categorías:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

# Elegir una categoría existente
def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoría: ")
    return lista[int(eleccion_correcta) -1]

# Mostrar las recetas existentes
def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


# Elegir una receta existente
def elegir_recetas(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")
    return lista[int(eleccion_receta) - 1]


# Leer la receta seleccionada
def leer_receta(receta):
    print(Path.read_text(receta))


# Crear una receta nueva
def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta}, ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe...")


# Crear una Categoría nueva
def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoría {nombre_categoria}, ha sido creada")
            existe = True
        else:
            print("Lo siento, esa categoría ya existe...")


# Eliminar una receta existente
def eliminar_receta(receta):
    Path(receta).unlink() # Método para eliminar un archivo
    print(f"La receta {receta.name}, ha sido eliminada...")


# Eliminar una categoría existente
def eliminar_categoría(categoria):
    # La siguiente linea elimina categorías vacias
    # Path(categoria).rmdir() # Método para eliminar carpetas
    # La siguiente linea elimina categorías aunque tenga recetas dentro
    shutil.rmtree(Path(categoria)) # Método para eliminar carpetas y su contenido
    print(f"La categoría {categoria.name}, ha sido eliminada...")


# Volver al menú principal
def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresione 'V' para volver al menú: ")


finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        # Mostrar Categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir Categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # Mostrar Recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # Si no hay recetas en la categoría seleccionada
        if len(mis_recetas) < 1:
            print("No hay recetas en ésta categoría")
        else:
            # Elegir Recetas
            mi_receta = elegir_recetas(mis_recetas)
            # Leer Receta
            leer_receta(mi_receta)
        # Volver al Inicio
        volver_inicio()
    elif menu == 2:
        # Mostrar Categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir Categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # Crear Receta Nueva
        crear_receta(mi_categoria)
        # Volver al Inicio
        volver_inicio()
    elif menu == 3:
        # Crear Categoría
        crear_categoria(mi_ruta)
        # Volver al Inicio
        volver_inicio()
    elif menu == 4:
        # Mostrar Categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir Categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # Mostrar Recetas
        mis_recetas = mostrar_recetas(mi_categoria)
        # Si no hay recetas en la categoría seleccionada
        if len(mis_recetas) < 1:
            print("No hay recetas que eliminar en ésta categoría")
        else:
            # Elegir Recetas
            mi_receta = elegir_recetas(mis_recetas)
            # Eliminar Receta
            confirmacion = input(f"Seguro que deseas eliminar la receta {mi_receta.name}???\nPresiona 'S' para confirmar: ")
            while confirmacion.lower() == "s":
                eliminar_receta(mi_receta)
                confirmacion = "x"
        # Volver al Inicio
        volver_inicio()
    elif menu == 5:
        # Mostrar Categorías
        mis_categorias = mostrar_categorias(mi_ruta)
        # Elegir Categoría
        mi_categoria = elegir_categoria(mis_categorias)
        # Eliminar Categoría
        confirmacion = input(f"Seguro que deseas eliminar la categoría {mi_categoria.name}???\nPresiona 'S' para confirmar: ")
        while confirmacion.lower() == "s":
            eliminar_categoría(mi_categoria)
            confirmacion = "x"
        # Volver al Inicio
        volver_inicio()
    elif menu == 6:
        # Finalizar Programa
        system("cls")
        print("*" * 56)
        print("*" * 5 + " Gracias por usar el Administrador de Recetas " + "*" * 5)
        print("*" * 56)
        print("\n")
        finalizar_programa = True
