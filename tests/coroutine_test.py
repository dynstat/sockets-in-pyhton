from time import sleep


def cr():
    print("coroutine starts")
    sleep(5)
    yield 5
    print("coroutine continues..")
    sleep(5)
    yield 6
    print("coroutine continues again..")
    sleep(5)
    yield 7
    print("couroutine ends !!!")


if __name__ == "__main__":
    print("main starts...!!")
    gen_cr = cr()
    sleep(1)
    print("main continue...!!")
    print("main continue...!!")
    print("main continue...!!")
    print("main continue...!!")
    value1 = next(gen_cr)
    print("main continue...!!")
    print("main continue...!!")
    print("main continue...!!")
    print("main continue...!!")
    print(value1)
    sleep(1)
    value2 = next(gen_cr)
    print(value2)
    sleep(1)
    value3 = next(gen_cr)
    print(value3)
