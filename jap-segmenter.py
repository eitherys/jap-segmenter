# Nabeel Ansari

import os
import codecs
import tinysegmenter

textfile = raw_input('name of file: ')
f = codecs.open(textfile, 'r', 'utf-8')
text_dump = u''.join([l.rstrip() for l in f.readlines()])
f.close()

toker = tinysegmenter.TinySegmenter()
tokens = toker.tokenize(text_dump)
freq_dic = {t:text_dump.count(t) for t in tokens}

sorted_list = sorted(freq_dic.items(), key=lambda word:word[1], reverse=True)


f = codecs.open(textfile + '-token-frequency.csv', 'w', 'utf-16')
for tup in sorted_list:
	f.write(u'{},{}\n'.format(tup[0],str(tup[1])))
f.close()