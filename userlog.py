import os
import sys
import time


def userlog(name) :
    log = open('userlog.txt', 'a')
    timeis = time.ctime()
    log.write('\n')
    log.write(timeis)
    log.write('   :   ')
    log.write(name)
    
    

a = 'nut'
userlog(a)