# coding=gbk
# 显示读书的进度条
import sys

class Book:
    # 书的信息
    def __init__(self,name='',pagesum=0,curpage=0):
        # 构造函数
        self.name = name          # 书名
        self.pagesum = pagesum    # 书的总页数
        self.curpage = curpage     # 当前读到多少页

book_list = []      # 创建书列表
book_sum = 0     # 书的数量
localfile = 'bookstack.dat'      # 本地文件的名字，用于存储书的信息

def start():
    # 启动该模块时加载
    global book_list,book_sum
    fp = open(localfile,'r')    # 已只读模式打开文件
    i = 1
    for line in fp:    # 读每行
        line = line.strip()
        line = line.split('|') # 去除行末的\n
        b = Book()
        b.name,b.pagesum,b.curpage = line[0],int(line[1]),int(line[2])     # 字符串转换为数字
        book_list.append(b) # 将该书信息载入内存
        book_sum+=1     # 计数+1
    fp.close()

def InsertLocal(b):
    # 添加到本地文件
    fp = open(localfile,'a')    # 以追加模式打开文件
    fp.writelines('%s|%s|%s\n'%(b.name,b.pagesum,b.curpage))   # 添加条目到文件最后
    fp.close()

def addBook(bookname='',pagesum=0,curpage=0):
    # 添加一本书
    global book_sum
    if bookname=='':
        print '抱歉，你没有设置书名！'
    elif pagesum==0:
        print '抱歉，你没有设置书的总页数！'
    else:
        b = Book(bookname,pagesum,curpage)
        InsertLocal(b)          # 记录添加到本地
        book_list.append(b)     # 添加到内存
        book_sum += 1
        #print '添加成功！进度条已为您生成！'

'''
def showBooks():
    # 显示所有图书
    print '书的清单：'
    i = 1
    for book in book_list:
        print '[%d] %s'%(i,book.name)
        i+=1
'''

def showBar(num):
        # 显示某一本书的进度
        num-=1
        name = book_list[num].name
        curpage = book_list[num].curpage
        pagesum = book_list[num].pagesum
        b_num = curpage*20/pagesum
        # display bookname
        print '[%d] %s'%(num+1,name)
        # display progress bar of read
        print '[%s%s] [%d/%d | %.1f%%]'%\
              ('■'*b_num,'□'*(20-b_num),curpage,pagesum,float(curpage*100)/pagesum)

def showProgress(num=0):
    # 显示某一本书的读书进度
    if num<0 or num>book_sum:
        print '抱歉，没有这本书！'
        return 
    if num==0:
        # 显示所有书的读书进度
        print '我的书架：'
        for i in range(1,book_sum+1):
            showBar(i)
    else:
        # 显示某一本书的进度条 
        showBar(num)

def update(num,page):
    # 更新某一本书的进度
    num-=1
    book_list[num].curpage = page
    # 更新本地文件
    fp = open(localfile,'w')
    for l in book_list:
        fp.write('%s|%s|%s\n'%(l.name,l.pagesum,l.curpage))
    fp.close()
    print '更新成功！'
    showBar(num+1)

def getCatalog(bookname):
    # 从网上获取目录，并整理格式
    pass


def help():
    # 程序使用文档
    pass

def isDigit(my_str):
    try:
        int(my_str)
    except ValueError:
        return False
    return True

if __name__=='__main__':
    start()
    #addBook('我的奋斗',234,123)
    #addBook('暗时间',464,340)
    
    argv = sys.argv
    argc = len(argv)
    if argc==1:     # 显示所有书的进度
        showProgress()
    if argc==2:     # 显示某一本书的进度
        showProgress(int(argv[1]))
    if argc==3:     
        if isDigit(argv[1]):    # 更新一本书
            update(int(argv[1]),int(argv[2]))
        else:   # 添加一本书
            addBook(argv[1],argv[2])
    if argc==4:     # 添加一本书
        addBook(argv[1],argv[2],argv[3])
    

