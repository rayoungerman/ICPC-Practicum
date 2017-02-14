#Collaboration between Colin Lightfoot, Juliana Dajon, Rebecca Youngerman
def process( m , f, c ) :
    
    #Make list of all possible children: 
    possC = []
    
    
    for i in range(len(m)): 
        
        for j in range(len(f)) :
            
            geneM = m[i]
            geneF = f[j]
            
            listM = list(str(geneM))
            listF = list(str(geneF))
            
            
            #compare genes and add possible C genes to list
            child = ""        
            
            for a in range(len(listM)) : 
     
                if listM[a] == "0" and listF[a] == "0": 
                    child = child + "0" 
                    
                if listM[a] == "1" and listF[a] == "1": 
                    child = child + "1"   
                    
                if listM[a] == "1" and listF[a] == "0": 
                    child = child + "1"
                    
                if listM[a] == "0" and listF[a] == "1": 
                    child = child + "1"               
                
    
            possC.append(child)
    
    
    ##################################################################
    
    #Compare actual Children to possible children and record gene matches
    for key in range(len(c)):
        
        matches = 0
        matchesList = []    
        
        for possible in range(len(possC)):
            
            #actual child is list that includes gene sequence and highest number of 
            #matches
            
            actChild = c[key]
            possChild = possC[possible]
            
            actChildList = list(str(actChild[0]))
            possChildList = list(str(possChild))
            
    
            
            for a in range(len(possChildList)):
                
                if actChildList[a] == possChildList[a] : 
                    matches += 1
                    
            matchesList.append(matches)
            matches = 0; 
            
        #Find max number of matches
        maxMatch = max(matchesList)
        
        #add max number of matches to value of specific child
        c[key][1] = maxMatch
       
    
    #####################################################################
        
    #iterate through children list, and output number of mutations.
    #mutation = length of gene list - 
    
    for key, value in c.items():
        
        #number of sequences
        n = len(value[0])
        
        #number of mutations = number of sequences minus
        mutation = n - value[1]
        
        num = key + 1
        
        print("Child "+ str(num) + " has a minimum of " + str(mutation) + " mutations.")


        
        
######################################################


#Read input file

import sys

sourceFile = sys.argv[1]
textFile = open(sourceFile)

m = []
f = [] 
c = {0 : [] }

countX = 0
numC = 0

for line in textFile :
    
    l = line.strip().split()
    
    
    #in one set, add each line to m, f, or c lists
    if l[0] != "X" :
        
        countX = 0
        
        if l[0] == "M" :
            
            m.append(l[1])
            
        if l[0] == "F" :
            
            f.append(l[1])
        
        if l[0] == "C" :
            
            c[numC] = [ l[1] , 0 ]
            numC += 1
            
            
        
    #if line is X, call process function
    #clear m, f, c lists/dictionaries
    
    
    if l[0] == "X" :
        
        if countX == 1: 
            break
        
        countX += 1
        
        
        process( m, f, c)
        
        m = []
        f = [] 
        c = {0 : [] }
        numC = 0
         
        
#################################################  
