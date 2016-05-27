#encoding=utf8
__author__ = 'jdwang'
__date__ = 'create date: 2016-05-24'
import numpy as np
import pandas as pd
import logging
import timeit
import yaml

config = yaml.load(file('../config.yaml'))
config = config['data_filter']
logging.basicConfig(filename=config['log_file_path'], filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)

print 'start running!'
start_time = timeit.default_timer()
import re
import io
data_file_path = config['data_file_path']
output_file_path = config['output_file_path']
logging.debug(config['describe'])
out = io.open(output_file_path,'w',encoding='utf8')
# 使用正则过滤掉非中文的字符
pattern = re.compile(u'[^\u4e00-\u9fa5]+')
filter_not_chinese_text = lambda x: pattern.sub(' ', x.decode('utf8'))
counter = 0
error_line_counter = 0
for line in open(data_file_path,'r'):
    if (counter+1)%1e5 == 0:
        logging.debug('第%d条记录'%(counter+1))
    if (counter+1)%1e6 == 0:
        print('第%d条记录'%(counter+1))
    seg = line.strip().split(',')
    line = ''.join(seg[5:])
    # print line
    try:
        line = filter_not_chinese_text(line)

        out.write(line + '\n')
        break
    except:
        logging.debug('exception！In line %d:%s'%(counter,line))
        error_line_counter+=1
        print counter
        print line
    # print type(unicode(line))
    counter+=1
logging.debug('总共%d句'%(counter))
logging.debug('错误转换行的个数：%d'%(error_line_counter))
end_time = timeit.default_timer()
print 'end! Running time:%ds!' % (end_time - start_time)
logging.debug( 'end! Running time:%ds!' % (end_time - start_time))
