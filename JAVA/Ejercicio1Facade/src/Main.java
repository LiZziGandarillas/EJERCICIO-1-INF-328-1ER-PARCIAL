
public class Main {

	public static void main(String[] args) {
		Subsystem1 subsystem1 = new Subsystem1();
        Subsystem2 subsystem2 = new Subsystem2();
        Facade facade = new Facade(subsystem1, subsystem2);
        Client.ClientCode(facade);
	}

}





class Client
{
    public static void ClientCode(Facade facade)
    {
    	System.out.println(facade.OperacionFacade());
    }
}