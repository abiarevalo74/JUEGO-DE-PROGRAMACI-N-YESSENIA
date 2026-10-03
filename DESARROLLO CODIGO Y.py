import random

vida = 100
inventario = []
misiones = 0

print("================================")
print(" AVENTURA: LA BÚSQUEDA DEL TESORO")
print("================================")

nombre = input("Nombre del jugador: ")

while True:
    print("\n--- MENÚ ---")
    print("1. Explorar")
    print("2. Inventario")
    print("3. Misiones")
    print("4. Descansar")
    print("5. Salir")

    op = input("Opción: ")

    # EXPLORAR
    if op == "1":
        print("\n1. Bosque")
        print("2. Cueva")
        print("3. Templo")

        lugar = input("¿A dónde ir? ")

        if lugar == "1":
            print("\nEncontraste una Llave Antigua.")
            inventario.append("Llave")
            misiones += 1

        elif lugar == "2":
            print("\n¡Apareció un enemigo!")
            enemigo = 50

            while enemigo > 0 and vida > 0:
                dano = random.randint(10, 25)
                enemigo -= dano
                print("Atacaste al enemigo.")

                if enemigo > 0:
                    vida -= random.randint(5, 15)

            if vida > 0:
                print("¡Ganaste!")
                inventario.append("Mapa")
                misiones += 1
            else:
                print("GAME OVER")
                break

        elif lugar == "3":
            if "Llave" in inventario:
                print("\nResuelve el acertijo:")
                respuesta = input("¿Qué tiene ciudades, pero no casas? ")

                if respuesta.lower() == "mapa":
                    print("¡Correcto!")
                    inventario.append("Espada")
                    misiones += 1
                else:
                    print("Respuesta incorrecta.")
            else:
                print("Necesitas la Llave.")

    # INVENTARIO
    elif op == "2":
        print("\nInventario:", inventario)

    # MISIONES
    elif op == "3":
        print(f"\nMisiones completadas: {misiones}/3")

        if misiones == 3:
            print("¡Todas las misiones completadas!")
            print("Llegaste a la Cueva del Tesoro.")

            print("\n⚔️ ¡BATALLA FINAL!")
            guardian = 100

            while guardian > 0 and vida > 0:
                guardian -= random.randint(15, 30)
                vida -= random.randint(5, 15)

            if vida > 0:
                print("\n🏆 ¡DERROTASTE AL GUARDIÁN!")
                print("💰 ¡ENCONTRASTE EL TESORO!")
                print("¡FELICIDADES", nombre, "!")
                break
            else:
                print("GAME OVER")
                break

    # DESCANSAR
    elif op == "4":
        vida = 100
        print("\nHas recuperado toda tu vida.")

    # SALIR
    elif op == "5":
        print("\n¿Guardar antes de salir?")
        guardar = input("S/N: ")

        if guardar.lower() == "s":
            print("Partida guardada.")

        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")
