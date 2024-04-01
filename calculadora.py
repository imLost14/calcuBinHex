import numpy as np


#def conv_dec_bin



def main():
    print("BIENVENIDO A LA CALCULADORA BINARI-HEXA")
    print("Debes elegir el tipo de dato que deseas convertir")
    print("1, Para decimal")
    print("2, para binario")
    print("3, para Hexadecimal")
    base = int(input())
    
    if int(base) == 1:
        print("A que tipo quieres convertir el decimal")
        print("1 = Binario")
        print("2 = Hexadecimal")
        var_Conv = int(input())
        if var_Conv == 1:
            num_Dec = int(input("Ingresa el numero que quieres convertir a binario\n"))
            bina = np.binary_repr(num_Dec)
            print(bina)
            

if __name__ == "__main__":
    main()
    
