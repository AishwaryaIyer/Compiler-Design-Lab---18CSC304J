import re

keyword = ['break','case','char','const','continue','default','do','int','else','enum','extern','float','for','goto','if',
            'long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['clrscr()','printf(','scanf(','getch()','main()']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
specialsymbol = ['@','#','$','_','!']
separator = [',',':',';','\n','\t','{','}','(',')','[',']']

kw = set()
op = set()
sp = set()
bf = set()
sep =set()
hf = set()
num = set()
iden = set()

file = open('lexical.txt','r+')
contents = file.read()
splitCode = contents.split() #split program in word based on space
length = len(splitCode)      # count the number of word in program
for i in range(0,length):
    if splitCode[i] in keyword:
        kw.add(splitCode[i])
        continue
    if splitCode[i] in operators:
        op.add(splitCode[i])
        continue
    if splitCode[i] in specialsymbol:
        sp.add(splitCode[i])
        continue
    if splitCode[i] in built_in_functions:
        bf.add(splitCode[i])
        continue
    if splitCode[i] in separator:
        sep.add(splitCode[i])
        continue
    if re.match(r'(#include*).*', splitCode[i]):
        hf.add(splitCode[i])
        continue
    if re.match(r'^[-+]?[0-9]+$',splitCode[i]):
        num.add(splitCode[i])
        continue
    if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):
        iden.add(splitCode[i])
print("\nType\t\t\t|Count\t\t|Values")
print("-------------------------------------------------------------")

print("\nHeader File\t\t|",str(len(hf))+"\t\t|",hf)

print("\nBuilt-in functions\t|",str(len(bf))+"\t\t|",bf)

print("\nKeywords\t\t|",str(len(kw))+"\t\t|",kw)

print("\nOperators\t\t|",str(len(op))+"\t\t|",op)

print("\nSpecial Symbols\t\t|",str(len(sp))+"\t\t|",sp)  

print("\nNumerals\t\t|",str(len(num))+"\t\t|",num)

print("\nIdentifiers\t\t|",str(len(iden))+"\t\t|",iden)

print("\nSeparators\t\t|",str(len(sep))+"\t\t|",sep)

    