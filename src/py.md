<h1>Variavel Global</h1>

Variáveis ​​globais podem ser usadas por todos, tanto dentro de funções quanto fora:

~~~python
x = "Name:" #variavel global 

def myfunc():
    print (x, "Kevin")
    
myfunc()   
~~~

Quando criar uma variável com o mesmo nome dentro de uma função, esta variável será local, e só poderá ser utilizada dentro da função. A variável global com o mesmo nome permanecerá como estava, global e com o valor original.

~~~python
x = "Name: " #variavel global 

def myfunc():
    x = "Mendes" #variavel local
    print ("Sobrenome:", x)
    
myfunc()   

print(x + "Kevin")
~~~

<h1>Condições e Instruções if</h1>

~~~python
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
~~~

<h1>Funções em Python</h1>
Basicamente uma função é um bloco de código que só é excutado quando chamado. 

Em Python, uma função é definida usando a palavra-chave: def

As informações podem ser passadas para funções como argumentos.

Os argumentos são especificados após o nome da função, dentro dos parênteses. Podemos adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

~~~python
def entrada_dados(edados):
  print("nomes:" + edados)

entrada_dados("Kevin")
entrada_dados("Vick")
entrada_dados("Tico")
~~~

~~~python 
def entrada_dados(dados1, dados2, dados3): #entrada_dados(função) dados1(argumentos)
  print("dados:" + dados2)

entrada_dados(dados1 = "Vick", dados2 = "Kevin", dados3 = "Tico")
~~~

<h1>Passando uma lista como um argumento</h1>

 podemos enviar qualquer tipos de dados de argumento para uma função (string, número, lista, dicionário etc.) e eles serão tratados como o mesmo tipo de dados dentro da função.

 ~~~python
def function(food):
    for x in food:
        print(x)
        
food = ["Apple", "Banana", "Grape"]

function(food)
 ~~~

 <h1>Recursão</h1>
Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.
O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever uma função que nunca termina ou uma que usa quantidades excessivas de memória ou poder do processador.

~~~python
def tri_recursion(k): #tri_recursion() é uma função que definimos para chamar a si mesma ("recursão")
  if(k > 0): #variável k como dados, que decrementa (-1) toda vez que recursamos.
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
~~~
[comment]: <> (https://www.w3schools.com/python/python_functions.asp)

