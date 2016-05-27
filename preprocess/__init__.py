#encoding=utf8
__author__ = 'jdwang'
__date__ = 'create date: 2016-05-24'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

logging.basicConfig(filename='20160524.log', filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)

print 'start running!'
start_time = timeit.default_timer()

end_time = timeit.default_timer()
print 'end! Running time:%ds!' % (end_time - start_time)
