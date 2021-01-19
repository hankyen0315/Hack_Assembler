from Parser import Parser





    
if __name__ == "__main__":
    file_name = input("Please enter the asm file you want to translate: ")
    abs_path = "D:\\College\\Introduction to Computer\\Hack_Assembler"
    
    parser = Parser(file_name,abs_path = abs_path)
    parser.parse()
    
    file_partial_name = file_name.split(".")[0]

    output_file = open(abs_path+"\\"+file_partial_name+".hack", "w")
    for code in parser.bin_file_buffer:
        output_file.write(code+"\n")
    output_file.close()





