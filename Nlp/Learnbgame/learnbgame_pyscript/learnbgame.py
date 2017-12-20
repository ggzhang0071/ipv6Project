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

        
        




