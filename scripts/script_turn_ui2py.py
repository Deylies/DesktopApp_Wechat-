# encoding:utf-8
# __author__:DeyLies,WangYu
import os,sys
ui_file = sys.argv[1]
save_name = sys.argv[2]
os.system("pyuic5 %s>widgets/widget_%s.py"%(ui_file,save_name))
