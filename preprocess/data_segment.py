#encoding=utf8
__author__ = 'jdwang'
__date__ = 'create date: 2016-05-24'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

config = yaml.load(file('../config.yaml'))
config = config['data_segment']
logging.basicConfig(filename=config['log_file_path'], filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)
start_time = timeit.default_timer()
print config['describe']
print 'start running!'
logging.debug('='*30)
logging.debug(config['describe'])
logging.debug('='*30)
logging.debug('start running!')
logging.debug('='*20)

input_file_path = config['input_file_path']
output_file_path = config['output_file_path']

from jiebanlp.toolSet import seg
import io
out = io.open(output_file_path,'w',encoding='utf8')
counter = 0
error_line_counter = 0
for line in io.open(input_file_path,'r',encoding='utf8'):
    if (counter + 1) % 1e5 == 0:
        logging.debug('第%d条记录' % (counter + 1))
    if (counter + 1) % 1e6 == 0:
        print('第%d条记录' % (counter + 1))
    try:
        # backup = line
        line = line.strip()
        if len(line) == 0:
            continue
        seg_str = seg(line,sep=' ',full_mode=False)
        out.write(seg_str+'\n')
        # print seg_str
        # break
    except:
        logging.debug(u'exception！In line %d:%s'%(counter,line))
        error_line_counter+=1
    counter += 1
logging.debug('总共%d句'%(counter))
logging.debug('错误转换行的个数：%d'%(error_line_counter))
end_time = timeit.default_timer()
print 'end! Running time:%ds!' % (end_time - start_time)
logging.debug('='*20)
logging.debug('end! Running time:%ds!' % (end_time - start_time))
