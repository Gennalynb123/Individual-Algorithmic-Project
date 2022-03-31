class Factorial:
  def __init__(self):
    self.final = [1]
  def __call__(self,n):
    if n < len(self.final):
      return 1
    else:
      f_number = n * self(n-1)
      self.final.append(f_number)
    return self.final[n]

obj = Factorial()
n = int(input("n = "))
print(obj(n))