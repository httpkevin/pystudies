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

<h1>Python Lambda</h1>
Podemos considerar que a função lambda é uma função anonima. Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

~~~python
lambda arguments : expression 
~~~

Exempo:
~~~python 
x = lambda a: a + 10 
print(x(5))
~~~

As funções do Lambda podem receber qualquer número de argumentos. 
Multiplique o argumento "a" pelo argumento "b" e retorne o resultado:

~~~python 
x = lambda a, b : a * b
print(x(5, 6))
~~~

Resuma os argumentos "a", "b" e "c" retorna o resultado:

~~~python 
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
~~~

O poder de lambda é melhor mostrado quando você os usa como uma função anônima dentro de outra função. 
Use a mesma definição de função para fazer uma função que sempre triplica o número que você envia:

~~~python
def funcao(n):
  return lambda a : a * n 

dobro = funcao(2)
triplo  = funcao(3)

print(dobro(2))
print(triplo(2))
~~~

<h1>Python Arrays</h1>
Um Array (matriz) é uma variável especial, que pode conter mais de um valor por vez.

~~~python
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)
~~~

| Métodos | Descrição |
| --- | --- |
| append() | Adiciona um elemento no final da lista |
| clear() | Remove todos os elementos da lista |
| copy() | Retorna uma cópia da lista |
| count() | Retorna o número de elementos com o valor especificado |
| extend() | Adicionar os elementos de uma lista (ou qualquer iterável) ao final da lista atual |
| index() | Retorna o índice do primeiro elemento com o valor especificado |
| insert() | Adiciona um elemento na posição especificada |
| pop() | Remove o elemento na posição especificada |
| remove() | Remove o primeiro item com o valor especificado |
| reverse() | Inverte a ordem da lista |
| sort() | Classifica a lista |

<h1>Python Classes/Objetos</h1>
Uma grande parte em Python é relacionado a objetos, com suas propriedades e métodos. Podemos dizer que uma classe é como um construtor de objetos.

~~~python
class myClass:
  x = 10 

print(x)
~~~

Um exemplo simples para demostrar objetos, construi uma classe na qual cria objetos:

~~~python
class myClass:
  x = 10 

p1 = myClass()
print(p1.x)
~~~

<h1>The __init__() Function</h1>
Os exemplos acima são classes e objetos em sua forma mais simples e não são realmente úteis em aplicações da vida real.
Todas as classes possuem uma função chamada __init__(), que sempre é executada quando a classe está sendo iniciada. Use a função __init__() para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado:


~~~python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 

p1 = Person("Kevin", 27)

print(p1.name)
print(p1.age)
~~~

<h1>The __str__() Function</h1>
A função __str__() controla o que deve ser retornado quando o objeto de classe é representado como uma string. Se a função __str__() não for definida, a representação de string do objeto é retornada:

A representação de string de um objeto SEM a função __str__():

~~~python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 

p1 = Person("Kevin", 27)

print(p1)
~~~

A representação de string de um objeto COM a função __str__():

~~~python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
    
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Kevin", 27)

print(p1)
~~~


<h1>Métodos de objetos</h1>

Os Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.
Inserindo uma função que imprima uma saudação e execute-a no objeto p1.

Exemplo:
~~~python 
class Person:
  def __init__(self, name, age):
    self.name = name 
    self.age = age 
    
  def myfunc(self):
    print("Olá,  meu nome é " + self.name)
  
p1 = Person("Kevin", 00)
p1.myfunc()
~~~

<h1>Parametro Self</h1>
O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis ​​pertencentes à classe.

Ele não precisa ser chamado de self, podemos chamá-lo como quiser, porém deve ser o primeiro parâmetro de qualquer função da classe:

~~~python
class Person:
  def __init__(test, name, age): #utilizando "test" no lugar do self
    test.name = name 
    test.age = age 
    
  def myfunc(abc):
    print("Olá,  meu nome é " + abc.name)
  
p1 = Person("Kevin", 00)
p1.myfunc()
~~~

<h1>Python JSON</h1>

Em Python tem um pacote embutido chamado json, já que JSON normalmente é escrito em JS e com isso podemos usar para trabalhar com dados JSON.

Importando modulo JSON: 
~~~python 
import json
~~~

<h1>Convertendo de PY para JSON</h1>
Se tiver um objeto Python, poderá convertê-lo em uma string JSON usando o método json.dumps().

~~~python
import json 

# um objeto em py:
x = {
  "nome": "Kevin",
  "Idade": 27,
  "Cidade": "Nova York"
}

# convertendo em JSON:
y = json.dumps(x)

# o resultado 
print(y)
~~~

Podemos converter objetos Python dos seguintes tipos em strings JSON: 

- dict 
- list 
- tuple
- string 
- int 
- float 
- True 
- False 
- None 

~~~python
import json 

print(json.dumps({"nome": "Kevin", "idade": 30}))
print(json.dumps(["maca", "banana"]))
print(json.dumps(("maca", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
~~~

Um exemplo legal também, é convertendo um objeto python contendo todos os tipos de dados legais:

~~~python 
import json 

x = {
  "nome": "Kevin",
  "idade": 27,
  "casado": False,
  "divorciado": False,
  "pets": ("POPO", "Tico", "Sofis"),
  "filhos": None,
  "cars": [
    {"modelo1": "bmw 230"},
    {"modelo2": "camaro"}
  ] 
}

print(json.dumps(x))
~~~

<h1>Formatando o Resultado</h1>

O exemplo acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha. 

O "json.dumps() o método possui parâmetros para facilitar a leitura do resultado.

Usando o "indent" parâmetro para definir o número de recuos:

~~~python
json.dumps(indent=4)
~~~

Podemos também definir os separadores, o valor padrão é (", ", ": "), o que significa usar uma vírgula e um espaço para separar cada objeto, e dois pontos e um espaço para separar as chaves dos valores:

~~~python 
json.dumps(x, indent=4, separators=(". ", " = "))
~~~

<h1>Ordenando o resultado</h1>
O método json.dumps() possui parâmetros para ordenar as chaves no resultado:

Exemplo:
Usando o parâmetro "sort_keys" para especificar se o resultado deve ser classificado ou não:

~~~python
json.dumps(x, indent=4, sort_keys=True)
~~~

Resultado final:

~~~python
import json 

x = {
  "nome": "Kevin",
  "idade": 27,
  "casado": False,
  "divorciado": False,
  "pets": ("POPO", "Tico", "Sofis"),
  "filhos": None,
  "cars": [
    {"modelo1": "bmw 230"},
    {"modelo2": "camaro"}
  ] 
}

print(json.dumps(x, indent=4, sort_keys=True, separators=(". ", " = ")))

#resultado do print
{
    "cars" = [
        {
            "modelo1" = "bmw 230"
        }. 
        {
            "modelo2" = "camaro"
        }
    ]. 
    "casado" = false. 
    "divorciado" = false. 
    "filhos" = null. 
    "idade" = 27. 
    "nome" = "Kevin". 
    "pets" = [
        "POPO". 
        "Tico". 
        "Sofis"
    ]
}
~~~







