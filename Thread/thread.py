import threading

def do_this():
    global lock,x
    while(x<300):
        x+=1
    # lock.acquire()
    # try:
    #     while (x < 300 ):
    #         x+=1
    # finally:
    #     lock.release()
    print('The value of are x -{}'.format(x))

def do_this_after():
    global x,lock
    # while(x<600):
    #     x+=1
    lock.acquire()
    try:
        while(x <600):
            x+=1
    finally:
        lock.release()
    print('The value of x are -{}'.format(x))

def main():
    global lock,x
    lock = threading.RLock()
    x = 0
    our_thread = threading.Thread(name = 'our_thread',target=do_this)
    our_thread.start()
    our_next_thread = threading.Thread(name = 'our_next_thread',target=do_this_after)
    our_next_thread.start()
    
if __name__ == '__main__':
    main()