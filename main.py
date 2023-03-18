temp = 0
inp = None

#I -> input(inp) cm8
#P -> print(temp , end="") cm1
#A -> print(chr(temp) , end="") cm2
#R -> inp,temp = (0 , None) cm3
#+ -> temp+=1 cm4
#- -> temp-=1 cm5
#E -> print("\n") cm6
#D -> print(inp , end="") cm7
class commands:
    def cm1():
        print(temp , end="")
    def cm2():
        print(chr(temp) , end="")
    def cm3():
        global temp , inp
        inp,temp = (None , 0)
    def cm4():
        global temp
        temp += 1
    def cm5():
        global temp
        temp -= 1
    def cm6():
        print()
    def cm7():
        print(inp)
    def cm8():
        global inp
        inp = input()
dict = {
    "I":commands.cm8,
    "P":commands.cm1,
    "A":commands.cm2,
    "R":commands.cm3,
    "+":commands.cm4,
    "-":commands.cm5,
    "E":commands.cm6,
    "D":commands.cm7
}
with open("MyApp.ipar" , "r") as code:
    code = code.read()
for i in code:
    if i in dict:
        dict[i]()