from algo_mockup import *
import os

N = Rule("N", Production("astronomers"), Production("ears"), Production("stars"), Production("telescope"))
V = Rule("V",Production("saw"))
P = Rule("P",Production("with"))

PP = Rule("PP")
NP = Rule("NP")
NP.add(Production(NP, PP))
NP.add(Production(N))
PP.add(Production(P, NP))

VP = Rule("VP")
VP.add(Production(V,NP))
VP.add(Production(VP, PP))
S = Rule("S", Production(NP, VP))

if os.path.isfile("./Debug.txt") != True:
    open("./Debug.txt","x")

f= open("./Debug.txt","w")


for tree in build_trees(parse(S, "astronomers saw stars with ears",f)):
    print ("--------------------------")
    tree.print_()

f.close()
