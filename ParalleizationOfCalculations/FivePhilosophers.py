import random
import time
import threading
from ParalleizationOfCalculations.Seneca import Seneca

if __name__ == '__main__':
    print("Party time!")
    chopsticks = [threading.Lock() for n in range(4)]
    random_people = ["Mathew", "Shaq", "Snoop", "Will"]
    cool_dudes = [Seneca(random_people[n], chopsticks[n % 4], chopsticks[(n + 1) % 4]) for n in range(4)]

    Seneca.wants_to_eat = True

    for dude in cool_dudes:
        dude.start()
    time.sleep(10)
    Seneca.wants_to_eat = False
    print("Time to sleep!")




