import graphviz

with open("input.txt") as f:
    data = f.read().split('\n\n')

xyvals = data[0].splitlines()
expr = data[-1].splitlines()

dict = {}

for e in expr:
    s = e.split(" ")
    op1 = s[0]
    instr = s[1]
    op2 = s[2]
    res = s[4]
    dict[res] = (op1,op2,instr)
    print(s)
for x in xyvals:
    v = x.split(": ")
    xvar = v[0]
    xval = v[1]
    dict[xvar] = int(xval)
    print(v)

dot = graphviz.Digraph('adder',comment='adder')

outputn = 0
for k in dict:
    if dict[k] != 1 and dict[k] != 0:
        val = dict[k]
        op1, op2, func = val[0], val[1], val[2]
        if func == 'XOR':
            dot.node(k, style="filled", fillcolor="darkred", shape="star")# + "(" + k + ")")
        elif func == 'OR':
            dot.node(k, style="filled", fillcolor="darkblue", shape="diamond")# + "(" + k + ")")
        elif func == 'AND':
            dot.node(k, style="filled", fillcolor="darkgreen", shape="triangle")# + "(" + k + ")")
        dot.node(op1)
        dot.node(op2)
        dot.edge(op1,k)
        dot.edge(op2,k)
        if k.startswith('z'):
            outputnode = str(outputn)
            dot.node(outputnode,k)
            dot.edge(k,outputnode)
            outputn += 1

#8 wires swapped
#wrong connections:
#vcg
#pgq, green should be blue

#rrs, rvc need to be swapped
#vcg, z24
#z20, jgb
#z09, rkf?
to_swap = ['rrs','rvc','vcg','z24','z20','jgb','z09','rkf']
to_swap.sort()
print(",".join(to_swap))
dot.render(directory='doctest-output')