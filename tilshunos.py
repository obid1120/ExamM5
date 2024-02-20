import threading
import pdfkit
from time import perf_counter
#
base_url = 'https://tilshunos.com/omonims/'
#
#
# def tilshunos(arg):
#     pdfkit.from_url(f"{base_url}{arg}/", f"omonimlar/{arg}.pdf")
#     print(f"{arg}-finished")
#
#
# start = perf_counter()
# threads = []
#
# for i in range(1, 3):
#     print("start")
#     t = threading.Thread(target=tilshunos, args=(i,))
#     threads.append(t)
#     t.start()
#     print("end")
#
# for thread in threads:
#     thread.join()
# end = perf_counter()
#
# print(f"Runtime: {end - start: .3f}")

from time import perf_counter
from multiprocessing import Process


def tilshunos(arg):
    pdfkit.from_url(f"{base_url}{arg}/", f"omonimlar/{arg}.pdf")
    print(f"{arg}-finished")


if __name__ == '__main__':
    processes = []

    start = perf_counter()

    for i in range(1, 11, 5):
        p = Process(target=tilshunos, args=[i])
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    finish = perf_counter()
    print(f"Time: {finish - start: .3f} second(s)")

# dastur Linuxda qilingan


