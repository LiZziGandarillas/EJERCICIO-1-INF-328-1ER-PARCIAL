import java.util.Scanner;

public class Main {

	public static void main(String[] args) {		
		Scanner leer = new Scanner(System.in);
		System.out.print("Ingrese el nombre del estudiante: ");
		String nombre = leer.nextLine();        
		System.out.print("Ingrese el tipo de materia teorica o laboratorio(l/t): ");
		String tipo = leer.nextLine();
		if (tipo.equalsIgnoreCase("l"))
		{
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
				System.out.println("El estudiante " + nombre + " APROBO");
			else
				System.out.println("El estudiante " + nombre + " REPROBO");
		}
		else
		{
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
			Vector2 notaTeo = new Vector2(numTot);
			//Llenado del vector de notas notaTeo
			for (int j = 1; j <= numTot; j++)
			{
				System.out.print("Ingrese por cuanta nota evaluara el "+ j +"º parcial: ");
				notaTeo.setValor(j - 1,leer.nextInt());
				nota += notaTeo.getValor(j - 1);
			}
			System.out.println();
			//Recorrido del vector de notas notaTeo con IteratorVector
			IteradorVector iterador = notaTeo.iterador();
            int i = 1;
            while (iterador.hasNext())
			{
            	int notaParcial = (int)(iterador.next());
				do
				{
					System.out.print("Ingrese nota obtenida en el " + i + "º parcial: ");
					notaEst = leer.nextInt();
					if (notaEst > notaParcial)
					{
						System.out.println("¡Nota no valida!");
					}
				} while (notaEst > notaParcial);
				notaFinal = notaFinal + notaEst;
				i++;
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
				System.out.println("El estudiante " + nombre + " APROBO");
			else
				System.out.println("El estudiante " + nombre + " REPROBO");
		}

	}
}
class Vector2 {
	public int[] _datos;

	public Vector2(int valores){ 
		_datos = new int[valores];
		for (int i = 0; i < _datos.length; i++){
			_datos[i] = 0; 
		}
	}    

	public int getValor(int pos){ 
		return _datos[pos]; 
	}

	public void setValor(int pos, int valor){ 
		_datos[pos] = valor; 
	}

	public int dimension(){ 
		return _datos.length; 
	}

	public IteradorVector iterador(){
		return new IteradorVector(this); 
	}
}
class IteradorVector{
	private int[] _vector;
	private int _posicion;

	public IteradorVector(Vector2 vector) {
		_vector = vector._datos;
		_posicion = 0;
	}

	public boolean hasNext(){
		if (_posicion < _vector.length) 
			return true;
		else
			return false;
	}

	public Object next(){
		int valor = _vector[_posicion];
		_posicion++;
		return valor;
	}
}
