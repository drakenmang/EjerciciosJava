package SinInterfaz;

import Interfaz.cocheCRUD;
import java.util.List;

public class Main {

    public static void main(String[] args) {
    CocheCRUD coche = (CocheCRUD) new CocheCRUDImpl();
    coche.save();
    coche.findAll();
    coche.delete();
    /*
    cocheCRUD cocheCRUD = new cocheCRUD();


    Coche Ford = new Coche("Focus", 2005, 2500.0, true);
    Coche Mustang = new Coche("GT", 2005, 4500.0, true);
    Coche BMW = new Coche("M3", 2008, 3500.0, true);
    Coche Honda = new Coche("Civic", 1999, 1500.0, false);

         GUARDAR EMPLEADOS
        cocheCRUD.guardar();
        cocheCRUD.guardar(Ford);
        cocheCRUD.guardar(Mustang);
        cocheCRUD.guardar(BMW);
        cocheCRUD.guardar(Honda);


        // CONSULTAR EMPLEADOS
        List<Coche> coches = cocheCRUD.findAll();
        System.out.println(coches);


        //BORRAR EMPLEADOS

        cocheCRUD.delete();

        */


    }
}
