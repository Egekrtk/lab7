import maath_utils;
x = int(input("give number"))
y = int(input("give number"))

def main():
    print(maath_utils.add(x, y))
    print(maath_utils.substract(x, y))
    print(maath_utils.power(x, y))
    print(maath_utils.divide(x, y))
    print(maath_utils.mod(x, y))

if __name__ == "__main__" :
    main()
