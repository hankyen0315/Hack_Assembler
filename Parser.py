import io
from hack_asm_spec import *

class Parser():
    def __init__(self,file_name,abs_path = ""):
        self.bin_file_buffer = []
        self.asm_file = open(abs_path+"\\"+file_name,"r")
        self.content = self.store_file()
        self.asm_file.close()
        self.label_map = {}
        self.variable_map = {}
        self.free_address = 16
        self.get_file_without_symbol()
        #self.debug_print_file()
        
    def debug_print_file(self):
        for line in self.content:
            print(line)
        
    def store_file(self):
        content = []
        for line in self.asm_file.readlines():
            content.append(line)
        return content
    
    def get_file_without_symbol(self):
        line_count = 0
        for i in range(len(self.content)):
            line = self.content[i]
            line = Parser.get_clean_line(line)
            if (line == ''):
                self.content[i] = line
                continue
            line = self.process_symbol(line,line_count)
            if (line == ''):
                self.content[i] = line
                continue
            line_count += 1
            self.content[i] = line
           
    @staticmethod
    def get_clean_line(line):
        line = Parser.remove_spaces(line)
        line = Parser.remove_comments(line)
        line = Parser.remove_newline_char(line)
        return line 
        
    @staticmethod
    def remove_spaces(line):
        line = line.replace(' ', '')
        return line
    @staticmethod
    def remove_comments(line):
        split_line = line.split("//", 1)
        line = split_line[0]
        return line
    @staticmethod
    def remove_newline_char(line):
        split_line = line.split('\n', 1)
        line = split_line[0]
        return line

    
    def process_symbol(self,line,address):
        starter = line[0]
        if starter == "(":
            label_name = line[1:-1]
            self.assign_address_to_label(label_name,address) 
            line = ""        
        return line
    
    
    
    
    def parse(self):
        for line in self.content:
            not_empty,result_bin_code = self.parse_line(line)
            if not_empty:
                self.bin_file_buffer.append(result_bin_code)
        
    def parse_line(self,line):
        not_empty = True
        if line == "":
            not_empty = False
            return not_empty,""
        elif line[0] == "@":
            result_bin_code = self.get_a_instruction_code(line)
        else:
            result_bin_code = Parser.get_c_instruction_code(line)
        
        return not_empty,result_bin_code
    

    def get_a_instruction_code(self,line):
        binary_code = ""
        address = line[1:]

        if address in predefined_symbol:
            address = Parser.replace_predefined_symbol(address)
        elif address in self.label_map:
            address = self.replace_label(address)
        elif address in self.variable_map:
            address = self.replace_variable(address)
        else:
            is_variable = not address.isdecimal()
            if is_variable:
                self.assign_address_to_variable(address)
                address = self.replace_variable(address)
        try:
            address = int(address)
            binary_code = bin(address)[2:].zfill(16)
        except:
            print("error: address can't be non number")
            print(address)
        return binary_code
        
    @staticmethod
    def get_c_instruction_code(line):
        dest_code, rest = line.split("=") if "=" in line else ("", line)
        comp_code, jump_code = rest.split(";") if ";" in rest else (rest, "")
        
        binary_code = "111{}{}{}".format(comp[comp_code],dest[dest_code],jump[jump_code])

        return binary_code


    @staticmethod
    def replace_predefined_symbol(symbol):
        return predefined_symbol[symbol]
        
    
    def assign_address_to_label(self,label_name,address):
        self.label_map[label_name] = address
    
    def replace_label(self,label_name):
        return self.label_map[label_name]
        
    def assign_address_to_variable(self,variable_name):
        self.variable_map[variable_name] = self.free_address
        self.free_address += 1
        
    def replace_variable(self,variable_name):
        return self.variable_map[variable_name]
        
