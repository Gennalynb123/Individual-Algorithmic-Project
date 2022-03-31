
# Python 3 program to find
# factorial of given number
def factorial(n):

    # Checking the number
    # is 1 or 0 then
    # return 1
    # other wise return
    # factorial
    if (n==1 or n==0):

        return 1

    else:

        return (n * factorial(n - 1))

def Test():
    # Driver Code
    num = 5;
    print("number : ",num)
    print("Factorial : ",factorial(num))


def drive():
    Test()

if __name__ == "__main__":
    drive()