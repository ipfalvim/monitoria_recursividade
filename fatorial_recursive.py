def fatorial(numero):
    
    if numero == 0:
        return 1
    else:
        return numero*fatorial(numero-1)

def main():
    numero = range(0,10)
    for n in numero:
        print(f"O fatorial de {n} é: {fatorial(n)}")

if __name__ == '__main__':
    main()
