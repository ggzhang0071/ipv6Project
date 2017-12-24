import argparse



parser = argparse.ArgumentParser(
        prog='learnbgame', 
        usage="python learnbgame.py [option]",# -i <input filename> -o <output filename>' 
        description="learnbgame help document", 
        epilog="And that’s how you‘d use learnbgame", 
        parents=[], 
        formatter_class=argparse.HelpFormatter, 
        prefix_chars='-', 
        fromfile_prefix_chars=None, 
        argument_default=None, 
        conflict_handler='error', 
        add_help=True, 
        allow_abbrev=True,
        )




parser.add_argument(
	'-txt',
	metavar='<input filename>',
	dest='txtf',
	help="specify input filenamen with txt format")
parser.add_argument(
	'-pdf',
	metavar='<input filename>',
	dest='pdff',
	help="specify input filenamen with pdf format")
parser.add_argument(
	'-csv',
	metavar='<output filename>',
	dest='csvf',
	help="specify output filenamen with csv format")
    
    

args = parser.parse_args()  


txtf = args.txtf
csvf = args.csvf
print(txtf,csvf)  