from threading import Thread
from writer import parse_and_write
from proxies import proxyDict_1
from proxies import proxyDict_2
from proxies import proxyDict_3
from proxies import proxyDict_4
from proxies import proxyDict_5
from proxies import proxyDict_6
from proxies import proxyDict_7
from proxies import proxyDict_8
from proxies import proxyDict_9
from proxies import proxyDict_10

#33999999 - количество книг

t1 = Thread(target=parse_and_write, args=(1, 10000, proxyDict_1))
t2 = Thread(target=parse_and_write, args=(10001, 17002, proxyDict_2))
t3 = Thread(target=parse_and_write, args=(17003, 24004, proxyDict_3))
t4 = Thread(target=parse_and_write, args=(24005, 31006, proxyDict_4))
t5 = Thread(target=parse_and_write, args=(31007, 38008, proxyDict_5))
t6 = Thread(target=parse_and_write, args=(38009, 45010, proxyDict_6))
t7 = Thread(target=parse_and_write, args=(45011, 52012, proxyDict_7))
t8 = Thread(target=parse_and_write, args=(52013, 59014, proxyDict_8))
t9 = Thread(target=parse_and_write, args=(59015, 66016, proxyDict_9))
t10 = Thread(target=parse_and_write, args=(66017, 73018, proxyDict_10))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
