from multiprocessing import Lock, Manager
import time
import random

def delay():
    time.sleep(random.random()/6)

nombres = ['Platon', 'Descartes', 'Kant', 'Nietzsche', 'Socrates']

class Table:
    def __init__(self,N,K, manager):
        self.comidas = [K for _ in range(N)]
        self.tenedores = [Lock() for _ in range(N)]
        self.semaforos = [True for _ in range(N)]
        
    def wants_eat(self, i):
        if i%2 == 0:
            j = (i+1) % 5
        else:
            j = i
            i +=1
        if self.semaforos[i]:
            self.tenedores[i].acquire()
            self.semaforos[i] = False
            
            print(nombres[i % 5], ' ha cogido un tenedor',self.semaforos[i])
            delay()
            if self.semaforos[j]:
                self.semaforos[j] = False
                self.tenedores[j].acquire()
                
                print(nombres[i % 5],' esta comiendo')
                delay()
                self.comidas[i] -= 1
            else:
                print(nombres[i % 5], ' esta llorando porque le falta un tenedor')
                
                self.tenedores[i].release()
                self.semaforos[i] = True
                
                    
    def wants_think(self, i):
        j = (i+1) % 5

        self.tenedores[j].release()
        self.tenedores[i].release() 
        self.semaforos[i] = True
        self.semaforos[j] = True
        print(nombres[i % 5],' esta pensando')
        print(nombres[i % 5],' esta pensando')