import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		print "Pokrecem nit "+ self.name
		process_data(self.name, self.q)
		print "Izlazim iz niti " + self.name
		
	def process_data(threadName, q):
		while not exitFlag:
			queueLock.acquire()
			if not workQueue.empty():
				data = q.get()
				queueLock.release()
				print "%s procesuira %s" %(threadName, data)
			else: 
				queueLock.release()
				time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["Jedan", "Dva", "Tri", "Cetiri", "Pet"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadsID = 1

#Kreiraj nove niti

for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1

#Napuni red cekanjua
queueLock.acquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

#Cekaj da se red cekanja isprazni
while not workQueue.empty():
	pass
#Obavijesti niti da je vrijemen za izlazak
exitFlag = 1

#Cekaj dok se sve niti ne izvrse
for t in threads:
	t.join()
print "\nIzlazim iz glavne niti \n"