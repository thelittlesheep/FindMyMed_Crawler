from concurrent.futures import ThreadPoolExecutor

class TestClass():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def customPrint(self):
        for i in range(self.start,self.end):
            print(str(i))

def worker1():
    test1 = TestClass(1,100000)
    test1.customPrint()

def worker2():
    test2 = TestClass(100001,200000)
    test2.customPrint()

def worker3():
    test3 = TestClass(100001,300000)
    test3.customPrint()

def worker4():
    test4 = TestClass(300001,400000)
    test4.customPrint()

with ThreadPoolExecutor() as executor:
    executor.submit(worker1)
    executor.submit(worker2)
    executor.submit(worker3)
    executor.submit(worker3)

if __name__ == '__main__':
        executor