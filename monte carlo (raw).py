import random
import matplotlib.pyplot as plt
import numpy as np
import time
from tqdm import tqdm
lowerbust=30
higherprofit=60
samplesize=10000 
startingfunds=100000
wagersize=100
wagercount=100000
maxwager=[]

def roll_dice():
    roll= random.randint(1,100)
    if roll==100:
        # print(f'roll was {roll} you lose')
        return False
    elif roll<50:
        # print(f'roll was 1-50, you lose')
        return False
    elif roll>=50 and roll<100:
        # print(f'roll was between 51-99 you win')
        return True


# lent=[]
# x=0
# while x<100:
#     result=roll_dice()
#     lent.append(result)
#     x+=1

# g=len(lent)
# t= np.sum(lent)/g
# print(t)
james=[]
def simple_bettor(funds,initialwager,wagercount,color):
    global simplebust
    global simpleprofit
    value= funds
    wager=initialwager
    wX=[]
    wY=[]
    currentwager=1

    while currentwager<=wagercount:
        if value<=0:
            value= 0
            wX.append(currentwager)
            wY.append(value)
            break
        
        elif roll_dice():
            value+=wager
            wX.append(currentwager)
            wY.append(value)
        else:
             value-=wager
             wX.append(currentwager)
             wY.append(value)
        currentwager+=1
    if value<=0:
        value= 0
        simplebust+=1
    james.append(value)

    plt.plot(wX,wY,color)
    if value>funds:
        simpleprofit+=1

    

    #print(f'funds {value}')  
    return(value)  

def doublerbettor(funds,initialwager,wagercount,color):
    value= funds
    wager=initialwager
    global doublerbust
    global doublerprofit
    wX=[]
    wY=[]
    currentwager=1
    previouswager='win'
    previouswageramount=initialwager

    while currentwager<=wagercount:
        roll=random.randint(1,100)
        if previouswager=='win':
            # print('previous wager was a win')
            if roll_dice():
             value+=wager
            #  print(value)
             wX.append(currentwager)
             wY.append(value)
            else:
                value-=wager
                previouswager='loss'
                # print(value)
                previouswageramount=wager
                if value<=0:
                    wX.append(currentwager)
                    wY.append(value)
                    doublerbust+=1
                    break
                wX.append(currentwager)
                wY.append(value)
        elif previouswager=='loss':
            # print('previous wager was a loss')
            if roll_dice():
                wager=previouswageramount*2
                value+=wager
                wager=initialwager
                previouswager='win'
                # print(value)
                wX.append(currentwager)
                wY.append(value)
            else:
                wager= previouswageramount*2
                value-=wager
                previouswager='loss'
                # print(value)
                if value<=0:
                    # print("we went broke")
                    doublerbust+=1
                    break
                previouswageramount=wager
                wX.append(currentwager)
                wY.append(value)
        currentwager+=1
    # print(value)
    if value<=0:
        value=0
    james.append(value)
    plt.plot(wX,wY,color)
    if value> funds:
        doublerprofit+=1

def multibettor(funds,initialwager,wagercount):
    global multibust
    global multiprofit
    global Ret

    value=funds
    wager=initialwager
    # wX=[]
    # wY=[]
    currentwager=1
    previouswager='win'
    previouswageramount=initialwager
    roll=np.random.randint(1,101,size=wagercount)
    for rolls in roll:
        if previouswager=='win':
            if value<=0:
                multibust+=1
                break
            # print('previous wager was a win')
            if rolls>50:
             value+=wager
            #  print(value)
            #  wX.append(currentwager)
            #  wY.append(value)
            else:
                if value<=0:
                    multibust+=1
                    break
                value-=wager
                previouswager='loss'
                # print(value)
                previouswageramount=wager
                if value<=0:
                    # wX.append(currentwager)
                    # wY.append(value)
                    multibust+=1
                    break
                # wX.append(currentwager)
                # wY.append(value)
        elif previouswager=='loss':
            if value<=0:
                multibust+=1
                break
            # print('previous wager was a loss')
            if rolls>50:
                wager=previouswageramount*randommulti
                value+=wager
                wager=initialwager
                previouswager='win'
                # print(value)
                # wX.append(currentwager)
                # wY.append(value)
            else:
                if value<=0:
                    multibust+=1
                    break
                wager= previouswageramount*randommulti
                value-=wager
                previouswager='loss'
                # print(value)
                if value<=0:
                    # print("we went broke")
                    multibust+=1
                    break
                previouswageramount=wager
                # wX.append(currentwager)
                # wY.append(value)
        currentwager+=1
    # print(value)
    if value<=0:
        value=0
    # james.append(value)
    # plt.plot(wX,wY,color)
    if value> funds:
        multiprofit+=1
    Ret+=value

def dAlambert(funds,initialwager,wagercount):
 global Ret
 global dabust
 global daprofit
 value=funds
 wager= initialwager
 currentwager=1
 previouswager='win'
 previouswageramount=initialwager
 roll=np.random.randint(1,101,size=wagercount)
 for rolls in roll:
    if previouswager=='win':
        if value<=0:
            dabust+=1
            break
        if wager<=initialwager:
            pass
        else:
            wager= previouswageramount - randomwager
        if rolls<=50:
            value+=wager
            # Wx.append(currentwager)
            # Wy.append(value)
            previouswageramount=wager
        else:
            if value<=0:
                break
            value-=wager
            # Wx.append(currentwager)
            # Wy.append(value)
            previouswager='loss'
            previouswageramount=wager
            if value<=0:
                dabust+=1
                break
    elif previouswager=='loss':
        if value<=0:
            dabust+=1
            break
        wager= previouswageramount+randomwager
        if (value-wager)<=0:
            wager=value
        if rolls<=50:
            value+=wager
            # Wx.append(currentwager)
            # Wy.append(value)
            previouswager='win'
            previouswageramount=wager
        else:
            if value<=0:
                dabust+=1
                break
            value-=wager
            # Wx.append(currentwager)
            # Wy.append(value)
            previouswageramount=wager
            if value<=0:
                dabust+=1
                break
            
    currentwager+=1
 if value> funds:  
     daprofit+=1
 if value<=0:
     value=0
 Ret+=value
#  t=np.max(maxwager)
#  maxwager=[]
#  maxwager.append(t)
#  plt.plot(Wx,Wy,'g')            



simplebust,simpleprofit,doublerbust,doublerprofit=0,0,0,0




multisampsize=10000
while True:
    multibust,multiprofit=0,0
    Ret=0
    wagersize=round(np.random.uniform(startingfunds*0.0001,startingfunds*0.01),2)
    wagercount=np.random.randint(10,10000)
    wagersizepercent= ((wagersize/startingfunds)*100)
   

    randommulti=random.uniform(1.20,3.00)
    for i in tqdm(range(multisampsize), desc=f"Running Multiplier {randommulti:.2f} with wagersize {wagersizepercent:.2f}% and wagercount {wagercount}"):
        multibettor(startingfunds,wagersize,wagercount)
    roipercentage=(((Ret/multisampsize)-startingfunds)/startingfunds)*100
    
    if ((multibust/multisampsize)*100 <lowerbust ) and ((multiprofit/multisampsize)*100)>higherprofit and roipercentage>5:
        print(f'''for multiplier {randommulti:.2f} 
        bust rate: {multibust/multisampsize*100:.2f} %
        profit rate: {multiprofit/multisampsize*100:.2f} %''')
        print("wager size percentage is :", wagersizepercent)
        print("wager count is :", wagercount)
        print("roi percentage is :", roipercentage)
        saveFile= open("MonteCarloMultiplier.csv","a")
        saveLine= '\n'+str(randommulti)+ ','+str(wagersizepercent)+','+str(wagercount)+ str(roipercentage)+','+'g'
        saveFile.write(saveLine)
        saveFile.close()
    elif ((multibust/multisampsize)*100 <=lowerbust ) and ((multiprofit/multisampsize)*100)>higherprofit and roipercentage<-5:
        print(f'''for multiplier {randommulti:.2f} 
        bust rate: {multibust/multisampsize*100:.2f} %
        profit rate: {multiprofit/multisampsize*100:.2f} %''')
        print("wager size percentage is :", wagersizepercent)
        print("wager count is :", wagercount)
        print("roi percentage is :", roipercentage)
        saveFile= open("MonteCarloMultiplier.csv","a")
        saveLine= '\n'+str(randommulti)+ ','+str(wagersizepercent)+','+str(wagercount)+','+str(roipercentage)+','+'r'
        saveFile.write(saveLine)
        saveFile.close()


        #print(f'for multiplier {randommulti:.2f} the bust rate was {multibust/multisampsize*100:.2f} % and the profit rate was {multiprofit/multisampsize*100:.2f} % this is a loser')  
# i=0
# j=0
# roi=[]
# wagercountlist=[]
# wageramountlist=[]
# while j<1000:  
#     dabust,daprofit,Ret=0,0,0 
#     randomwager=round(np.random.uniform(startingfunds*0.0001,startingfunds*0.01),2)
#     currentsample=1
#     wagercount= np.random.randint(10,10000)
#     wagersizepercent= ((randomwager/startingfunds)*100)
    

#     print(randomwager)
#     for i in tqdm(range(samplesize), desc="Simulating"):
#         dAlambert(startingfunds, randomwager, wagercount)
#         i+=1
#     percentroi= (((Ret/samplesize)-startingfunds)/startingfunds)*100
# #((dabust/samplesize)*100 <lowerbust ) and ((daprofit/samplesize)*100)>higherprofit and
#     if percentroi>=5:
#         print(f'percent roi is {percentroi:.2f} %')
#         print(f'wager amount: {randomwager:.2f}')
#         print(f'wager count: {wagercount}')
#         print(f'bust rate: {dabust/samplesize*100:.2f} %')
#         print(f'profit rate: {daprofit/samplesize*100:.2f} %')
#         print("Wager size percentage is :",wagersizepercent)
#         print('')
#         saveFile= open("MonteCarloliberal.csv","a")
#         saveLine= '\n'+str(percentroi)+ ','+str(wagersizepercent)+','+str(wagercount)+','+',g'
#         saveFile.write(saveLine)
#         saveFile.close()
#     elif percentroi<=-5:
#         print(f'percent roi is {(((Ret/samplesize)-startingfunds)/startingfunds)*100:.2f} %')
#         print(f'wager amount: {randomwager:.2f}')
#         print(f'wager count: {wagercount}')
#         print(f'bust rate: {dabust/samplesize*100:.2f} %')
#         print(f'profit rate: {daprofit/samplesize*100:.2f} %')
#         print("Wager size percentage is :",wagersizepercent)
#         print("percent roi is :",percentroi)
#         print('')
#         saveFile= open("MonteCarloliberal.csv","a")
#         saveLine= '\n'+str(percentroi)+ ','+str(wagersizepercent)+','+str(wagercount)+','+',r'
#         saveFile.write(saveLine)
#         saveFile.close()

#     roi.append((((Ret/samplesize)-startingfunds)/startingfunds)*100)
#     wagercountlist.append(wagercount)
#     wageramountlist.append(randomwager)
    # j+=1

# ax=plt.subplot(111,projection='3d')
# ax.scatter(wagercountlist,wageramountlist,roi)
# ax.set_xlabel('Wager Count')
# ax.set_ylabel('Wager Amount')
# ax.set_zlabel('ROI')
# plt.colorbar()
# plt.show()
# tqdm wraps the range(samplesize)
# for i in tqdm(range(samplesize), desc="Simulating"):
#     dAlambert(startingfunds, wagersize, wagercount)

# print(f'death rate: {dabust/samplesize*100:.2f} %')
# print(f'profit rate: {(daprofit/samplesize)*100:.2f} %')
# print(f'average return: {((Ret/samplesize)-startingfunds):.2f}')
# print(f'{samplesize*startingfunds} is the total amount of money bet')
# print(f'({Ret-(samplesize*startingfunds)}) is the ROI')
# print(np.max(maxwager))
# plt.show()
# print(f'death rate: {((simplebust+doublerbust)/float(2*xx))*100:.2f} %')
# print(f'survival rate: {100-(((simplebust+doublerbust)/float(2*xx)))*100:.2f}')
# print(f''' The average account value is {np.mean(james):.3f}
# The highest account value is {np.max(james)}
# The lowest account value is {np.min(james)} 
# The number of people at 0 is {james.count(0)}
# and the total number of bettors was {len(james)}''')
# print('''

# ''')
# print(f'Simple bettor bust chance:{(simplebust/samplesize)*100:.2f}')
# print(f'Doubler bettor bust chance:{(doublerbust/samplesize)*100:.2f}')
# print(f'Simple bettor profit chance:{(simpleprofit/samplesize)*100:.2f}')
# print(f'Doubler bettor profit chance:{(doublerprofit/samplesize)*100:.2f}')

# plt.axhline(0,color="red")
# plt.axhline(10000,color="blue")
# plt.grid()
# plt.show()       


# x=0
# while x<1000:
#     simple_bettor(10000,100,40000)
#     x+=1

# plt.ylabel('Account Value')
# plt.xlabel('Wager Count')
# plt.grid()
# plt.show()












# losses=[]
# wins=[]
# for i in range(10000):

#     j=simple_bettor(10000,100,1000)
#     if j<10000:
#         losses.append(j)
#     else:
#         wins.append(j)

# print(f'cases for wins were {len(wins)}') 
# print(f'cases for losses were {len(losses)}')

# print(f'''
# The average profit/loss amount after 10,000 trials was {(((np.sum(wins)+np.sum(losses))/10000)-10000):.2f}
#  this represents a percentage ratio of {(((( (np.sum(wins)+np.sum(losses))/10000)-10000)/10000)*100):.2f}%''')

