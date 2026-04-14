def is_prime(n):
  if n<=1:
    return False
  else:
    for i in range(2,(n**0.5)+1):
      if n%i==0:
        return False
  return True
n=int(input("enter the number")
if is_prime(n):
  print("prime")
else:      
  print("not prime")
