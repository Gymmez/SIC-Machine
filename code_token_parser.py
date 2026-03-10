def code_parser(instruction,type):
        if instruction[0] == "LDA":
                return f"\tmovzx rdi, {type} [{instruction[1]}]\n"
        if instruction[0] == "STA":
                if type== "byte":
                        return f"\tmov [{instruction[1]}], dil\n"
                elif type=="word":
                        return f"\tmov [{instruction[1]}], di\n"
        if instruction[0]=="LDX":
                return f"\tmovzx rbx, {type} [{instruction[1]}]\n"
        if instruction[0]=="LDL":
               return f"\tmovzx rcx, {type} [{instruction[1]}]\n"
        if instruction[0]=="STX":
                if type== "byte":
                        return f"\tmov [{instruction[1]}], bl\n"
                elif type=="word":
                    return f"\tmov [{instruction[1]}], bx\n"
        if instruction[0]=="STL":
                if type== "byte":
                        return f"\tmov [{instruction[1]}], cl\n"
                elif type=="word":
                    return f"\tmov [{instruction[1]}], cx\n"
        if instruction[0]=="ADD":
                return f"\tmovzx r12, {type} [{instruction[1]}]\n\tadd rdi, r12\n"

        if instruction[0]=="SUB":
                return f"\tmovzx r12, {type} [{instruction[1]}]\n\tsub rdi, r12\n"

        if instruction[0]=="MUL":
                return f"\tmov rax, rdi\n\tmovzx r12, {type} [{instruction[1]}]\n\timul rax, r12\n\tmov rdi, rax\n"

        if instruction[0]=="DIV":
                return f"\tmov rax, rdi\n\tmovzx r12, {type} [{instruction[1]}]\n\txor rdx, rdx\n\tidiv r12\n\tmov rdi, rax\n"
        if instruction[0] in ["AND","OR"]:
                return f"\tmov rax,rdi\n\t movzx r12, {type} [{instruction[1]}] \n\t {instruction[0].lower()} rdi, r12\n"
        