import os
import sys
import time


def userlog(action) :
    log = open('adminlog.txt', 'a')
    timeis = time.ctime()
    log.write('\n')
    log.write(timeis)
    log.write('   :   ')
    log.write(action)
    log.close
