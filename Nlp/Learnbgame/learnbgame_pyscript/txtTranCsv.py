import csv 
from googletrans import Translator
from learnbgameArgparser import args
from languageHash import LANGUAGES


def txTranCsv(txtf,csvf):
    filro = open(txtf,'r')
    filwo = open(csvf,'w')
    translator = Translator()
    contents = filro.read()
    dst = ''
    src = 'auto'
    # 当输入内容超过限制的时候的解决 分段处理
    if len(contents) > 4891:    
        print("翻译的长度超过限制！！！") 
    else:
        for lan in LANGUAGES:
            dst = lan
            transcontent = translator.translate(contents,dest=dst,src=src)
            print(transcontent.text,'----',lan)
            filwo.write(transcontent.text+'\n')
    filro.close()  
    filwo.close()


def main():
    txTranCsv(args.txtf,args.csvf)


if __name__ == '__main__':
    main()