
def onSetupParameters(scriptOp):
    op('randNums').clear()
    op('randNums').insertCol(['0', '0'], 0)
    op('randNums').insertRow(['0', '0'], 1)
    return

def onPulse(par):
    return

def onCook(scriptOp):
    scriptOp.clear()
    currMSel = 0
    ranNums = op('randNums')
    checks = op('checks')
    tgrCurr = op('grCurr')
    treCurr = op('reCurr')
    tfoCurr = op('foCurr')
    cntrMenu = op('cntrlMenu1')['p1_x']
    clpSelect = op('clipSelect').par.value0
        
    #Checking for equal values to trigger the change

    if tgrCurr[0,0] == op('growlOld').par.value0:
        op('gcheck').par.value0 = 1
    else:
        op('gcheck').par.value0 = 0

    if treCurr[0,0] == op('revOld').par.value0:
        op('rcheck').par.value0 = 1
    else:
        op('rcheck').par.value0 = 0

    if tfoCurr[0,0] == op('foOld').par.value0:
        op('fcheck').par.value0 = 1
    else:
        op('fcheck').par.value0 = 0

    #Hot n Cold Colour change    
    
    tcom = op('tCompare')
    grdiff = op('grdiff1').par.value0
    rediff = op('fodiff1').par.value0
    fodiff = op('rediff1').par.value0
    op('RGB').par.value0
    op('RGB').par.value1
    op('RGB').par.value2
    
    op('tCompare').clear()
    op('tCompare').appendRow([op('selGr')['chan1'],op('selFo')['chan2'],op('selRe')['chan3']])
    op('tCompare').appendRow([grdiff,rediff,fodiff])
 
 
 
    if op('mccheck')['chan1'] == 1 and tcom[1,0] == 0:
        op('RGB').par.value0 = 0.75
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan1'] == 1 and 10 >= tcom[1,0] >= 1:
        op('RGB').par.value0 = 1
        op('RGB').par.value1 = 0.5
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan1'] == 1 and 20 >= tcom[1,0] >= 11:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0.75
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan1'] == 1 and tcom[1,0] >= 21:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0.75



    if op('mccheck')['chan3'] == 1 and tcom[1,2] == 0:
        op('RGB').par.value0 = 0.75
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan3'] == 1 and 10 >= tcom[1,2] >= 1:
        op('RGB').par.value0 = 1
        op('RGB').par.value1 = 0.5
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan3'] == 1 and 20 >= tcom[1,2] >= 11:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0.75
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan3'] == 1 and tcom[1,2] >= 21:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0.75         
   

   
    if op('mccheck')['chan2'] == 1 and tcom[1,1] == 0:
        op('RGB').par.value0 = 0.75
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0    
    elif op('mccheck')['chan2'] == 1 and 10 >= tcom[1,1] >= 1:
        op('RGB').par.value0 = 1
        op('RGB').par.value1 = 0.5
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan2'] == 1 and 20 >= tcom[1,1] >= 11:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0.75
        op('RGB').par.value2 = 0
    elif op('mccheck')['chan2'] == 1 and tcom[1,1] >= 21:
        op('RGB').par.value0 = 0
        op('RGB').par.value1 = 0
        op('RGB').par.value2 = 0.75        
        
            
    #growl - amplification change
            
    if tcom[1,0] == 0:
        op('ampchange').par.value0 = 0
    elif tcom[1,0] >= 1 and tcom[1,0] <= 10:
        op('ampchange').par.value0 = 3
    elif tcom[1,0] >= 11 and tcom[1,0] <= 20 :
        op('ampchange').par.value0 = 6
    elif tcom[1,0] >= 21:
        op('ampchange').par.value0 = 10
            
    #force to feedback change
            
    if tcom[1,1] == 0:
        op('feechange').par.value0 = 1
    elif tcom[1,1] >= 1 and tcom[1,1] <= 10:
        op('feechange').par.value0 = 0.6
    elif tcom[1,1] >= 11 and tcom[1,1] <= 20 :
        op('feechange').par.value0 = 0.3
    elif tcom[1,1] >= 21:
        op('feechange').par.value0 = 0
            
    #reverb to pixellation change
            
    if tcom[1,2] == 0:
        op('pixchange').par.value0 = 0
    elif tcom[1,2] >= 1 and tcom[1,2] <= 10:
        op('pixchange').par.value0 = 0.3
    elif tcom[1,2] >= 11 and tcom[1,2] <= 20 :
        op('pixchange').par.value0 = 0.6
    elif tcom[1,2] >= 21:
        op('pixchange').par.value0 = 1            
    

    #Performing the Clip Change

    if op('null5')['chan1'] == 1:
        for i in range(2):
            op('grfoRand').par.value0 += 0.01
            ranNums[0,i] = op('null6')['chan1']
            op('grfoRand').par.value0 += 0.01
            ranNums[1, i] = op('null6')['chan1']
            op('revrandConst').par.value0 += 0.01
            ranNums[2, i] = op('null8')['chan1']

        #Randomising the Values

        op('growlOld').par.value0 = ranNums[0,0]
        op('revOld').par.value0 = ranNums[1,0]
        op('foOld').par.value0 = ranNums[2,0]

        op('grBase').par.value0 = ranNums[0,1]
        op('reBase').par.value0 = ranNums[1,1]
        op('foBase').par.value0 = ranNums[2,1]


    return