

#
# #fibonocii
#
# def f(n):
#     a,b=0,1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
#
# #f(8)
#
# def fact(n):
#     if n<0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

#for i in range(10):
    #print(fact(i))


#swap
#
# def swap(a,b):
#     a=a^b
#     b=a^b
#     a=a^b
#     return a,b
# print(swap(2,3))
#
# a,b=2,3
# a,b=b,a
# print(a,b)

#reverse string without string fun

# def rev(s):
#     r=""
#     l = len(s)
#     for i in range(l):
#         r=r+s[l-1]
#         l-=1
#     return r
#     #return s[::-1]
# print(rev("abcd"))

def star(n):
#     a = '* '
#     len =n
#     # for i in range(len):
#     #     print(a*n)
#     #     n=n-1
#     #
#     # for i in range(len):
#     #     print(a*i)
#     # print("\n\n")
#     # number of spaces
    k =  2*n -1
    for i in range(0, n):
        for j in range(0, k+1):
            print(" ",end=""),
            k = k - 1
        for j in range(0, i + 1):
            print("* ".format(i),end=' ')
    print("\r",end="")



def num(n):
#     a = '* '
#     len =n
#     # for i in range(len):
#     #     print(a*n)
#     #     n=n-1
#     #
#     # for i in range(len):
#     #     print(a*i)
#     # print("\n\n")
#     # number of spaces
    k =  2*n
    for i in range(0, n):
        k=n
        for j in range(0, int(k/2)):
            print(" ",end=""),
        #k = k - 1
        for j in range(0, i + 1):
            print("{} ".format(i),end=""),
        print("\r")
def num2(n):
#     a = '* '
#     len =n
#     # for i in range(len):
#     #     print(a*n)
#     #     n=n-1
#     #
#     # for i in range(len):
#     #     print(a*i)
#     # print("\n\n")
#     # number of spaces
    k =  n-1
    for i in range(0, n):
        for j in range(0, k):
            print(" ",end=""),
        k = k - 1
        for j in range(0, i + 1):
            print("{} ".format(i),end=""),
        print("\r")
def letter(n):
    st=65
    k=n-1
    for i in range(0,n):
        for j in range(0,i+1):
            print("{}".format(chr(st)),end="")
        print("\r")
        st+=1

num(10)
star(10)
num2(10)
letter(5)
#num_star.py
#Displaying num_star.py.
