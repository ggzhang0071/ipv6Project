
import csv
import argparse 
from googletrans import Translator
from learnbgameArgparser import args
import txtTranCsv


def main(): 
    #print(args)
    # 输入为文件txt,输出为文件csv
    txtTranCsv.txTranCsv(args.txtf,args.csvf)





if __name__ == '__main__':
    main()

        
        




