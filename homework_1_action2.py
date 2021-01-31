# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:43:18 2021

@author: albert
"""

import numpy as np
studenttype=np.dtype({
    'names':['name','chinese','math','english'],
    'formats':['S32','f','f','f']})
students_score=np.array([
    ("Zhangfei",68,65,30),
    ('Guanyu',95,76,98),
    ('Liubei',98,86,88),
    ('Dianwei',90,88,77),
    ('Xuchu',80,90,90)],dtype=studenttype)
chinese_score=students_score['chinese']
math_score=students_score['math']
english_score=students_score['english']
print('这几个人的语文平均分是：'+str(np.mean(chinese_score)))
print('语文最低分是: '+str(np.min(chinese_score)))
print('语文最高分是: '+str(np.max(chinese_score)))
print('语文的方差是: '+str(np.var(chinese_score)))
print('语文的标准差是: '+str(np.std(chinese_score)))
print('\n')
print('这几个人的数学平均分是: '+str(np.mean(math_score)))
print('数学最低分是: '+str(np.min(math_score)))
print('数学最高分是: '+str(np.max(math_score)))
print('数学的方差是: '+str(np.var(math_score)))
print('数学的标准差是: '+str(np.std(math_score)))
print('\n')
print('这几个人的英语平均分是: '+str(np.mean(english_score)))
print('英语最低分是: '+str(np.min(english_score)))
print('英语最高分是: '+str(np.max(english_score)))
print('英语的方差是: '+str(np.var(english_score)))
print('英语的标准差是: '+str(np.std(english_score)))
print('\n')
print('总成绩排名依次是：')
print(np.sort(chinese_score+math_score+english_score))
#s=np.array(np.sort(chinese_score+math_score+english_score))
#print(s[0])
