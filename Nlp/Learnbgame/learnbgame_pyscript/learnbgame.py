
import csv
import sys
from googletrans import Translator
from learnbgameArgparser import args,parser
import txtTranCsv


def main(): 
    
    # 输入为文件txt,输出为文件csv
    if len(sys.argv) < 2:
    	parser.print_help()
    else:
    	
    	txtTranCsv.txTranCsv(args.txtf,args.csvf)





if __name__ == '__main__':
    main()

        
        




