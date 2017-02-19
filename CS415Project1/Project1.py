# all the computations for HW 1 shall be done using binary arithmetic
# only the user input and the final output will be in decimal.
# the two functions dec2bin and bin2dec provide I/O conversion between
# binary and decimal.

# functions provided: Add, Mult, divide and many supporting functions such as
# Compare to compare two unbounded integers, bin2dec and dec2bin etc.

# missing functions: sub which performs subtraction and Divide which is the decimal version
# of divide, and also a solution to Problem 3.

########################################################
### SAMPLE INPUT/OUTPUT                             ###
########################################################
#>> > Problem1(99, 101, 101, 99)
#3621042145110495340304913321770092884828963481118630680783443137199360424701178235489444339150903695510140270221458360654677736177726261420668704432019096568923217654887729426654819147812495289601990198L

#>> > Problem1(101, 100, 102, 101)
#-73624909023231670869261708087644352879856062771895622746310308401235838873720979357266761267201142320719562605934027588808477220968934718015196126899431090054281838673459558997083139194957867884875198351L
#>> > Problem2(921, 97, 376, 49)
#(
##223346796471162164452913306468608511973357088088077011223389370777657713512498752849853123746821473506392127360180733334528455377517683142902106402854175807704081L,
#868589458788803459890025777897148259540992011101528169885851420031124037456917859918715079950453053934476646860356569316780185L)
#>> > Problem3(71)
#(3028810706851429109067025637383L, 624893729741902836283505236800L)
#>> >
##########################################################

import random
import sys
import time

sys.setrecursionlimit(10000000)

from random import *


def shift(A, n):
    if n == 0:
        return A
    return [0] + shift(A, n - 1)


def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))
    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))


def Mult(X, Y):
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1, Y1))


def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True


def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]


def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def add(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1) - len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1) - len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C


def Add(A, B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))


def sub(A, B):
    n = len(A)
    m = len(B)
    if n < m:
        for j in range(m - n):
            A.append(0)
    else:
        for j in range(n - m):
            B.append(0)
    C = add(A, add(flipbits(B), [1]))
    C.pop()
    return C


def flipbits(A):
    for i in range(len(A)):
        if A[i]:
            A[i] = 0
        else:
            A[i] = 1
    return A


def exc_or(a, b, c):
    return (a ^ (b ^ c))


def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0


def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val


def reverse(A):
    B = A[::-1]
    return B


def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0


def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))


def dec2bin(n):
    if n == 0:
        return []
    m = n / 2
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A


def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([], [])
    (q, r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)
    if (not even(X)):
        r = add(r, [1])
    if (not compare(r, Y) == 2):
        r = sub(r, Y)
        q = add(q, [1])
    return (q, r)


def map(v):
    if v == []:
        return '0'
    elif v == [0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0, 1]:
        return '2'
    elif v == [1, 1]:
        return '3'
    elif v == [0, 0, 1]:
        return '4'
    elif v == [1, 0, 1]:
        return '5'
    elif v == [0, 1, 1]:
        return '6'
    elif v == [1, 1, 1]:
        return '7'
    elif v == [0, 0, 0, 1]:
        return '8'
    elif v == [1, 0, 0, 1]:
        return '9'


def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0, 1, 0, 1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))


def expo(A, B):
    print("Entering expo with values: " , bin2dec(A), bin2dec(B))
    if len(B) == 0:
        return [1]
    Z = expo(A, div2(B))
    if even(B):
        return mult(Z, Z)
    else:
        return mult(A, mult(Z, Z))


def problem1(A, B, C, D):
    # Input: 4 ints 0 < A, B, C, D < 1000. These ints will be in decimal form.
    # Output: A^B - C^D
    print("Inside problem1a... ")
    print("Values: ", reverse(A), reverse(B), reverse(C), reverse(D))
    AB = expo(A, B)
    CD = expo(C, D)

    if(bin2dec(CD) > bin2dec(AB)):
        print("Ture")
        temp = sub(CD, AB)
        print("temp: ", temp)
        if(temp[-1]==1):
            temp.append(0)
        print("temp: ", temp)
        temp = flipbits(temp)
        print("temp with flipbits: ", temp)
        twoscomp = add(temp, [1])
        print("twoscomp: ", twoscomp)
        return twoscomp
    else:
        subs = sub(AB, CD)
        return subs


def problem2(A, B, C, D):
    AB = expo(A, B)
    print("AB: ", bin2dec(AB))
    CD = expo(C, D)
    print("CD: ", bin2dec(CD))
    (q, r) = divide(AB, CD)
    # print("q, r: ", (q, r))
    return (q, r)


def main():

    # answer = problem1(dec2bin(25), dec2bin(25), dec2bin(24), dec2bin(2))
    answer = problem2(dec2bin(50), dec2bin(3), dec2bin(2), dec2bin(4))
    # answer = expo(dec2bin(24), dec2bin(3))
    print("result: ", (answer))


main()


