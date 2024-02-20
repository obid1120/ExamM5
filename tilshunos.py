# dastur Linuxda qilingan

import threading
import pdfkit
from time import perf_counter

base_url = 'https://tilshunos.com/omonims/'


def tilshunos(arg):
    pdfkit.from_url(f"{base_url}{arg}/", f"omonimlar/{arg}.pdf")
    print(f"{arg}-finished")


start = perf_counter()
threads = []

for i in range(1, 11):
    t = threading.Thread(target=tilshunos, args=(i,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
end = perf_counter()

print(f"Runtime: {end - start: .3f}")
