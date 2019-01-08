"""
for i in range(1, 101):
    if (i % 3) == 0 and not((i % 5) == 0):
        print("Fizz")
    elif not((i % 3) == 0) and (i % 5) == 0:
        print("Buzz")
    elif (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz")
    else:
        print(i)
"""
"""
st = 'Create a list of the first letters of every word in this string'
st2 = st.split(" ")
st3 = []
for i in st2:
    st3.append(i[0])

print(st3)
 
"""
"""

def myfunc(word):
    word2 = ""
    for i in range(len(word)):
        if i%2 == 0:
            word2 += word[i].lower()
        else:
            word2 += word[i].upper()
    return word2

myfunc('BonKaSobiElEzy')
"""
"""
def myfunc(a,b):
    if a%2 == 0 and b%2 == 0:
        if a > b:
            return b
        elif b > a:
            return a
    elif not (a%2 == 0) or not(b%2 == 0):
        if a > b:
            return a
        elif b > a:
            return b

print(myfunc(54,121))
"""
"""
def myfunc(string1, string2):
    if string1[0].upper() == string2[0].upper():
        return True
    else:
        return False

print(myfunc("Lima", "lama"))
"""
"""
def myfunc(a, b):
    if a == 20 or b == 20:
        return True
    elif a + b == 20:
        return True
    else:
        return False

print(myfunc(18,2))
"""
"""
def myfunc(string):
    string2 = ""
    for i in range(len(string)):
        if i == 0:
            string2 += string[i].upper()
        elif i == 3:
            string2 += string[i].upper()
        else:
            string2 += string[i]
    return string2

print(myfunc("macdonald"))
"""
"""
def master_yoda(string):
    string = " ".join(string.split(" ")[::-1])
    return string

print(master_yoda("We are ready"))
"""
"""
def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

print(almost_there(199))
"""
"""
def find_33(list):
    for i in range(len(list)):
        if list[i] == 3 and list[i+1] == 3:
            return True
    return False

list = [3, 4, 6, 3, 4, 2, 3, 3]
print(find_33(list))
"""
"""
def paper_doll(string):
    string2 = ""
    for i in range(len(string)):
        string2 += (string[i] * 3)
    return string2

print(paper_doll("Mateusz"))
"""
"""
def blackjack(a,b,c):
    numbers = (a, b, c)
    suma = sum(numbers)
    if suma <= 21:
        return suma
    elif (suma > 21) and (11 in (a, b, c)) and ((suma - 10) <= 21):
        return suma - 10
    else:
        return "BUST"

print(blackjack(9,9,9))
"""
"""
def summer(*args):
    suma = 0
    if  not args:
        return 0
    for i in args:
        if (i < 6) or (9 < i <= 11):
            suma += i
    return suma


print(summer())
"""
"""
def spy_game(*args):
    for i in range(0, len(args)-1):
        if args[i] == 0:
            for j in range(i+1, len(args)-1):
                if args[j] == 0:
                    for k in range(j+1, len(args)-1):
                        if args[k] == 7:
                            return True
    return False
"""
"""
def spy_game(nums):
    spy = [0, 0, 7, "x"]
    for num in nums:
        if num == spy[0]:
            spy.pop(0)
    return len(spy) == 1

print(spy_game([0, 4, 0, 7, 1, 5]))
"""
"""
def count_primes(x):
    primes = 0
    counter = 0
    for i in range(2, x + 1):
        for j in range(2, i + 1):
            if i%j == 0:
                counter += 1
            else:
                pass
        if counter == 1:
            primes += 1
        counter = 0
    return primes

print(count_primes(100))
"""
"""
def sphere(x):
    return (4/3) * 3.14 * x**3

print(sphere(2))
"""
"""
def ran_check(num, low, high):

    return (num <= high) and (num >= low)


print(ran_check(5, 2, 8))
"""
"""
def up_low(string):
    low_number = 0
    up_number = 0
    for l in string:
        if l.isupper():
            up_number += 1
        elif l.islower():
            low_number += 1
    return (print(f"Low number is: {low_number}, Up number is: {up_number}"))

up_low("MacDonald")
"""
"""
def unique_list(list):
    new_list = set(list)
    return print(new_list)

unique_list([2,2,4,5,6,7,2,2,3,3,5,5,6,6])
"""
"""
def multiply(num):
    result = 1
    for i in nums:
        result = result * i
    return result

numbers = [1, 2, 3, -4]
print(list(map(lambda num : num ** 2, numbers)))
"""
"""
def palindrome(s):
    if s[0] == s[len(s) - 1]:
        pass
    else:
        return False
    if len(s)%2 == 0:
        n = int(len(s)/2)
        print(n, " EVEN")
    else:
        n = int(len(s)/2 - 0.5)
        print(n)

    for i in range(n):
        if s[i] == s[::-i-1]:
            pass
        else:
            return False



name = "MatltaM"
print(palindrome(name))
"""
"""
import string

def ispangram(str1):
    str2 = ""
    for l in str1:
        if l.lower() in string.ascii_lowercase:
            if l.lower() not in str2:
                str2 += l.lower()
    if len(str2) == len(string.ascii_lowercase):
        return True
    else:
        return False


print(ispangram("The quick brown fox jumps ovet the lazy dog"))

print(string.ascii_lowercase)
"""
