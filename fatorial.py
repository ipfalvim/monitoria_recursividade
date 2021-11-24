def fatorial(numero):
    
    resultado = 1
    while numero>0:
        resultado = resultado * numero
        numero -= 1
    
    return resultado

def main():
    numero = range(0,10)
    for n in numero:
        print(f"O fatorial de {n} é: {fatorial(n)}")

if __name__ == '__main__':
    main()
