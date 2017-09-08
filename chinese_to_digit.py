dict ={u'零':0, u'一':1, u'二':2, u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, u'八':8, u'九':9, u'十':10, u'百':100, u'千':1000, u'万':10000,
    u'０':0, u'１':1, u'２':2, u'３':3, u'４':4, u'５':5, u'６':6, u'７':7, u'８':8, u'９':9,
    u'壹':1, u'贰':2, u'貳':2, u'叁':3, u'參':3, u'肆':4, u'伍':5, u'陸':6, u'陆':6, u'柒':7, u'捌':8, u'玖':9, u'拾':10, u'佰':100, u'仟':1000, u'萬':10000,
        u'億':100000000, u'亿':100000000, u'角':0.1, u'分':0.01}
def getResultForDigit(a,b):
    count = 0 
    result = 0
    tmp = 0
    Billion = 0
    #print(a)
    #print(b)
    while count < len(a):
        #print(count)
        tmpChr = a[count]
        tmpNum = dict.get(tmpChr, None)
        #print(tmpNum)
        #如果等于1亿
        if tmpNum is None:
            count += 1
            continue
        if tmpNum == 100000000:
            result = result + tmp #两百亿
            result = result * tmpNum
            #获得亿以上的数量，将其保存在中间变量Billion中并清空result
            Billion = Billion * 100000000 + result 
            result = 0
            tmp = 0
        #如果等于1万
        elif tmpNum == 10000:
            result = result + tmp
            result = result * tmpNum
            tmp = 0
        #如果等于十或者百，千
        elif tmpNum >= 10:
            if tmp == 0:
                tmp = 1
            result = result + tmpNum * tmp
            tmp = 0
        #如果是个位数
        elif tmpNum is not None:
            tmp = tmp * 10 + tmpNum
        count += 1
    result = result + tmp
    result = result + Billion
    #print(result)
    
    count = 0
    tmp = 0
    while count < len(b):
        tmpChr = b[count]
        tmpNum = dict.get(tmpChr, None)
        if tmpNum is None:
            count += 1
            continue
        if tmpNum == 0.1:
            result = result + tmpNum * tmp
            tmp = 0
        elif tmpNum == 0.01:
            result = result + tmpNum * tmp
            tmp = 0
        elif tmpNum is not None:
            tmp = tmpNum
        count += 1
    #print(result)
    return result





'''
#print(daxietext)
sumpricetext = daxietext.replace(" ", "")
print('sumpricetext:',sumpricetext)
if sumpricetext.find('角') != -1: #有小数,圆有时会识别不正确
    jiaoPos = sumpricetext.find('角')
    
    strdaxie = sumpricetext[jiaoPos-1:] # 小数部分
    sumpricetext = sumpricetext[:jiaoPos-2] #整数
    #strdaxie = strdaxie.replace("角","")
    #strdaxie = strdaxie.replace("分","")
elif sumpricetext.find('分') != -1: #有小数,圆有时会识别不正确
    jiaoPos = sumpricetext.find('分')
    
    strdaxie = sumpricetext[jiaoPos-2:] # 小数部分
    sumpricetext = sumpricetext[:jiaoPos-3] #整数
    #strdaxie = strdaxie.replace("角","")
    #strdaxie = strdaxie.replace("分","")
    
else:
    sumpricetext = sumpricetext.replace("整", "")
    sumpricetext = sumpricetext.replace("圆", "")
    strdaxie = ""
    
print('整数：',sumpricetext,'小数：',strdaxie)

sumpricetextd = str(getResultForDigit(sumpricetext, strdaxie))
'''
