'''For a given set of training data examples stored in a .CSV file, implement 
and demonstrate the Candidate-Elimination algorithm to output a description of 
the set of all hypotheses consistent with the training examples.'''

import csv
file=open('lab3ds.csv')
data=list(csv.reader(file))[1:]
concepts=[]
target=[]
for i in data:
    concepts.append(i[:-1])
    target.append(i[-1])
specific_h=['0']*len(concepts[0])
general_h= [['?' for i in range(len(specific_h))] for i in range(len(specific_h))]
for i,instance in enumerate(concepts):
    if target[i]=="Yes":
        for x in range(len(specific_h)):
            if specific_h[x]== '0':
                specific_h[x]=instance[x]
            elif instance[x]!=specific_h[x]:
                specific_h[x]='?'
                general_h[x][x] = '?'
    if target[i]=="No":
        for x in range(len(specific_h)):
            if instance[x]!= specific_h[x]:
                general_h[x][x]=specific_h[x]
            else:
                general_h[x][x]='?'
indices=[i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']]
for i in indices:
    general_h.remove(['?','?','?','?','?','?'])
print("Final Specific:",specific_h,sep="\n")
print("Final General:",general_h,sep="\n")

