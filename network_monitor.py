import sys
import os 
import time


http_con = os.popen('netstat -b | find "http"').read()
print "\n http connections",http_con
input('Press Enter to exit')
