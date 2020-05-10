import sun.security.krb5.internal.LastReqEntry;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.function.IntConsumer;

class FizzBuzz {
    private int n;
    private volatile int i = 1;

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (i <= n) {
            synchronized (this) {
                if (i % 3 != 0 || i % 15 == 0) {
                    wait();
                } else {
                    printFizz.run();
                    i += 1;
                    notifyAll();
                }
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (i <= n) {
            synchronized (this) {
                if (i % 5 != 0 || i % 15 == 0) {
                    wait();
                } else {
                    printBuzz.run();
                    i += 1;
                    notifyAll();
                }
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (i <= n) {
            synchronized (this) {
                if (i % 15 != 0) {
                    wait();
                } else {
                    printFizzBuzz.run();
                    i += 1;
                    notifyAll();
                }
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while (i <= n) {
            synchronized (this) {
                if (i % 3 == 0 || i % 5 == 0) {
                    wait();
                } else {
                    printNumber.accept(i);
                    i += 1;
                    notifyAll();
                }
            }
        }
    }

    public static void submit(FizzBuzz fizzBuzz, ExecutorService executorService, Printer printer) {
        List<Future<?>> futures = new ArrayList<>();
        futures.add(executorService.submit(() -> {
            try {
                fizzBuzz.fizz(() -> printer.print("fizz"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
        futures.add(executorService.submit(() -> {
            try {
                fizzBuzz.buzz(() -> printer.print("buzz"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
        futures.add(executorService.submit(() -> {
            try {
                fizzBuzz.fizzbuzz(() -> printer.print("fizzbuzz"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));
        futures.add(executorService.submit(() -> {
            try {
                fizzBuzz.number((i) -> printer.print(String.valueOf(i)));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }));

        for (Future<?> future : futures) {
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
        FizzBuzz fizzBuzz = new FizzBuzz(10);
        ExecutorService executorService = Executors.newFixedThreadPool(4);
        submit(fizzBuzz, executorService, new Printer());
        executorService.shutdown();
    }
}