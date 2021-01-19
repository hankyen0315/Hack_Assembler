from sys import argv
from os import getcwd
from Parser import Parser





    
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:python assembler.py <asmfile.asm>")
    file_name = str(argv[1])
    file_partial_name = file_name.split(".")[0]
    
    sub_dir_asm = "\\Hack Assembly"
    sub_dir_bin = "\\Hack Machine Code"
    abs_path = str(getcwd())
    
    abs_path_to_input = abs_path + sub_dir_asm
    parser = Parser(file_name,abs_path = abs_path_to_input)
    parser.parse()
    
    abs_path_to_ouput = abs_path+sub_dir_bin
    output_file = open(abs_path_to_ouput+"\\"+file_partial_name+".hack", "w")
    
    for code in parser.bin_file_buffer:
        output_file.write(code+"\n")
    output_file.close()





