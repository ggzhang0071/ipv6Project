#
import csv
import argparse 
from googletrans import Translator



def txTrancsv(txtf,csvf):
    firo = open(txtf,'r')
    fiwo = open(csvf,'w')
    translator = Translator()
    contents = firo.read()
    dst = ''
    src = 'auto'
    # 当输入内容超过限制的时候的解决 分段处理
    if len(contents) > 4891:    
        print("翻译的长度超过限制！！！") 
    transcontent = translator.translate(contents,dest=dst,src=src)
    fiwo.write(transcontent)
    firo.close()  
    fiwo.close()




def main(): 
    # 输入为文件txt,输出为文件csv   
    parser = argparse.ArgumentParser('usage%prog -h <help>-i <input filename> -o <output filename>')
    #parser.add_option('-h',dest='helpu',type='string')
    parser.add_argument('-i',dest='txtf',type=str,help='specify input file')
    parser.add_argument('-o',dest='csvf',type=str,help='specify output filename')
    args = parser.parse_args()
    '''
    if options.txtf == None && options.csvf == None:
        pass
    else:
    
    if helpu == None:
        pass
    '''
    print(args.txtf) 

if __name__ == '__main__':
    main()

        
        



#peepdf:Python 编写的PDF文件分析工具，可以帮助检测恶意的PDF文件

#Didier Stevens' PDF tools:析，识别和创建 PDF 文件(包含PDFiD，pdf-parser，make-pdf和 mPDF)

#Opaf: 开放 PDF 分析框架，可以将 PDF 转化为 XML 树从而进行分析和修改

#Origapy: Ruby 工具Origami的 Python 接口，用于审查 PDF 文件

#pyPDF2: Python PDF 工具包包含：信息提取，拆分，合并，制作，加密和解密等等

#PDFMiner:从 PDF 文件中提取文本

#python-poppler-qt4: Python 写的 Poppler PDF 库，支持 Qt4

