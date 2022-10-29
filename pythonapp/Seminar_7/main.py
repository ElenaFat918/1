from fileinput import filename
from stat import filemode
import controller as c
import logging as log

# если хотим, чтобы логи вывлдились в консоль
# log.basicConfig(level=log.INFO)

# если хотим, чтобы логи вывлдились в файл
log.basicConfig(filename = 'log.txt',
                    filemode = 'a',
                    format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=log.INFO)


c.run(log)