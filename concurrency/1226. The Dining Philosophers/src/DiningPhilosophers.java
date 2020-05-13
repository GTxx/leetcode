import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;

class DiningPhilosophers {
  private List<Semaphore> semaphoreList = new ArrayList<>();

  public DiningPhilosophers() {
    for (int i = 0; i < 5; i++) {
      semaphoreList.add(new Semaphore(1));
    }
  }

  // call the run() method of any runnable to execute its code
  public void wantsToEat(int philosopher,
                         Runnable pickLeftFork,
                         Runnable pickRightFork,
                         Runnable eat,
                         Runnable putLeftFork,
                         Runnable putRightFork) throws InterruptedException {

    int leftForkIndex = (philosopher ) %5;
    int rightForkIndex = (philosopher + 1) % 5;
    Semaphore leftForkSemaphore = semaphoreList.get(leftForkIndex);
    Semaphore rightForkSemaphore = semaphoreList.get(rightForkIndex);
    if (philosopher == 0) {
      // pick left fork first
        leftForkSemaphore.acquire();
        pickLeftFork.run();
        rightForkSemaphore.acquire();
        pickRightFork.run();
        eat.run();
        leftForkSemaphore.release();
        putLeftFork.run();
        rightForkSemaphore.release();
        putRightFork.run();
    } else {
      // pick right fork first
      rightForkSemaphore.acquire();
      pickRightFork.run();
      leftForkSemaphore.acquire();
      pickLeftFork.run();
      eat.run();
      leftForkSemaphore.release();
      putLeftFork.run();
      rightForkSemaphore.release();
      putRightFork.run();
//    }
  }

  public static Runnable[] getRunnable(int philosofer) {
    Runnable[] runnables = {
        () -> System.out.println(philosofer + " pick left"),
        () -> System.out.println(philosofer + " pick right"),
        () -> System.out.println(philosofer + " eat"),
        () -> System.out.println(philosofer + " put left"),
        () -> System.out.println(philosofer + " put right"),
    };
    return runnables;
  }
  public static void main(String[] args) {
    DiningPhilosophers diningPhilosophers = new DiningPhilosophers();
    ExecutorService executorService = Executors.newFixedThreadPool(5);
    for (int m = 0; m < 2; m ++) {
      for (int i = 0; i < 5; i++) {
        Runnable[] runnables = getRunnable(i);
        final int k = i;
        executorService.submit(() -> {
          try {
            diningPhilosophers.wantsToEat(k, runnables[0], runnables[1], runnables[2], runnables[3], runnables[4]);
          } catch (InterruptedException e) {
            e.printStackTrace();
          }
        });
      }
    }
    executorService.shutdown();
  }
}


