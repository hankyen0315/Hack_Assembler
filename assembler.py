from sys import argv
from os import getcwd
from Parser import Parser





    
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:python assembler.py <asmfile.asm>")
    file_name = str(argv[1])
    file_partial_name = file_name.split(".")[0]
    abs_path = str(getcwd())
    
    parser = Parser(file_name,abs_path = abs_path)
    parser.parse()
    
    
    output_file = open(abs_path+"\\"+file_partial_name+".hack", "w")
    for code in parser.bin_file_buffer:
        output_file.write(code+"\n")
    output_file.close()





