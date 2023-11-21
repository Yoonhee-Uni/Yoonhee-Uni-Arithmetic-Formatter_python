def arithmetic_arranger(problems, bool=None):
    first = []
    second = []
    third = []
    forth = []
    check_digits=[]
    first_row = []
    second_row = []
    third_row = []
    forth_row = []

    if 5 < len(problems) :
        return "Error: Too many problems."
    try:
        for i in range(len(problems)):
                x = problems[i].split(" ")
                first.append(x[0])
                second.append(x[1])
                third.append(x[2])
                check_digits.append(int(x[0]))
                check_digits.append(int(x[2]))

                if x[1] == '+':
                    result = int(x[0]) + int(x[2])
                    forth.append(result)
                elif x[1] == '-':
                    result = int(x[0]) - int(x[2])
                    forth.append(result)
                else :
                    return "Error: Operator must be '+' or '-'."
        for i in check_digits:
            if 9999 < i :
                return "Error: Numbers cannot be more than four digits."         
            else : pass

        if len(first[0]) < len(third[0]):
            first_row.append("  "+" "*(len(third[0])-len(first[0]))+ first[0]+"    ")#(for 1 + 5987)
            second_row.append(second[0]+" "+third[0]+"    ")

        elif len(first[0]) == len(third[0]):    
            first_row.append("  "+ first[0]+"    ") #(for 45+45)
            second_row.append(second[0]+" "+third[0]+"    ")
        else:
            first_row.append("  "+first[0]+"    ")    #(for 123+49)  
            second_row.append(second[0]+" "+" "*(len(first[0])-len(third[0]))+third[0]+"    ")
        third_row.append("-"*(len(second_row[0])-4)+"    ")
        if bool:
            forth_row.append(" "*((len(third_row[0])-len(str(forth[0]))-4))+str(forth[0])+ "    ")

        for i in range(1,len(first)-1):
            if len(first[i]) < len(third[i]):
                first_row.append(" "+" "*(len(third[i]))+ first[i]+"    ")#(for 1 + 5987)
                second_row.append(second[i]+" "+third[i]+"    ")
            elif len(first[i]) == len(third[i]):    
                first_row.append("  "+ first[i]+"    ") #(for 45+45)
                second_row.append(second[i]+" "+third[i]+"    ")
            else:
                first_row.append("  "+first[i]+"    ")    #(for 123+49)  
                second_row.append(second[i]+" "+" "*(len(first[i])-len(third[i]))+third[i]+"    ")
            third_row.append("-"*(len(second_row[i])-4)+"    ")
            if bool: 
                forth_row.append(" "*((len(third_row[i])-len(str(forth[i]))-4))+str(forth[i])+ "    ")

        if len(first[-1]) < len(third[-1]):
            first_row.append(" "+" "*(len(third[-1]))+ first[-1])#(for 1 + 5987)
            second_row.append(second[-1]+" "+third[-1])
        elif len(first[-1]) == len(third[-1]):    
            first_row.append("  "+ first[-1]) #(for 45+45)
            second_row.append(second[-1]+" "+third[-1])
        else:
            first_row.append("  "+first[-1])    #(for 123+49)  
            second_row.append(second[-1]+" "+" "*(len(first[-1])-len(third[-1]))+third[-1])
        third_row.append("-"*(len(second_row[-1])))
        if bool: 
            forth_row.append(" "*((len(third_row[-1])-len(str(forth[-1]))))+str(forth[-1]))


        x ="".join(first_row)
        y ="".join(second_row)
        z ="".join(third_row)
        a ="".join(forth_row)

        if bool :
            output = (f"{x}" "\n" f"{y}" "\n"f"{z}" "\n"f"{a}")
        else : 
            output = (f"{x}" "\n" f"{y}" "\n" f"{z}" f"{a}")


        return output
    except ValueError:
        return "Error: Numbers must only contain digits."