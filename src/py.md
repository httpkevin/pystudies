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

[comment]: <> (https://www.w3schools.com/python/python_functions.asp)

