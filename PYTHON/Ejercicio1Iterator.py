import sys
class Vector2:
    def __init__(self,valores):
        self._datos = [0 for x in range(valores)]
        
    def getValor(self,pos):
        return self._datos[pos]

    def setValor(self,pos, valor):
        self._datos[pos] = valor 

    def dimension(self):
        return len(self._datos)
    
    def iterador(self):
        return IteradorVector(self)

class IteradorVector:
    def __init__(self,vector):
        self._vector = vector._datos
        self._posicion = 0

    def hasNext(self):
        if (self._posicion < len(self._vector)):
            return True
        else:
            return False

    def next(self):
        self.valor = self._vector[self._posicion]
        self._posicion =  self._posicion + 1
        return self.valor


if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    print("\nIngrese el tipo de materia laboratorio o teorica (l/t):",end=" ")
    dato = input().lower()
    if dato == "l":
        notaFinal = 0
        print("La materia cuenta con auxiliatura(s/n):", end=" ");
        aux = input().lower()
        notaAux = 0
        if (aux == "s"):
            notaAux = int(input("Ingrese cuanto vale la auxiliatura: "))
        numTot = int(input("Ingrese el numero de laboratorios: "))
        notaLab = int(input("Ingrese la nota que vale un laboratorio: "))
        nota= int(notaLab*numTot)
        notaEst = 0
        print()
        for i in range(0,numTot):
            notaEst=notaLab+1
            while notaEst>notaLab:
                notaEst= int(input("Ingrese la nota obtenida en el " + str(i+1) + "º laboratorio: "))
                if(notaEst>notaLab):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaEst
        notaAuxEst = 0
        if (aux == "s"):
            notaAuxEst = notaAux + 1
            while (notaAuxEst > notaAux):
                notaAuxEst = int(input("Ingrese la nota de auxiliatura: "))
                if (notaAuxEst > notaAux):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaAuxEst
        print("\nNOTA FINAL DE LABORATORIO: ", notaFinal)
        if notaFinal > nota/2:
           print("El estudiante",nombre,"APROBO")
        else:
            print("El estudiante",nombre,"REPROBO")
    else:
        notaFinal = 0
        print("La materia cuenta con auxiliatura(s/n):", end=" ");
        aux = input().lower()
        notaAux = 0
        if (aux == "s"):
            notaAux = int(input("Ingrese cuanto vale la auxiliatura: "))
        numTot = int(input("Ingrese el numero de parciales: "))
        nota = 0
        notaEst = 0
        notaTeo = Vector2(numTot)
        #Llenado del vector de notas notaTeo
        for i in range (0,numTot):
            notaP = int(input("Ingrese por cuanta nota evaluara el "+ str(i+1) +"º parcial: "))
            notaTeo.setValor(i, notaP)
            nota += notaTeo.getValor(i)
        print()
        #Recorrido del vector de notas notaTeo con IteratorVector        
        iterador = notaTeo.iterador()
        i = 0
        while (iterador.hasNext()):
            notaParcial = int(iterador.next())
            notaEst=sys.maxsize
            while notaEst>notaTeo.getValor(i):
                notaEst= int(input("Ingrese nota obtenida en el " + str(i+1) + "º parcial: "))
                if(notaEst>notaParcial):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaEst
            i = i + 1
        notaAuxEst = 0
        if (aux == "s"):
            notaAuxEst = notaAux + 1
            while (notaAuxEst > notaAux):
                notaAuxEst = int(input("Ingrese la nota de auxiliatura: "))
                if (notaAuxEst > notaAux):
                    print("¡Nota no valida!")
            notaFinal = notaFinal + notaAuxEst
        print("\nNOTA FINAL:", notaFinal)
        if notaFinal > nota/2:
           print("El estudiante",nombre,"APROBO")
        else:
            print("El estudiante",nombre,"REPROBO")
