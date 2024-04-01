import os


#def conv_dec_bin



def main():
    #Entrar en bucle en el programa
    while True:
        print("***" * 20)
        print("BIENVENIDO A LA CALCULADORA BINARI-HEXA")
        print("***" * 20)
        print("Debes elegir el tipo de dato que deseas convertir")
        print("1, Para decimal")
        print("2, para binario")
        print("3, para Hexadecimal")
        print("4, para salir del programa")
        base = int(input())
        print("***" * 20)
    
        if base == 1:
            while True:
                print("A que tipo quieres convertir el decimal")
                print("1 = Binario")
                print("2 = Hexadecimal")
                print("***" * 20)
                var_Conv = int(input())
                print("***" * 20)
                if var_Conv == 1:
                    num_Dec = int(input("Ingresa el numero decimal quieres convertir a binario\n"))
                    bina = bin(num_Dec)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(bina+"\n")
                    print("==============================================")
                    break
                elif var_Conv == 2:
                    num_Dec = int(input("ingresa el numero decimal que quieres convertir a hexadecimal\n"))
                    hexa = hex(num_Dec)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(hexa+"\n")
                    print("==============================================")
                    break
        elif base == 2:
            while True:
                print("A que tipo quieres convertir el binario")
                print("1 = Decimal")
                print("2 = Hexadecimal")
                var_Conv = int(input())
                if var_Conv == 1:
                    num_bin = input("ingresa el numero binario que quieres convertir a decimal\n")
                    deci = int(num_bin, 2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(deci,"\n")
                    print("==============================================")
                    break
                elif var_Conv == 2:
                    num_bin = input("ingresa el numero binario que quieres convertir a hexadecimal\n")
                    hexadeci = format(int(num_bin, 2),'x')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(hexadeci,"\n")
                    print("==============================================")
                    break

        elif base == 3:
            while True:
                print("A que tipo quieres convertir el Hexadecimal")
                print("1 = Decimal")
                print("2 = binario")
                var_Conv = int(input())
                if var_Conv == 1:
                    num_hex = input("ingresa el numero hexadecimal que quieres convertir a decimal\n")
                    deci = int(num_hex, 16)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(deci,"\n")
                    print("==============================================")
                    break
                elif var_Conv == 2:
                    num_hex = input("ingresa el numero hexadecimal que quieres convertir a binario\n")
                    bina = bin(int(num_bin,16))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("==============================================")
                    print(bin,"\n")
                    print("==============================================")
                    break
        elif base == 4:
            return False











if __name__ == "__main__":
    main()
    
