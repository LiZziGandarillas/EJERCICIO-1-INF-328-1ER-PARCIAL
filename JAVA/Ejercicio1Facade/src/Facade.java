public class Facade
{
    protected Subsystem1 _subsystem1;

    protected Subsystem2 _subsystem2;

    public Facade(Subsystem1 subsystem1, Subsystem2 subsystem2)
    {
        this._subsystem1 = subsystem1;
        this._subsystem2 = subsystem2;
    }

    // Metodos Facade
    public String OperacionFacade()
    {
        String result = "\nFIN FACHADA \n----------- \n";
        System.out.println("INICIO FACHADA\n-------------- \n");
        result += this._subsystem1.operacionEst();
        if (this._subsystem1.operacionMateria() == "l")
            result += this._subsystem2.operacionLab();
        else
            result += this._subsystem2.operacionTeo();
        return result;
    }
}