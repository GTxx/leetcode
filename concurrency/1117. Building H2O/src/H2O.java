import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

class H2O {
    private Semaphore canReleaseOxygen = new Semaphore(1);
    private Semaphore canReleaseHydrogen = new Semaphore(2);
    public H2O() {
        
    }

    public synchronized void releaseNew() {
        if (canReleaseOxygen.availablePermits() == 0 && canReleaseHydrogen.availablePermits() == 0) {
            canReleaseOxygen.release(1);
            canReleaseHydrogen.release(2);
        }
    }
    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        canReleaseHydrogen.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        releaseNew();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        canReleaseOxygen.acquire();
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
		releaseNew();
    }

    public static void submit(String orders, H2O h2o, ExecutorService executorService, Printer printer) {
        List<Future<?>> futures = new ArrayList<>();
        for (Character order : orders.toCharArray()) {
            if (order.equals('H')) {
                futures.add(executorService.submit(() -> {
                    try {
                        h2o.hydrogen(() -> printer.print("H"));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }));
            } else if (order.equals('O')) {
                futures.add(executorService.submit(() -> {
                    try {
                        h2o.oxygen(() -> printer.print("O"));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }));
            } else {
                throw new RuntimeException("not support character: " + order);
            }
        }

        for (Future<?> future: futures) {
            try {
                future.get();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            }
        }
        System.out.println(printer.getOutput());
    }

    public static void main(String[] args) {
        H2O h2O = new H2O();
        ExecutorService executorService = Executors.newFixedThreadPool(10);
        submit("HOH", new H2O(), executorService, new Printer());
        submit("OOHHHH", new H2O(), executorService, new Printer());
        submit("OOHHOHHHH", new H2O(), executorService, new Printer());
        executorService.shutdown();
    }


}