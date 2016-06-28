#encoding=utf8

from gensim.models import Word2Vec
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

config = yaml.load(file('../config.yaml'))
config = config['load_word2vec']
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

import io
input_file_path = config['input_file_path']
print input_file_path
model = Word2Vec.load(input_file_path)

# model = Word2Vec.load_word2vec_format(r'D:\ZixuanKe\project\Python\NumberRecognition\weibo_50size.bin',binary=True)
word = u'额'
result = model.most_similar(positive=[word])
print result
print ','.join([i for i,j in result])
