from multiprocessing import Process
from multiprocessing import Condition, Lock
from multiprocessing import Array, Manager
import time
import random
from monitor import Table, delay
NPHIL = 5
K = 100
def delay(n):
    time.sleep(random.random()/n)
def philosopher_task(num, table):
 #   table.set_current_phil(num)
    for i in range(K):
      #  print('Philosofer',num, 'thinking')
      #  print('Philosofer', num, 'wants to eat')
        table.wants_eat(num)
        print(i)
      #  print('Philosofer' ,num, 'eating')
        table.wants_think(num)
        print(i)
      #  print('Philosofer' ,num, 'stops eating')
def main():
    manager = Manager()
    table = Table(NPHIL,K, manager)
    philosofers = [Process(target=philosopher_task, args=(i,table)) \
                   for i in range(NPHIL)]
    for i in range(NPHIL):
        philosofers[i].start()
        
    for i in range(NPHIL):
        philosofers[i].join()
if __name__ == '__main__':
    main()
