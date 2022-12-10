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

