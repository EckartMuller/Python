def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]#(3549 // 1000 => div = 3),(549 // 500 => div = 1)
        number %= num[i]#number = number % num[i]
        #number(new) = 549
        #number(new) = 49

        while div:
            print(sym[i], end="")#i = 12
            div -= 1#div = 2
        i -= 1#i = 11


number = 3549
print("Roman value is:", end=" ")
printRoman(number)
