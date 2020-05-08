import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

public class FooBar {
    private int n;
    private Semaphore foo;
    private Semaphore bar;
    public FooBar(int n) {
        this.n = n;
        foo = new Semaphore(1);
        bar = new Semaphore(0);

    }

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            foo.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            bar.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {

            // printBar.run() outputs "bar". Do not change or remove this line.
            bar.acquire();
            printBar.run();
            foo.release();
        }
    }

    public static void main(String[] args) {
        FooBar fooBar = new FooBar(5);
        ExecutorService executorService = Executors.newFixedThreadPool(2);
        executorService.submit(() -> {
            try {
                fooBar.foo(() -> System.out.println("foo"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        executorService.submit(() -> {
            try {
                fooBar.bar(() -> System.out.println("bar"));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        executorService.shutdown();
    }
}
