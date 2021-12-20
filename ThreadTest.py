import time
import threading

def do_something():
    print('sleeping 1 seconds')
    time.sleep(1)
    print('Done Sleeping...')

def do_waiting():
    print('wait 1 seconds')
    time.sleep(1)
    print('Done waiting...')

def do_something_two_seconds():
    for i in range(10):
        print('sleeping 2 seconds')
        time.sleep(2)
    print('Done Sleeping...!')

def do_something_one_seconds():
    for i in range(10):
        print('sleeping 1 seconds')
        time.sleep(1)
    print('Done Sleeping...')

start = time.perf_counter()
# 기본
# for i in range(10):
#     if (i % 2) == 0:
#         do_something()
#     else:
#         do_waiting()

# 멀티 쓰레드
# threads = []
# for i in range(10):
#     if (i % 2) == 0:
#         t = threading.Thread(target=do_something)
#     else:
#         t = threading.Thread(target=do_waiting)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# 실험
# threads = []
# t = threading.Thread(target=do_something_one_seconds)
# t.start()
# threads.append(t)
# t = threading.Thread(target=do_something_two_seconds)
# t.start()
# threads.append(t)
# 
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')