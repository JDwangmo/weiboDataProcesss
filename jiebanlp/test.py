# encoding=utf-8
import jieba
import jieba.posseg as pseg
p = u'我不同意你的看法'

jieba.load_userdict('userdict.txt')


# jieba.add_word('石墨烯')
# jieba.add_word('凱特琳')
# jieba.del_word('自定义词')

test_sent = (
"2b\n"
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.cut(test_sent)
print words

print('/'.join(words))

print("="*40)
result = pseg.cut(test_sent)
# quit()

for w in result:
    print w.word, "/", w.flag, ", "

print("\n" + "="*40)

terms = jieba.cut('easy_install is great')
print('/'.join(terms))
terms = jieba.cut('python 的正则表达式是好用的')
print('/'.join(terms))

print("="*40)
# test frequency tune
testlist = [
('今天天气不错', ('今天', '天气')),
('如果放到post中将出错。', ('中', '将')),
('我们中出了一个叛徒', ('中', '出')),
]

for sent, seg in testlist:
    print('/'.join(jieba.cut(sent, HMM=False)))
    word = ''.join(seg)
    print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
    print('/'.join(jieba.cut(sent, HMM=False)))
    print("-"*40)

# quit()
jieba.add_word('石墨烯')
seg_list = jieba.cut(p, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(p, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut(p)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(p)  # 搜索引擎模式
print(", ".join(seg_list))
print jieba.suggest_freq(('好','我'))
print jieba.suggest_freq(('走','了'))


print ','.join(jieba.lcut(p))
print ','.join(jieba.lcut_for_search(p))

print ','.join(['%s/%s'%(i,j) for i,j in pseg.lcut(p)])