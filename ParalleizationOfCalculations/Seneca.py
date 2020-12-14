import random
import time
import threading


class Seneca(threading.Thread):
    wants_to_eat = True

    def __init__(self, nickname, l_chopstick, r_chopstick):
        threading.Thread.__init__(self)
        self.name = nickname
        self.l_chopstick = l_chopstick
        self.r_chopstick = r_chopstick

    def run(self):
        while self.wants_to_eat:
            time.sleep(random.randint(0, 3))
            print("{} would like to eat noodels.".format(self.name))
            self.start_eating()

    def start_eating(self):
        l_chop = self.l_chopstick
        r_chop = self.r_chopstick

        while self.wants_to_eat:
            l_chop.acquire(True)
            locked = r_chop.acquire(False)
            if locked:
                break
            l_chop.release()
            print("{} swaps chopsticks.".format(self.name))
            l_chop, r_chop = r_chop, l_chop
        else:
            return

        self.eat()
        l_chop.release()
        r_chop.release()

    def eat(self):
        print("{} starts eating delicious noodles.".format(self.name))
        time.sleep(random.randint(1, 6))
        print("{} finished eating noodles and now has WeltSchmerz.".format(self.name))
