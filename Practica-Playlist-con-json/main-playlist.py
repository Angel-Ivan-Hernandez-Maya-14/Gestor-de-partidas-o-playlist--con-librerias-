import gestorjson
import time

def main():
    while True:
        gestorjson.menu()
        opcion=str(input("Elige una opción: "))
        if opcion.strip()=="1":
            gestorjson.agregar()
        elif opcion.strip()=="2":
            gestorjson.mostrar()
        elif opcion.strip()=="3":
            gestorjson.buscar()
        elif opcion.strip()=="4":
            gestorjson.eliminar()
        elif opcion.strip()=="5":
            print("Saliendo del programa...")
            time.sleep(2)
            print("Hasta pronto :)")
            break
        else:
            print("\nOpción no válida. Intentelo de nuevo.")
        
if __name__== "__main__":
    main()
