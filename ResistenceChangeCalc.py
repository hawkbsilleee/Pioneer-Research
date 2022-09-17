import pandas as pd

no_of_lines = 28
x = ""
for i in range(no_of_lines):
    x+=input() + " "

index = 0
comma_count = 0
old_line = 0
listl = []
for character in x:
  index += 1
  if character == ",":
    comma_count += 1
    if comma_count % 2 == 0:
      new_line = str(x[old_line:index])
      old_line = x.find(new_line) + len(new_line)
      listl.append(new_line)

new_list = []
for line in listl:
  start = line.find(",")
  new_line = line[start+1:len(line)-1]
  new_list.append(new_line)

varChange = []
rChange = []
for i in range(0, len(new_list), 2):
  if float(new_list[i]) > float(new_list[i+1]):
    rChange.append("-R")
    rChange.append(None)
    varChange.append("z")
    varChange.append(None)
  elif float(new_list[i]) == float(new_list[i+1]):
    rChange.append("R")
    rChange.append(None)
    varChange.append("s")
    varChange.append(None)
  else:
    rChange.append("+R")
    rChange.append(None)
    varChange.append("x")
    varChange.append(None)

rName = []
for i in range(1,15):
  rName.append("Rf"+str(i))
  rName.append("Rc"+str(i))

df = pd.DataFrame(new_list, columns = ['Power Dissipation'])
df["Resistance Change"] = rChange
df["Resistor"] = rName
df["Variable"] = varChange
print(df)

key = ["R1, R2, R3, R4, R5, R6, R9, R10, R11, R12, R13, R14, R26, R27"]
counter = 0
for i in range(len(varChange)):
  if varChange[i] != None:
    print(varChange[i])
    counter += 1




