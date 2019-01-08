
"""
try:
    for i in ['a', 'b', 'c']:
        print(i**2)

except:
    print("Something went wrong")
finally:
    print("I always run")
"""
"""
try:
    x = 5
    y = 0
    z = x/y

except ZeroDivisionError:
    print("You can't divide by 0")

except:
    print("Something went wroong!")

finally:
    print("I always run!")
"""


def ask():
    x = int(input("Give me integer: "))
    result = x ** 2

while True:
    try:
        ask()
    except TypeError:
        print("It's not an integer!")
    except:
        print("Something went wrong!")
    else:
        print("Thank you!")
        break
    finally:
        print("Let's do it again!")
