# coding=gbk
# ��ʾ����Ľ�����
import sys

class Book:
    # �����Ϣ
    def __init__(self,name='',pagesum=0,curpage=0):
        # ���캯��
        self.name = name          # ����
        self.pagesum = pagesum    # �����ҳ��
        self.curpage = curpage     # ��ǰ��������ҳ

book_list = []      # �������б�
book_sum = 0     # �������
localfile = 'bookstack.dat'      # �����ļ������֣����ڴ洢�����Ϣ

def start():
    # ������ģ��ʱ����
    global book_list,book_sum
    fp = open(localfile,'r')    # ��ֻ��ģʽ���ļ�
    i = 1
    for line in fp:    # ��ÿ��
        line = line.strip()
        line = line.split('|') # ȥ����ĩ��\n
        b = Book()
        b.name,b.pagesum,b.curpage = line[0],int(line[1]),int(line[2])     # �ַ���ת��Ϊ����
        book_list.append(b) # ��������Ϣ�����ڴ�
        book_sum+=1     # ����+1
    fp.close()

def InsertLocal(b):
    # ��ӵ������ļ�
    fp = open(localfile,'a')    # ��׷��ģʽ���ļ�
    fp.writelines('%s|%s|%s\n'%(b.name,b.pagesum,b.curpage))   # �����Ŀ���ļ����
    fp.close()

def addBook(bookname='',pagesum=0,curpage=0):
    # ���һ����
    global book_sum
    if bookname=='':
        print '��Ǹ����û������������'
    elif pagesum==0:
        print '��Ǹ����û�����������ҳ����'
    else:
        b = Book(bookname,pagesum,curpage)
        InsertLocal(b)          # ��¼��ӵ�����
        book_list.append(b)     # ��ӵ��ڴ�
        book_sum += 1
        #print '��ӳɹ�����������Ϊ�����ɣ�'

'''
def showBooks():
    # ��ʾ����ͼ��
    print '����嵥��'
    i = 1
    for book in book_list:
        print '[%d] %s'%(i,book.name)
        i+=1
'''

def showBar(num):
        # ��ʾĳһ����Ľ���
        num-=1
        name = book_list[num].name
        curpage = book_list[num].curpage
        pagesum = book_list[num].pagesum
        b_num = curpage*20/pagesum
        # display bookname
        print '[%d] %s'%(num+1,name)
        # display progress bar of read
        print '[%s%s] [%d/%d | %.1f%%]'%\
              ('��'*b_num,'��'*(20-b_num),curpage,pagesum,float(curpage*100)/pagesum)

def showProgress(num=0):
    # ��ʾĳһ����Ķ������
    if num<0 or num>book_sum:
        print '��Ǹ��û���Ȿ�飡'
        return 
    if num==0:
        # ��ʾ������Ķ������
        print '�ҵ���ܣ�'
        for i in range(1,book_sum+1):
            showBar(i)
    else:
        # ��ʾĳһ����Ľ����� 
        showBar(num)

def update(num,page):
    # ����ĳһ����Ľ���
    num-=1
    book_list[num].curpage = page
    # ���±����ļ�
    fp = open(localfile,'w')
    for l in book_list:
        fp.write('%s|%s|%s\n'%(l.name,l.pagesum,l.curpage))
    fp.close()
    print '���³ɹ���'
    showBar(num+1)

def getCatalog(bookname):
    # �����ϻ�ȡĿ¼���������ʽ
    pass


def help():
    # ����ʹ���ĵ�
    pass

def isDigit(my_str):
    try:
        int(my_str)
    except ValueError:
        return False
    return True

if __name__=='__main__':
    start()
    #addBook('�ҵķܶ�',234,123)
    #addBook('��ʱ��',464,340)
    
    argv = sys.argv
    argc = len(argv)
    if argc==1:     # ��ʾ������Ľ���
        showProgress()
    if argc==2:     # ��ʾĳһ����Ľ���
        showProgress(int(argv[1]))
    if argc==3:     
        if isDigit(argv[1]):    # ����һ����
            update(int(argv[1]),int(argv[2]))
        else:   # ���һ����
            addBook(argv[1],argv[2])
    if argc==4:     # ���һ����
        addBook(argv[1],argv[2],argv[3])
    

