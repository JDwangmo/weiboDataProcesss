#encoding=utf8
__author__ = 'jdwang'
__date__ = 'create date: 2016-05-24'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

config = yaml.load(file('../config.yaml'))
config = config['main']
logging.basicConfig(filename=config['log_file_path'], filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)
start_time = timeit.default_timer()
print('=' * 30)
print config['describe']
print('=' * 30)
print 'start running!'
logging.debug('=' * 30)
logging.debug(config['describe'])
logging.debug('=' * 30)
logging.debug('start running!')
logging.debug('=' * 20)

from preprocess import data_filter,data_segment


end_time = timeit.default_timer()
print 'end! Running time:%ds!' % (end_time - start_time)
logging.debug('=' * 20)
logging.debug('end! Running time:%ds!' % (end_time - start_time))
