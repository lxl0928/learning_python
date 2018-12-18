#! /usr/bin/env python3 
# coding: utf-8 

import time 

def fibs(num):
    result = [0, 1]
    for i in range(num):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fibs(13)
    with open("./01fibs.txt", 'w+') as fobj:
        for i, num in enumerate(result):
            print("第{0}个数是{1}".format(i, num))
            fobj.write("{0}     {1}\n".format(i, num))
            time.sleep(1)
        fobj.close()

if __name__ == "__main__":
    main()
