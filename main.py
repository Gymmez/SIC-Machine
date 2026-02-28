import os
import sys
from code_token_parser import code_parser
found_start=0
found_end=0
variable_type={}
code_tokens=[]
data_tokens=[]
bss_tokens=[]
data_direc=["BYTE","WORD"]
bss_direc=["RESW","RESB"]
classA_instructs=["ADD","AND","COMP","STA","DIV","J","JEQ","JGT","JLT","JSUB","LDA","LDCH","LDL","MUL","OR","RD","RSUB","TIX"]
#Lexing
def lexer(line, j):
    line = line.replace(",", " ")
    words = line.strip().split()
    
    if not words or words[0] == "." or words[0] in ["START", "END"]:
        return


    if len(words) == 2:
        if words[0] in classA_instructs:
            code_tokens.append(words)
        else:
            print(f"Unknown instruction at line {j}: {words}")
            sys.exit(22)


    elif len(words) == 3:
        mnemonic = words[1]
        if mnemonic in classA_instructs:
            code_tokens.append(words)
        elif mnemonic in data_direc:
            data_tokens.append(words) 
        elif mnemonic in bss_direc:
            bss_tokens.append(words)
        else:
            print(f"Unknown instruction at line {j}: {words}")
            sys.exit(22)

#Checking for START and END labels        
def start_end_checker(line):
    global found_start, found_end
    line=line.replace(","," ")
    words=line.strip().split()
    if words[0]=="START":
        found_start+=1
    if words[0]=="END":
        found_end+=1
#Parser
def parser():
    global variable_type
    with open("main.s", "w") as f:
        f.write("section .data\n")

        for instruction in data_tokens:
            if instruction[1]=="WORD":
                f.write(f"\t{instruction[0]} dw {instruction[2]}\n")
                variable_type[f"{instruction[0]}"]="word"
            if instruction[1]=="BYTE":
                f.write(f"\t{instruction[0]} db {instruction[2]}\n")
                variable_type[f"{instruction[0]}"]="byte"
        f.write("section .text\nglobal _start\n_start:\n")

        for instruction in code_tokens:
            if instruction[0] not in classA_instructs:
                f.write(f"{instruction[0]}:\n")
                type=variable_type.get(instruction[2])
                code=code_parser(instruction[1:],type)
                f.write(code)
            else:
                type=variable_type.get(instruction[1])
                code=code_parser(instruction,type)
                f.write(code)
        f.write("\tmov rax, 60\n\tsyscall\n")
        
        
    
def process_sic_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    if not file_path.lower().endswith('.sic'):
        print("File must end with .sic")
        sys.exit(1)
    i=1
    try:
        with open(file_path, 'r') as file:
            for line in file:
                start_end_checker(line)
            if found_start!=1 or found_end!=1:
                print("START or END labels not recognised")
                sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")

    try:
        with open(file_path, 'r') as file:
            for line in file:
                lexer(line,i)
                i+=1
    except Exception as e:
        print(f"Error: {e}")
    parser()
if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_sic_file(sys.argv[1])
    else:
        print("python script.py <filename.sic>")