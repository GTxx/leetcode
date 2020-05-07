import java.util.concurrent.*;

class PrintOrder {

    private Semaphore run2;
    private Semaphore run3;

    public PrintOrder() {
        run2 = new Semaphore(0);
        run3 = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        run2.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        run2.acquire();
        printSecond.run();
        run3.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        run3.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }

    public static void submit(int[] orders, PrintOrder printOrder, ExecutorService executorService) {
        for (int order : orders) {
            if (order == 1) {
                executorService.submit(() -> {
                    try {
                        printOrder.first(() -> System.out.println("first"));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                });
            } else if (order == 2) {
                executorService.submit(() -> {
                    try {
                        printOrder.second(() -> System.out.println("second"));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                });
            } else if (order == 3) {
                executorService.submit(() -> {
                    try {
                        printOrder.third(() -> System.out.println("third"));
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                });
            } else {
                throw new RuntimeException("not support number: " + order);
            }
        }
    }

    public static void main(String[] args) {
        ExecutorService executorService = Executors.newFixedThreadPool(3);

        submit(new int[]{1, 2, 3}, new PrintOrder(), executorService);
        submit(new int[]{1, 3, 2}, new PrintOrder(), executorService);
        submit(new int[]{2, 3, 1}, new PrintOrder(), executorService);
        submit(new int[]{2, 1, 3}, new PrintOrder(), executorService);
        submit(new int[]{3, 1, 2}, new PrintOrder(), executorService);
        submit(new int[]{3, 2, 1}, new PrintOrder(), executorService);

        executorService.shutdown();

    }
}
