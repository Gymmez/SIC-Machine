def code_parser(instruction,type):
        if instruction[0] == "LDA":
                return f"\tmovzx rdi, {type} [{instruction[1]}]\n"
        if instruction[0] == "STA":
                if type== "byte":
                    return f"\tmov [{instruction[1]}], dil\n"
                elif type=="word":
                    return f"\tmov [{instruction[1]}], di\n"
        