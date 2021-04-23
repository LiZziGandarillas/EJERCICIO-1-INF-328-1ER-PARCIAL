import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner leer = new Scanner(System.in);
		Client client = new Client();
        System.out.print("Ingrese el tipo de materia teorica o laboratorio(l/t): ");
        String tipo = leer.nextLine();
        Abstraction abstraction;
        if (tipo.equalsIgnoreCase("l"))
        {
            abstraction = new Abstraction(new ConcreteImplementationLab());
            client.ClientCode(abstraction);
        }
        else
        {
            abstraction = new ExtendedAbstraction(new ConcreteImplementationTeo());
            client.ClientCode(abstraction);
        }
        System.out.println();
	}
}

class Abstraction
{
    protected IImplementation _implementation;

    public Abstraction(IImplementation implementation)
    {
        this._implementation = implementation;
    }

    public String Operation()
    {
        return "\n" +
            _implementation.OperationImplementation();
    }
}

class ExtendedAbstraction extends Abstraction
{
    public ExtendedAbstraction(IImplementation implementation)
    {
    	super(implementation);
    }

    @Override
    public String Operation()
    {
        return "\n" +
            super._implementation.OperationImplementation();
    }
}

interface IImplementation
{
    String OperationImplementation();
}
class ConcreteImplementationLab implements IImplementation
{
    public String OperationImplementation()
    {
    	Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese el nombre del estudiante: ");
        String nombre = leer.nextLine();
        int notaFinal = 0;
        System.out.print("La materia cuenta con auxiliatura(s/n): ");
        String aux = leer.nextLine();
        int notaAux = 0;
        if (aux.equalsIgnoreCase("s"))
        {
            System.out.print("Ingrese cuanto vale la auxiliatura: ");
            notaAux = leer.nextInt();
        }
        System.out.print("Ingrese el numero de laboratorios: ");
        int numTot = leer.nextInt();
        System.out.print("Ingrese la nota que vale un laboratorio: ");
        int notaLab = leer.nextInt();
        int nota = (notaLab * numTot);
        int notaEst = 0;
        System.out.println();
        for (int i = 1; i <= numTot; i++)
        {
            do
            {
                System.out.print("Ingrese la nota obtenida en el " + i + "º laboratorio: ");
                notaEst = leer.nextInt();
                if (notaEst > notaLab)
                {
                    System.out.println("¡Nota no valida!");
                }
            } while (notaEst > notaLab);
            notaFinal = notaFinal + notaEst;
        }
        int notaAuxEst = 0;
        if (aux.equalsIgnoreCase("s"))
        {
            do
            {
                System.out.print("Ingrese la nota de auxiliatura: ");
                notaAuxEst = leer.nextInt();
                if (notaAuxEst > notaAux)
                {
                    System.out.println("¡Nota no valida!");
                }
            } while (notaAuxEst > notaAux);
            notaFinal = notaFinal + notaAuxEst;
        }
        System.out.println("\nNOTA FINAL DE LABORATORIO: " + notaFinal);
        if (notaFinal > nota / 2)
            return "El estudiante " + nombre + " APROBO";
        else
            return "El estudiante " + nombre + " REPROBO";

    }
}

class ConcreteImplementationTeo implements IImplementation
{
    public String OperationImplementation()
    {
    	Scanner leer = new Scanner(System.in);
        System.out.print("Ingrese el nombre del estudiante: ");
        String nombre = leer.nextLine();
        int notaFinal = 0;
        System.out.print("La materia cuenta con auxiliatura(s/n): ");
        String aux = leer.nextLine().toLowerCase();
        int notaAux = 0;
        if (aux.equalsIgnoreCase("s"))
        {
            System.out.print("Ingrese cuanto vale la auxiliatura: ");
            notaAux = leer.nextInt();
        }
        System.out.print("Ingrese el numero de parciales: ");
        int numTot = leer.nextInt();
        int nota = 0, notaEst = 0;
        int[] notaTeo = new int[numTot];
        for (int i = 1; i <= numTot; i++)
        {
            System.out.print("Ingrese por cuanta nota evaluara el "+ i +"º parcial: ");
            notaTeo[i - 1] = leer.nextInt();
            nota += notaTeo [i-1];
        }
        System.out.println();
        for (int i = 1; i <= numTot; i++)
        {
            do
            {
                System.out.print("Ingrese nota obtenida en el " + i + "º parcial: ");
                notaEst = leer.nextInt();
                if (notaEst > notaTeo[i - 1])
                {
                    System.out.println("¡Nota no valida!");
                }
            } while (notaEst > notaTeo[i - 1]);
            notaFinal = notaFinal + notaEst;
        }
        int notaAuxEst = 0;
        if (aux.equalsIgnoreCase("s"))
        {
            do
            {
                System.out.print("Ingrese la nota de auxiliatura: ");
                notaAuxEst = leer.nextInt();
                if (notaAuxEst > notaAux)
                {
                    System.out.println("¡Nota no valida!");
                }
            } while (notaAuxEst > notaAux);
            notaFinal = notaFinal + notaAuxEst;
        }
        System.out.println("\nNOTA FINAL:" + notaFinal);
        if (notaFinal > nota / 2)
            return "El estudiante "+ nombre + " APROBO";
        else
            return "El estudiante " + nombre + " REPROBO";

    }
}

class Client
{
    public void ClientCode(Abstraction abstraction)
    {
        System.out.print(abstraction.Operation());
    }
}
