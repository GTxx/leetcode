public class Printer {

    private volatile String output = "";

    public String getOutput() {
        return output;
    }

    public void print(String s) {
        synchronized (this) {
            output = output + s;
        }
    }
}
