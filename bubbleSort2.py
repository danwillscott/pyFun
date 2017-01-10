def bubble(x):
    #TURN x INTO A LIST IF IT's NOT ALREADY A LIST
    if type(x)!=list:
        xaslist=[]
        c=0
        while c<len(x):
            xaslist.append(x[c])
            c+=1
        print ("we have now switched the original non-list",x,"to be the list",xaslist)
        x=xaslist
     
    if len(x)<2:
        print ("the input is too short to sort")
        return;
    #THE LINE BELOW IS THE REAL TRICK FOR THIS ALGORITHM   
    possswitch=len(x)*(len(x)-1)/2 #the nunber of total examinations of pairs needed is the sum 
    #of the positive integers less than or equal to x
    loopcount=0
    while possswitch>0:
        i=0;
        while i<len(x)-loopcount-1:
            print ("considering the pair of chars",x[i],"and",x[i+1])
            if x[i]>x[i+1]:
                temp=x[i]
                x[i]=x[i+1]
                x[i+1]=temp
                print ("just did a switch")
            i+=1;
            possswitch-=1;
        loopcount+=1
    print("after doing all",int(possswitch),"examinations of pairs, we have:",x)
    return
bubble(x);