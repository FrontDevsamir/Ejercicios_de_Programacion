

class Vertice :


    def __init__(self, clave, color= None) :

        self.clave = clave 
        self.color = color
        self.vecinos = []



class Grafo :

    def __init__(self) :

        self.vertices = []

    
    def add_vertice(self, vert) :

        self.vertices.append(vert)

    def add_arista(self, a, b) :
        
        a.vecinos.append(b)


    
    def adyacentes(self, pais) :

        return [vecino.color for vecino in pais.vecinos]



    def show(self) :

        for i in self.vertices :
            print('VERTICE ~ ', i.clave)
            for j in i.vecinos :
                print(j.clave, end=' - ')

            print()
            print('----------------------------------------------------------------')





def valido(pais, color, coloreados) :

    adyacentes = mapa.adyacentes(pais)
    if adyacentes :

        if color not in adyacentes :
            return True
    return False



def coloreo(paises, colores, coloreados= {}, ind_pais= -1) :

    if len(paises) == len(coloreados) :
        print('----------------------------------------------------------------')
        c = 0
        for i in coloreados :
            if c <= 2 :
                print(coloreados[i] ,end=" - ")
                if c == 2 :
                    print() 
            elif c <= 5 :  
                print(coloreados[i] ,end=" - ")
                if c == 5 :
                    print() 
            else :
                print(coloreados[i] ,end=" - ")
            c += 1

        input() 
        return True

    pais = ind_pais + 1

    for color in colores :

        if valido(paises[pais], color, coloreados) :

            coloreados[lista_paises[pais].clave] = color
            paises[pais].color = color

            coloreo(paises, colores, coloreados, pais)

            coloreados.pop(lista_paises[pais].clave)
            paises[pais].color = None 
    return False








paises = [
    [Vertice('PERU'), Vertice('CHILE'), Vertice('COLOMBIA')],
    [Vertice('TACNA'), Vertice('PUNO'), Vertice('MADRID')],
    [Vertice('BOGOTA'), Vertice('ESPAÑA'), Vertice('TUMBES')]
]


mapa = Grafo()

for i in paises :

    for j in i :

        mapa.add_vertice(j) 


mapa.add_arista(
    paises[0][0], paises[0][1]
    )
mapa.add_arista(
    paises[0][0], paises[1][0]
    )
mapa.add_arista(
    paises[0][0], paises[1][1]
    )

mapa.add_arista(
    paises[0][1], paises[0][0]
    )
mapa.add_arista(
    paises[0][1], paises[0][2]
    )
mapa.add_arista(
    paises[0][1], paises[1][0]
    )
mapa.add_arista(
    paises[0][1], paises[1][1]
    )
mapa.add_arista(
    paises[0][1], paises[1][2]
    )

mapa.add_arista(
    paises[0][2], paises[0][1]
    )
mapa.add_arista(
    paises[0][2], paises[1][1]
    )
mapa.add_arista(
    paises[0][2], paises[1][2]
    )

mapa.add_arista(
    paises[1][0], paises[0][0]
    )
mapa.add_arista(
    paises[1][0], paises[0][1]
    )
mapa.add_arista(
    paises[1][0], paises[1][1]
    )
mapa.add_arista(
    paises[1][0], paises[2][0]
    )
mapa.add_arista(
    paises[1][0], paises[2][1]
    )

mapa.add_arista(
    paises[1][1], paises[1][0]
    )
mapa.add_arista(
    paises[1][1], paises[1][2]
    )
mapa.add_arista(
    paises[1][1], paises[0][0]
    )
mapa.add_arista(
    paises[1][1], paises[0][1]
    )
mapa.add_arista(
    paises[1][1], paises[0][2]
    )
mapa.add_arista(
    paises[1][1], paises[2][0]
    )
mapa.add_arista(
    paises[1][1], paises[2][1]
    )
mapa.add_arista(
    paises[1][1], paises[2][2]
    )

mapa.add_arista(
    paises[1][2], paises[1][1]
    )
mapa.add_arista(
    paises[1][2], paises[0][1]
    )
mapa.add_arista(
    paises[1][2], paises[0][2]
    )
mapa.add_arista(
    paises[1][2], paises[2][1]
    )
mapa.add_arista(
    paises[1][2], paises[2][2]
    )

mapa.add_arista(
    paises[2][0], paises[2][1]
    )
mapa.add_arista(
    paises[2][0], paises[1][0]
    )
mapa.add_arista(
    paises[2][0], paises[1][1]
    )

mapa.add_arista(
    paises[2][1], paises[2][0]
    )
mapa.add_arista(
    paises[2][1], paises[2][2]
    )
mapa.add_arista(
    paises[2][1], paises[1][0]
    )
mapa.add_arista(
    paises[2][1], paises[1][1]
    )
mapa.add_arista(
    paises[2][1], paises[1][2]
    )

mapa.add_arista(
    paises[2][2], paises[2][1]
    )
mapa.add_arista(
    paises[2][2], paises[1][1]
    )
mapa.add_arista(
    paises[2][2], paises[1][2]
    )



lista_paises = [pais for i in paises for pais in i]
colores = ['ROJO', 'VERDE', 'AZUL', 'AMBAR']

print(coloreo(lista_paises, colores))

