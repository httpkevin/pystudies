#teste

a = int(input()) #entrada de dados (numero)
b = int(input()) #entrada de dados (numero)

#primeira condição
if a > b:
    print ("o primeiro valor é maior que o segundo")
#segunda condição (meio termo)  
elif a == b:
    print ("o primeiro valor é igual o segundo")
#terceira condição
else:
    print ("o segundo valor é maior que o primeiro")

def function(food):
    for x in food:
        print(x)
        
food = ["Apple", "Banana", "Grape"]

function(food)

#função de recursão 
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 4)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)
    

    

     
    

