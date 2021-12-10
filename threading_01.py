import threading 

def first_fun(age):
    while True:
        print("i'm first child",age)
    return

def second_fun(age):
    while True:
        print("i'm second child",age)
    return

if __name__ =='__main__':
    main = threading.Thread(target = first_fun,args=(5,))
    sub = threading.Thread(target = second_fun,args=(3,))
    main.start()
    sub.start()    
    main.join()
    sub.join()

    while True:
        print("i'm parents")
    
    pass