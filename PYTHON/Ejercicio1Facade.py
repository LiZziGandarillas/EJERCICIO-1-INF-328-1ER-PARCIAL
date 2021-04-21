from __future__ import annotations


class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
    

        results = []
        results.append("FACHADA FINALIZADA")
        print("INICIALIZANDO FACHADA")
        if (self._subsystem1.operation1()) == "laboratorio":
            results.append(self._subsystem1.operation2())
            results.append(self._subsystem2.operation3())  
        else:
            results.append(self._subsystem1.operation2())
            results.append(self._subsystem2.operation4()) 
         
        return "\n".join(results)



class Subsystem1:

   
    def operation1(self) -> str:
       print("ingrese el tipo de materia a evaluar laboratorio o teorico")
       dato = input()
       if dato == "laboratorio":
        return "laboratorio"
       else:
           return "teoricas"
    def operation2(self) -> str:
         print ("ingrese el nombre del estudiante")
         nombre = input()
         return nombre




class Subsystem2:
    

    def operation3(self) -> str:
        nl = int(input("ingrese el numero de laboratorios a evaluar "))
        nl2 = int(input("ingrese por cuanta nota se evaluara los laboratorio "))
        t= int(nl2*nl)
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota del laboratorio obtenida por el estudiante :  "))
            total = total + nt
        print("nota final")
        print(total)
        if total > t/2:
           return "aprobado"
        else:
           return "reprobado"

    def operation4(self) -> str:
        nl = int(input("Ingrese el numero de examnes que tomara"))
        print("ingrese por cuanta nota elvaluara cada examen")
        t = 0
        for j in range (0,nl):
           nl2 = int(input("por cuanta nota evaluara este examen "))
           t += nl2
        total = int (0) 
        for i in range(0,nl):
            nt= int(input("ingrese nota obtenida por el estudiante  :  "))
            total = total + nt
        print("nota final")
        print(total)
        if total > t/2:
           return "aprobado"
        else:
           return "reprobado"


def client_code(facade: Facade) -> None:
   

    print(facade.operation(), end="")


if __name__ == "__main__":

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
