#encoding=utf8

from gensim.models import Word2Vec
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

config = yaml.load(file('../config.yaml'))
config = config['train_word2vec']
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
output_file_path = config['output_file_path']

class MySentences(object):
    def __init__(self, fname):
        self.fname = unicode(fname)

    def __iter__(self):
        count = 0
        maxcount = 1e10
        for line in io.open(self.fname, mode='r',encoding='utf8'):
            count+=1
            if count <maxcount:
                if (count+1) % 1e6 == 0:
                    print (count+1),line
                    logging.debug((count+1))
                yield line.split(' ')
            else:
                break




# train
size = 50
sentences = MySentences(input_file_path)
# print sentences.__iter__().next()
# quit()
model = Word2Vec(sentences=sentences,
                 size = size,
                 min_count = 5,
                 workers = 100
                 )

# quit()
# save
# vector_file_path = './weibo_%dsize.bin'%(size)
model.save(output_file_path)
# model.save_word2vec_format(vector_file_path,binary=True)
logging.info('save the word2vec model')

word = u'你'
result = model.most_similar(positive=[word])
print ','.join([i for i,j in result])


end_time = timeit.default_timer()
print 'end! Running time:%ds!' % (end_time - start_time)
logging.debug('=' * 20)
logging.debug('end! Running time:%ds!' % (end_time - start_time))
