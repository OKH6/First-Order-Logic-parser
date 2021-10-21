import pydot
import sys
import re
nonTerminals=["Formula","Expression","Predicate","Equality","Conncetive","Var","Const","VAR_or_CONST","Equality_Symbol","QuantSymbol","Connective_Symbol","Negative_Symbol"]
print('\n')
graph = pydot.Dot(graph_type='graph')
def FirstOF(First, symbols):
	if not symbols:
		return set()
	return First[symbols[0]]
Log = open("LogFile.txt", "w")

def FindFirsts(CFG,terminals):
	firstSets = {}
	for head, prods in CFG.items():
		firstSets[head] = set()
		for prod in prods:
			for symbol in prod:
				if symbol in terminals:
					firstSets[symbol] = set([symbol])
	while True:
		changes = firstSets.copy()
		for head, prods in CFG.items():
			for prod in prods:
				if not prod[0]:
					firstSets[head] = firstSets[head].union(set([""]))
				else:
					firstSets[head] = firstSets[head].union(firstSets[prod[0]])
				for i in range(1, len(prod)):
					firstSets[head] = firstSets[head].union(firstSets[prod[0]])
		if changes == firstSets:
			return firstSets

def FindFollows(First,CFG, terminals):
	Follows = {}
	for head in CFG:
		if head == 'Start':
			Follows['Start'] = set(['$'])
		else:
			Follows[head] = set()
	while True:
		changes = Follows.copy()
		for (head, prods) in CFG.items():
			for prod in prods:

				for i in range(len(prod) - 1):

					if prod[i] not in terminals:

						Follows[prod[i]] = \
							Follows[prod[i]].union(FirstOF(First,
								prod[i + 1:]))
		if changes == Follows:
			return Follows
if len(sys.argv)<2:
	print("Please enter a file name")
	Log.write("No file name was provided")
	Log.close()
	exit()

f = open(sys.argv[1], "r")
LIST=[[],[],[],[],[],[],[]]
terminals=[]
curent=0
for x in f:
	for word in x.split():
		if word=="variables:":
			curent=0
			continue
		elif word=="constants:":
			curent=1
			continue
		elif word=="predicates:":
			curent=2
			continue
		elif word=="equality:":
			curent=3
			continue
		elif word=="connectives:":
			curent=4
			continue
		elif word=="quantifiers:":
			curent=5
			continue
		elif word=="formula:":
			curent=6
			continue

		if curent==1 or curent==0:
			if word in nonTerminals:
				print("you cannot use the symbol '"+word+"' as it is  it is used in the grammer as a NON TERMINAL symbol")
				Log.write("you cannot use the symbol '"+word+"' as it is  it is used in the grammer as a NON TERMINAL symbol")
				Log.close()
				exit()
			if word not in terminals:
				terminals.append(word)
			elif curent!=6:
				if curent==1:
					print("you cannot use the symbol '"+word+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
					Log.write("you cannot use the symbol '"+word+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
					Log.close()
					exit()
				if curent==0:
					print("you cannot use the symbol '"+word+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
					Log.write("you cannot use the symbol '"+word+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
					Log.close()
					exit()
		if curent==4 or curent==5:
			if re.match("^[A-Za-z0-9_\\\\]*$", word):
				pass
			else:
				print("Please only use letters, numbers, underscore and backslah for connectives and quantifiers.")
				Log.write("Please only use letters, numbers, underscore and backslah for connectives and quantifiers.")
				Log.close()
				exit()
		if curent==3:
			if re.match("^[A-Za-z0-9_\\\\=]*$", word):
				pass
			else:
				print("Please only use letters, numbers, underscore, backslah and = for equality.")
				Log.write("Please only use letters, numbers, underscore, backslah and = for equality.")
				Log.close()
				exit()

		LIST[curent].append(word)

		#print(word
variables=LIST[0]
constants=LIST[1]
predicates=LIST[2]
equality=LIST[3]
connectives=LIST[4]
quantifiers=LIST[5]
formula=LIST[6]
for x in equality:
	if x in terminals:
		print("you cannot use the same symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.write("you cannot use the same symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.close()
		exit()
	if x in nonTerminals:
		print("you cannot use the symbol '"+x+"' in the input file for equality as it is used as a NON TERMINAL symbol in the grammer")
		Log.write("you cannot use the symbol '"+x+"' in the input file for equality as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()
terminals+=equality
for x in connectives:
	if x in terminals:
		print("you cannot use the symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.write("you cannot use the symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.close()
		exit()
	if x in nonTerminals:
		print("you cannot use the symbol '"+x+"' in the input file for connectivesas as it is used as a NON TERMINAL symbol in the grammer")
		Log.write("you cannot use the symbol '"+x+"' in the input file for connectivesas as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()
terminals+=connectives
for x in quantifiers:
	if x in terminals:
		print("you cannot use the symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.write("you cannot use the symbol '"+x+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.close()
		exit()
	if x in nonTerminals:
		print("you cannot use the symbol '"+word+"' in the input file for quantifiers as it is used as a NON TERMINAL symbol in the grammer")
		Log.write("you cannot use the symbol '"+word+"' in the input file for quantifiers as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()
terminals+=quantifiers

#print(formula)
FF=[]
for x in formula:
	if "(" in x or ")" in x or "," in x:
		x=x.replace("("," ( ")
		x=x.replace(")"," ) ")
		x=x.replace(","," , ")
		x=x.split()
		for y in x:
			FF.append(y)
		continue
	FF.append(x)

formula=FF
if len(equality)!=1:
	print("ERROR please enter an equality sign in the input file")
	Log.write("ERROR please enter an equality sign in the input file")
	Log.close()
	exit()
if len(connectives)!=5:
	print("ERROR There should be 5 connectivety symbols in the input file")
	Log.write("ERROR There should be 5 connectivety symbols in the input file")
	Log.close()
	exit()
if len(quantifiers)!=2:
	print("ERROR There should be 2 quantifier symbols in the input file")
	Log.write("ERROR There should be 2 quantifier symbols in the input file")
	Log.close()
	exit()

neg=connectives.pop()
terminals.append("(")
terminals.append(")")
terminals.append(",")


CFG={}
CFG["Formula"]=[["Predicate"],["Quantifier_Symbol","Var","Formula"],["(","Expression",")"],["Negative_Symbol","Formula"]]
CFG["Expression"]=[["Equality"],["Conncetive"]]
CFG["Predicate"]=[]
CFG["Equality"]=[["VAR_or_CONST","Equality_Symbol","VAR_or_CONST"]]
CFG["Conncetive"]=[["Formula","Connective_Symbol","Formula"]]
CFG["VAR_or_CONST"]=[["Const"],["Var"]]
CFG["Var"]=[]
CFG["Const"]=[]
CFG["Equality_Symbol"]=[equality]
CFG["Quantifier_Symbol"]=[]
CFG["Connective_Symbol"]=[]
CFG["Negative_Symbol"]=[[neg]]
for x in predicates:
	x=x.replace("["," [ ")
	x=x.replace("]"," ] ")
	x=x.split()
	if len(x)<4:
		print("Predicate '"+x[0]+"' is of wrong format it should be in the following format: Name[Num]")
		Log.write("you cannot use the symbol '"+x[0]+"'in the input file for predicates as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()

	if x[0] in terminals:
		print("you cannot use the symbol '"+x[0]+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.write("you cannot use the symbol '"+x[0]+"' in more than one of these fields: equality,connectives,quantifiers,variables,constants and predicates")
		Log.close()
		exit()
	if x[0] in nonTerminals:
		print("you cannot use the symbol '"+x[0]+"'in the input file for predicates as it is used as a NON TERMINAL symbol in the grammer")
		Log.write("you cannot use the symbol '"+x[0]+"'in the input file for predicates as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()
	terminals.append(x[0])
	if x[1]!="[" and x[3]!="]":
		print("Predicate '"+x[0]+"' is of wrong format it should be in the following format: Name[Num]")
		Log.write("you cannot use the symbol '"+x[0]+"'in the input file for predicates as it is used as a NON TERMINAL symbol in the grammer")
		Log.close()
		exit()



	num=int(x[2])
	add=[",","Var"]
	exp=[x[0],"(","Var"]
	for x in range(1,num):
		exp+=add
	exp.append(")")
	CFG["Predicate"].append(exp)
for x in variables:
	exp=[x]
	CFG["Var"].append(exp)
for x in constants:
	exp=[x]
	CFG["Const"].append(exp)
for x in connectives:
	exp=[x]
	CFG["Connective_Symbol"].append(exp)
for x in quantifiers:
	exp=[x]
	CFG["Quantifier_Symbol"].append(exp)
Output = open("Production rules.txt", "w")


for x in CFG:
	if len(CFG[x])==0:
		if x=="Const":
			nonTerminals[6]=""
			CFG["VAR_or_CONST"]=[["Var"]]
		if x=="Var":
			nonTerminals[5]=""
			CFG["VAR_or_CONST"]=[["Const"]]
		if x=="Predicate":
			nonTerminals[2]=""
			CFG["Formula"]=[["Quantifier_Symbol","Var","Formula"],["(","Expression",")"],["Negative_Symbol","Formula"]]
		continue
if len(CFG["Const"])==0 and len(CFG["Var"])==0:
	nonTerminals[7]=""
	CFG["VAR_or_CONST"]=[]
	print("NOTE you cannot make a grrammer without constants and varibles")

Output.write("Terminals : ")
for x in terminals:
	if x!=terminals[len(terminals)-1]:
		Output.write("'"+x+"'  ")
	else:
		Output.write("'"+x+"'\n\n")
Output.write("Non Terminals : ")
for x in nonTerminals:
	if x!=nonTerminals[len(nonTerminals)-1] and len(x)>0:
		Output.write("'"+x+"'  ")
	elif len(x)>0:
		Output.write("'"+x+"'\n\n\n")


Output.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Production rules :\n\n\n")

for x in CFG:
	if len(CFG[x])==0:
		continue


	Output.write(x+" -->")
	for y in CFG[x]:
		s=""
		for z in y:
			s+=" "+z
		l=len(CFG[x])
		if y!=CFG[x][l-1]:
			Output.write(s+" | ")
		else:
			Output.write(s)
	Output.write("\n")
	Output.write("\n")
Output.close()
for x in formula:
	if x not in terminals:
		print("Symbol '" + x +"' in the formula is not part of the Language please change it and try again ")
		Log.write("Symbol '" + x +"'in the formula is not part of the Language please change it and try again ")
		Log.close()
		exit()


First=FindFirsts(CFG,terminals)
#print("sdafasdfsafasf")
#print(First)
Follow=FindFollows(First,CFG,terminals)


table = {}

for head, prods in CFG.items():
	for prod in prods:
		first_set = FirstOF(First,prod)
		for terminal in first_set:
			table[head, terminal] = prod
for nonterminal in nonTerminals:
	for terminal in terminals:
		try:
			prod = table[nonterminal, terminal]
		except KeyError:
			pass


formula.append("$")
Count = 0
LenRead=0
stack = ["$","Formula"]
stackOver=[]
top = "Formula"
head=0
iDStoDraw=[]
FinishedId=[]
dict={}
usedIDS=[0]
lastpoped=""
graph.add_node(pydot.Node(0, label="Start"))
while top != "$":
	if len(sys.argv)==3 and sys.argv[2]=="show":
		print("\n")
		print("Stack : " ,end = '')
		print(stack)
	stackOver.append(stack.copy())
	#print(stack)
	if top == formula[Count]:
		Count = Count + 1
		if len(sys.argv)==3 and sys.argv[2]=="show":
			print( "Pass:symbol `{0}`  matches top of stack".format(top))
		#print( "Pass:symbol `{0}`  matches top of stack".format(top))
		lastpoped=top
		stack.pop()

	elif top in terminals:
		print("ERROR expected a {0} after '{1}' at position number {2}".format(stack[len(stack)-1], lastpoped,Count))
		Log.write("ERROR expected a {0} after '{1}' at position number {2}".format(stack[len(stack)-1], lastpoped,Count))
		Log.close()
		exit()
	else:
		try:
			prod = table[top, formula[Count]]
			stack.pop()
			if len(sys.argv)==3 and sys.argv[2]=="show":
				print ("Action: derived next rule/symbol to use using token `{1}`, from non terminal '{0}' which gives {2}".format(top, formula[Count], prod))
			#print ("Action: derived next rule/symbol to use using token `{1}`, from non terminal '{0}' which gives {2}".format(top, formula[Count], prod))
			Curr=[]
			for x in prod:
				#print(x)
				n=str(x)
				y=n.replace(","," ,")
				x=x.replace(",","1")
				if x not in usedIDS:

					usedIDS.append(x)
					Curr.append(x)
				else:
					for z in range(0,1000):
						x=x+str(z)
						x=x.replace(",","1")
						if x not in usedIDS:
							usedIDS.append(x)
							Curr.append(x)
							break
				if "\\"in y:
					y="\\"+y
				graph.add_node(pydot.Node(x, label=y))
				edge = pydot.Edge(head, x)
				graph.add_edge(edge)
				dict[x]=n
			Curr.reverse()
			iDStoDraw=iDStoDraw+Curr
			for x in range(0,len(iDStoDraw)):
				head=iDStoDraw.pop()
				if dict[head] in terminals:
					LenRead+=1
					continue
				else:
					break
			stack.extend(reversed(prod))
		except KeyError:
			print ("ERROR: Not able to find derivation of {0} on `{1}` there is missing symbol between `{2}` and `{1}` at position {3}. Formula is of invalid format".format(top, formula[Count],formula[Count-1],Count))
			Log.write("ERROR: Not able to find derivation of {0} on `{1}` there is missing symbol between `{2}` and `{1}` at position {3}. Formula is of invalid format".format(top, formula[Count],formula[Count-1],Count))
			Log.close()
			exit()
	top = stack[-1]
print("\nformula is valid, parse tree generated. you can find tree in parse_tree.png ")
Log.write("formula is valid, parse tree generated. you can find tree in parse_tree.png ")
Log.close()
graph.write_png('parse_tree.png')
