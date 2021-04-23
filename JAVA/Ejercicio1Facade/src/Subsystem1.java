import java.util.Scanner;

public class Subsystem1
{
	Scanner leer = new Scanner(System.in);
    public String operacionMateria()
    {
    	
        System.out.print("\nIngrese el tipo de materia laboratorio o teorica (l/t): ");
        String tipo = leer.nextLine();
        if (tipo.equalsIgnoreCase("l"))
            return "l";
        else
            return "t";
    }
    public String operacionEst()
    {
    	System.out.print("Ingrese el nombre del estudiante: ");
        String nombre = leer.nextLine();
        return "El estudiante " + nombre;
    }
}