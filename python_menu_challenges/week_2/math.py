# Define a class for Checking odd number
class Check:
  # Constructor
  def __init__(self):
    return
  # define a method for checking number is odd or not
  def __call__(self,num):
    for i in range(2, int(num ** (1/2)) + 1) :
      if num % i == 0 and num != i:
        return False
      else:
        return True

    # if number is odd then return True
    
# input number
# make an object of Check class
check_prime = Check()
# method calling

print("is 16 an odd number? ", check_prime(16))
print("is 100 a odd number? ", check_prime(100))
print("is 5 a odd number? ", check_prime(5))
print("is 7 a odd number? ", check_prime(7))
print("is 1099 a odd number? ", check_prime(109))
print("is 110 a odd number? ", check_prime(110))





