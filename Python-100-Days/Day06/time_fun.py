import time
import shutil
import os

seconds = time.time()
print(type(seconds))

localtime = time.localtime(seconds)
print(type(localtime))
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)

asctime = time.asctime(localtime)
print(asctime)

strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)

mydate = time.strptime('2019-05-21', '%Y-%m-%d')
print(mydate)

shutil.copy('/Users/yuanfanggui/Dropbox/interview/knowledge/development_learning/Python-100-Days/foo2.py', '/Users/yuanfanggui/Dropbox/interview/knowledge/development_learning/Python-100-Days/Day06/foo2.py')
os.system('ls -l')
os.chdir('/Users/yuanfanggui/Dropbox/interview/knowledge/development_learning/Python-100-Days')
os.system('ls -l')
os.chdir('/Users/yuanfanggui/Dropbox/interview/knowledge/development_learning/Python-100-Days/Day06')
os.mkdir('text')
os.system('ls -l')
