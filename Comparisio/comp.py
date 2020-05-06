from glob import glob
import time
from datetime import datetime,timedelta, date
import numpy as np
#import numpy as np
#from google.colab import files

if __name__ == '__main__':
    fp = input('Enter filename1 ddmm: ')
    L2=open(fp+'.NRX','r')
    line2=L2.readlines()[2:]
    lst=[]
    for i in range (0,len(line2)):
        for j in range (25):
            if('-A' in line2[i][j:j+2] or '-B' in line2[i][j:j+2] and 'M - MAIN METER' not in line2[i] and  'S - STANDBY METER' not in line2[i] and  'C - CHECK METER' not in line2[i] and 'L - LOSSES METER' not in line2[i]):
                #print(line2[i][j-7:j+2])
                lst.append(line2[i][j-7:j+2])
            
    fp2 = input('Enter filename2 ddmm: ')
    L22=open(fp2+'.NRX','r')
    line22=L22.readlines()[2:]
    lst2=[]
    for i in range (0,len(line22)):
        for j in range (25):
            if('-A' in line22[i][j:j+2] or '-B' in line22[i][j:j+2] and 'M - MAIN METER' not in line22[i] and  'S - STANDBY METER' not in line22[i] and  'C - CHECK METER' not in line22[i] and 'L - LOSSES METER' not in line22[i]):
                #print(line22[i][j-7:j+2])
                lst2.append(line22[i][j-7:j+2])
             
            
    comp=[] 
    for i in range(len(lst)):
        if(lst[i] not in lst2):
            comp.append(lst[i])
    
    net=[]
    L1=open('MASTER.DAT','r')
    line1=L1.readlines()[2:]
    lst=[]
    for i in range (len(comp)):
        for j in range (0,len(line1)):
            if(comp[i] in line1[j]):
                net.append(line1[j])        
            
            
    np.savetxt("Comparision list.txt",net,fmt='%s')         
    print("\n Total comp =",len(comp))
    time.sleep(3)   
    exit()