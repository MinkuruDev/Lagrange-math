import math

def addUp(arr1, arr2):
    result = []
    a1 = arr1.copy()
    a2 = arr2.copy()

    while(len(a1) != len(a2)):
        if len(a1) > len(a2):
            a2.append(0)
        else:
            a1.append(0)

    for i in range(len(a1)):
        result.append(a1[i] + a2[i])
    return result

def arrMultipleNumber(arr, n):
    a = arr.copy()
    for i in range(len(a)):
        a[i] *= n
                
    return a    

def arrMultipleArr(arr1, arr2):
    a1 = arr1.copy()
    a2 = arr2.copy()
    result = []
    for i in a1:
        result = addUp(result, arrMultipleNumber(a2, i))
        a2.insert(0, 0)

    return result

def printPolynomial(arr):
    result = ""
    i = len(arr)
    while i>0:
        i-=1
        result += str(round(arr[i], 3)) + "x^" + str(i) + " "

    print(result)

def findLagrangePolynomial(n,x,y):
    gl_numerator = []

    for k in range(n):
        numerator = [1]
        denominator = 1
        for i in range(n):
            if i==k:
                continue
            numerator = arrMultipleArr(numerator, [-x[i], 1])
            denominator *= x[k] - x[i]

        numerator = arrMultipleNumber(numerator, y[k]/denominator)
        gl_numerator = addUp(numerator, gl_numerator)

    return gl_numerator

def replaceXtoPolynomial(poly, x):
    result = 0
    for i in range(len(poly)):
        result += poly[i] * x**i

    return result

def main():
    fi = open("input.txt", "r")
    n = int(fi.readline())
    x = fi.readline().split(" ")
    y = fi.readline().split(" ")
    for i in range(n):
        x[i] = eval(x[i])
        y[i] = eval(y[i])

    lagrangePolynomial = findLagrangePolynomial(n, x, y)
    printPolynomial(lagrangePolynomial)

    while True:
        x0 = input("input x to find f(x) (type '00' to quit): ")
        if x0 == "00":
            break
        x0 = eval(x0)
        res = replaceXtoPolynomial(lagrangePolynomial, x0)
        print("f({x0:.3f})= {res:.3f}".format(x0 = x0, res= res))
        input("press ENTER to continue")
    

if __name__ == "__main__":
    main()