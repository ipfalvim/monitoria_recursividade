def countdown (start):
    if start <= 0:
        print("DECOLAR!")
    else:
        print(start)
        countdown(start-1)


def main():
    countdown(10)

if __name__ == '__main__':
    main()
    