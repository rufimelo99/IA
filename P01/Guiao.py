#Desenvolvimento de funcoes
#Funcoes para processamento de listas

#1:Dada uma lista, retorna o seu comprimento.
lista = [1,2,3,4,5]

def comprimento(lista):
    if lista == []:
        return 0
    return 1+comprimento(lista[1:])

#2 Dada uma lista de n´umeros, retorna a respectiva soma
def soma(lista):
    if lista == []:
        return 0
    return lista[0]+soma(lista[1:])


#3 Dada uma lista e um elemento, verifica se o elemento ocorre na lista. Retorna um valor booleano
def existe(lista, elem):
    if lista == []:
        return False
    if lista[0] == elem:
        return True
    return existe(lista[1:], elem)
    #return lista[0] == elem or existe(lista[1:], elem)

#4 Dadas duas listas, retorna a sua concatena¸c˜ao.

l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]

def concatenacao(l1, l2):
    if l1 == []:
        return l2
    if l2 == [] :
        return l1
    l1.append(l2[0])
    
    return concatenacao(l1, l2[1:])

#5 Dada uma lista, retorna a sua inversa.
def inv(lista):
    if lista == []:
        return []
    return inv(lista[1:]) + [lista[0]]

    


#6 Dada uma lista, verifica se forma uma capicua, ou seja, se, quer se leia da esquerda para a direita ou vice-versa, se obtˆem a mesma sequˆencia de elementos.
def capicua(lista):
    if lista == []:
        return True
    if lista[0]!=lista[-1]:
        return False
    return capicua(lista[1:-1])

#7 Dada uma lista de listas, retorna a concatena¸c˜ao dessas listas
def conc_listas(l1, l2):
    if len(l1) != len(l2):
        return None
    if l1 == []:
        return []
    
    
    return [l1[0], l2[0]] + conc_listas(l1[1:], l2[1:])


#8 Dada uma lista, um elemento x e outro elemento y, retorna uma lista similar `a lista de entrada, na qual x ´e substituido por y em todas as ocorrˆencias de x.

def switch(x,y,lista):
    if lista == []:
        print("over")
        return []
    if lista[0] == x:
        return [y] + switch(x,y,lista[1:])
    return [lista[0]] + switch(x,y,lista[1:])


#9 Dadas duas listas ordenadas de n´umeros, calcular a uni˜ao ordenada mantendo eventuais repeti¸c˜oes.

def ordenacao_2listas(l1,l2):
    
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]]+ordenacao_2listas(l1[1:],l2[:])
    else:
        return [l2[0]]+ordenacao_2listas(l1[:],l2[1:])

#10. Dado um conjunto, na forma de uma lista, retorna uma lista de listas que representa o conjunto de todos os subconjuntos do conjunto dado.
#???????
#def listas_de_listas(lista):
#    if lista == []:
#        return []
#    for i in lista:
#        return [[i]+listas_de_listas(lista[0:i:]) ]
#
#
#
#



#Exec
print("-----EX 1------")
print(comprimento(lista))
print(soma(lista))
print(existe(lista, 3))
print(concatenacao(l1, l2))
print(inv(lista))
teste_capicua1 = [1,2,3,3,2,1]
teste_capicua2 = [1,2,3,2,1]
print(capicua(teste_capicua1))
print(capicua(teste_capicua2))
print(conc_listas(l1, l2))
print(switch(2,10,lista))
l1=[1,3,6,7]
l2=[2,4,5,8]
print(ordenacao_2listas(l1,l2))


#Fun¸c˜oes para processamento de listas e tuplos

#1 Dada uma lista de pares, produzir um par com as listas dos primeiros e segundos elementos desses pares. 
#separar ([( a1, b1), ... (an, bn)]) = ([a1, ... an], [b1, ... bn])

#solucao nao recursiva

lista_de_tuplos = [(1,4), (2,8), (3, 12)]
def separar(lista_de_tuplos):
    if lista_de_tuplos == []:
        return [[],[]]
    tempA=[]
    tempB=[]
    for i in range(len(lista_de_tuplos)):
        tempA.append(lista_de_tuplos[i][0])
        tempB.append(lista_de_tuplos[i][1])
    return [tempA, tempB]


#2. Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos de l diferentes de x e pelo n´umero de ocorrˆencias x em l.
#Exemplo:
#>>> r em o v e e c o n t a ( [ 1 , 6 , 2 , 5 , 5 , 2 , 5 , 2 ] , 2 )
#( [ 1 , 6 , 5 , 5 , 5 ] , 3 )


def remove_e_conta(lista, x):
    if lista==[]:
        return [], 0

    l, counter = remove_e_conta(lista[1:], x)

    if lista[0] == x:
        return l, counter+1
    else:
        return [lista[0]] + l, counter 

#3. Dada uma lista, retorna o n´umero de ocorrˆencias de cada elemento, na forma de uma lista
#de pares (elemento,contagem).
#print incorreto

def mapear(lista):
    if lista==[]:
        return [], 0 
    
    return (lista[0], remove_e_conta(lista, lista[0])[1]) , mapear(lista[1:])



#Exec
print("-----EX 2------")
print(separar(lista_de_tuplos))
print(remove_e_conta(lista, 1))
print(mapear(lista))


# Fun¸c˜oes que retornam None

#1. Dada uma lista, retornar o elemento que est´a `a cabe¸ca (ou seja, na posi¸c˜ao 0)
def cabeca(lista):
    if lista == []:
        return None
    return lista[0]

#2. Dada uma lista, retornar a sua cauda (ou seja, todos os elementos `a excep¸c˜ao do primeiro).


def cauda(lista):
    if lista == []:
        return None
    return lista[1:]
  
#3. Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos hom´ologos.
#??

#4. Dada uma lista de n´umeros, retorna o menor elemento

def menor(lista):
    if lista == []:
        return None
    if len(lista)==1:
        return lista[0]
    min = menor(lista[1:])

    if lista[0]< min:
        return lista[0]

#5.Dada uma lista de n´umeros, retorna um par formado pelo menor elemento e pela lista dos restantes elementos
#??? erro
def menor_e_lista(lista):
    if lista == []:
        return None
    if len(lista)==1:
        return [], lista[0]
    
    l, min = menor_e_lista(lista[1:])

    if lista[0]< min:
        return lista[1:], lista[0]

#6. Dada uma lista de n´umeros, calcular o m´aximo e o m´ınimo, retornando-os num tuplo.

def min_max(lista):
    if lista==[]:
        return None
    if len(lista)==1:
        return lista[0], lista[0]
    min, max = min_max(lista[1:])

    if lista[0]<min:
        return l1[0], max
    elif lista[0]>max:
        return min, lista[0]
    else:
        return min, max

#7. Dada uma lista de n´umeros, retorna um triplo formado pelos dois menores elementos e pela
#lista dos restantes elementos
#???

def min2_lista(lista):
    if lista==[] or len(lista)==1:
        print("oi")
        return None
    
    elif len(lista)==2:
        print("oi")
        if lista[0]<lista[1]:
            return lista[0], lista[1], []
        else:
            return lista[1], lista[0], []
    else:
        min1, min2, l = min2_lista(lista[1:])

        if lista[0] < min1 and lista[0]< min2:
            return lista[0], min1, lista[1:].append(min2)
        elif lista[0] < min2:
            return min1, lista[0], lista[1:].append(min2)
        else:
            return min1, min2, lista[:]


#Exec

print("-----EX 3------")
print(cabeca(l1))
print(menor(lista))
print(menor_e_lista(lista))
print(min_max(lista))
print(min2_lista(lista))