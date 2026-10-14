class Sensor {
    public static String tipo = "Genérico";
    public String id;
    public boolean encendido;
    public Sensor(String id) {
        this.id = id;
        this.encendido = false;
    }
    public void activar() {
        encendido = true;
        System.out.println("Sensor activado");
    }
    public void desactivar() {
        encendido = false;
        System.out.println("Sensor desactivado");
    }
}
class Camara extends Sensor {
    public static String tipo = "Cámara";
    public String resolucion;
    public Camara(String id, String resolucion) {
        super(id);
        this.resolucion = resolucion;
    }
    public void mostrarCamara() {
        System.out.println("Tipo: " + tipo);
        System.out.println("ID: " + id);
        System.out.println("Resolución: " + resolucion);
        System.out.println("Encendido: " + encendido);
    }
}
class SensorLuzLaser extends Sensor {
    public static String tipo = "Luz Laser";
    public int alcance;
    public SensorLuzLaser(String id, int alcance) {
        super(id);
        this.alcance = alcance;
    }
    public void mostrarLaser() {
        System.out.println("Tipo: " + tipo);
        System.out.println("ID: " + id);
        System.out.println("Alcance: " + alcance);
        System.out.println("Encendido: " + encendido);
    }
}
class VehiculoAutonomo extends Camara {
    public static String tipo = "Vehículo Autónomo";
    public SensorLuzLaser laser;
    public VehiculoAutonomo(
            String id, String resolucion, int alcance) {
        super(id, resolucion);
        laser = new SensorLuzLaser(id, alcance);
    }
    public void mostrarVehiculo() {
        System.out.println("Tipo: " + tipo);
        System.out.println("ID: " + id);
        System.out.println("Resolución: " + resolucion);
        System.out.println("Alcance del láser: " + laser.alcance);
    }
}
public class Main {
    public static void main(String[] args) {
        VehiculoAutonomo v =
                new VehiculoAutonomo("S001", "4K", 100);
        System.out.println("Tipo: " + VehiculoAutonomo.tipo);
        System.out.println("ID: " + v.id);
        System.out.println("Resolución: " + v.resolucion);
        System.out.println("Alcance: " + v.laser.alcance);
        v.activar();
        v.mostrarVehiculo();
        v.laser.activar();
        v.laser.desactivar();
        v.desactivar();
    }
}
