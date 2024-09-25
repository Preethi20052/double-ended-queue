class Queue:
    def __init__ (self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [0] * self.size

    def enqueuefront(self, data):
        if (self.rear + 1) % self.size == self.front:  
            print("Overflow")
        elif self.front == -1:  
            self.front = self.rear = 0
            self.queue[self.front] = data
        elif self.front==0:
            self.front=size-1
            self.queue[self.front]=data
        else:
            self.front-=1
            self.queue[self.front]=data

    def enqueuerear(self, data):
        if (self.rear + 1) % self.size == self.front:  
            print("Overflow")
        elif self.front == -1:  
            self.front = self.rear = 0
            self.queue[self.rear] = data    
        elif self.rear== size-1:
            self.rear=0
            self.queue[self.rear] = data
        else:
           self.rear+=1    
           self.queue[self.rear] = data

    def dequeuefront(self):
        if self.front == -1:  
            print("Underflow")
        elif self.front == self.rear:  
            print(self.queue[self.front])
            self.front = self.rear = -1  
        elif(self.front==size-1):
            self.front=0
        else:
            self.front+=1

    def dequeuerear(self):
        if self.front == -1:  
            print("Underflow")
        elif self.front == self.rear:  
            print(self.queue[self.front])
            self.front = self.rear = -1  
        elif(self.rear==0):
            self.rear=size-1
        else:
            self.rear-=1


    def display(self):
        if self.front == -1:  
            print("Queue is empty")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" -> ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print(None)

size = int(input("Enter the number of elements: "))
Q = Queue(size)
for i in range(size//2):
    data = int(input("Enter the data: "))
    
    Q.enqueuefront(data)
    Q.display()
    Q.enqueuerear(data)
    Q.display()

Q.dequeuefront()
Q.display()
Q.dequeuerear()
Q.display()






        

            

