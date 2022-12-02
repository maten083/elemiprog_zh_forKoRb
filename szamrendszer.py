#ez a függvény bekér egy egészszámot majd 8-as számrendszerbe pakolja
# A nyomorult lépéseket is fogja mutatni
def to8(num):
    digits = 0
    tempnum = num
    while tempnum != 0:
        tempnum //= 10
        digits += 1

    current = num
    remainders = ""
    strFormat = '{:>' + str(digits) + '} | {}'

    print(strFormat)
    while current > 0:
        remainder = current % 8
        print(strFormat.format(str(current), str(remainder)))
        current //= 8
        remainders += str(remainder)

    return (remainders[::-1]) + "₈"  #visszafelé kiírjuk a maradékokat

#print(to8(867))

num = int(input("decimal to octal: "))
print(to8(num))