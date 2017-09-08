import re
import json

flag = 0
def money(str_money,flag):
    num_money = re.findall(r'\d+\.?\d+|\d+', str_money)[0]
    if '.' not in num_money:
        if flag == 2:
            e = len(num_money) - 1
        if flag == 4:
            e = len(num_money) - 2
        list_money = list(num_money)
        list_money.insert(e, ".")
        num_money = "".join(list_money)
    return num_money

def pretreatment(rtn,dirName,fileName):
    rtn = rtn.replace(' ', '')
    print(rtn)
    with open('traffic.txt', 'a', encoding='utf-8') as f:
        f.write('\n\n' + dirName + fileName + '\n')
        f.write(rtn + '\n')
        print(11111)

def file_save(filestr):
    # print(json.dumps(data, indent=2))
    taxistr = json.dumps(filestr, ensure_ascii=False)
    # taxistr = str(filestr)
    with open('traffic.txt', 'a', encoding='utf-8') as f:
        f.write(taxistr)

def sub(rtn):
    flag = 1
    print('地铁发票')
    substr = {}
    substr['票据类型'] = '地铁发票'
    try:
        # print(rtn)
        pattern = re.compile(r'发票代码(\d{12})', re.S)
        sub_code = pattern.findall(rtn)[0]
        print('发票代码:' + sub_code)
        substr['发票代码'] = sub_code
    except Exception as e:
        substr['发票代码'] = ''
        pass
    try:
        num = re.compile(r'发票号码(\d+)', re.S)
        sub_num = num.findall(rtn)[0]
        print('发票号码:' + sub_num)
        substr['发票号码'] = sub_num
    except Exception as e:
        substr['发票号码'] = ''
        pass
    try:
        sub_money = re.findall(r'[壹|贰|叁|肆|伍|陆|柒|捌|玖|拾].*?元整', rtn, re.S)[0]
        print('金额：' + sub_money)
        substr['金额'] = sub_money
    except Exception as e:
        substr['金额'] = ''
        pass
    file_save(substr)

def train(rtn):
    flag = 2
    print('火车发票')
    trainstr = {}
    try:
        check_in = re.findall(r'检票:\w+|检票口\w+', rtn, re.S)[0]
        check_in = re.findall(r'[A-Z]?\d+[A-Z]?', check_in, re.S)[0]
        trainstr['检票口'] = check_in
        print(check_in)
    except Exception as e:
        trainstr['检票口'] = ''
        pass
    try:
        train_startend = re.findall(r'([\u4E00-\u9FA5]{2,7}站).*?([\u4E00-\u9FA5]{2,7}站)', rtn, re.S)[0]
        train_start = train_startend[0]
        train_end = train_startend[1]
        trainstr['起始站'] = train_start
        trainstr['终点站'] = train_end
        print('起始站：' + train_start, '终点站:' + train_end)
    except Exception as e:
        trainstr['起始站'] = ''
        trainstr['终点站'] = ''
        pass
    try:
        train_num = re.findall(r'\w+\s?(K\d+|G\d+|D\d+|Z\d+|Y\d+|T\d+)', rtn, re.S)[0]
        trainstr['车号'] = train_num
        print('车号：' + train_num)
    except Exception as e:
        trainstr['车号'] = ''
        pass
    try:
        train_date = re.findall(r'\d+年\d+月\d+日?', rtn, re.S)[0]
        # train_date = re.sub(r'\s', '', train_date)
        if train_date[-1] != '日':
            train_date = train_date + '日'
        trainstr['日期'] = train_date
        print('日期：' + train_date)
    except Exception as e:
        trainstr['日期'] = ''
        pass
    try:
        str_money = re.findall(r'\d+\.?\d*元|¥.*?元|\d+\.\d', rtn, re.S)[0]
        train_money = money(str_money,flag)
        print('金额：' + train_money)
        trainstr['金额'] = train_money
    except Exception as e:
        trainstr['车费'] = ''
        pass
    try:
        train_seatnum = re.findall(r'\d{2}车.*?号|\d{2}#\w+|\d{2}#.*?号|\d{2}车无座|\d{2}车.*?铺', rtn, re.S)[0]
        if (len(train_seatnum) >= 7) and (train_seatnum[-1] != ('号' or '铺')):
            train_seatnum = train_seatnum[:-1] + '号'
        if (len(train_seatnum) < 7) and (train_seatnum[-1].isdigit()):
            train_seatnum = train_seatnum + '号'
        trainstr['座位号'] = train_seatnum
        print('座位号：' + train_seatnum)
    except Exception as e:
        trainstr['座位号'] = ''
        pass
    try:
        seat_type = re.findall(r'(\w等座|商务座|新空调\w{2})', rtn, re.S)[0]
        trainstr['座位类型'] = seat_type
        print('座位类型：' + seat_type)
    except Exception as e:
        trainstr['座位类型'] = ''
        pass
    file_save(trainstr)

def bus(rtn):
    flag = 3
    busstr = {}
    busstr['票据类型'] = '大巴发票'
    print('汽车大巴发票')
    try:
        buscode = re.findall(r'发票代码(\d+)', rtn, re.S)[0]
        busstr['发票代码'] = buscode
        print('发票代码' + buscode)
    except Exception as e:
        busstr['发票代码'] = ''
        pass
    try:
        busnum = re.findall(r'发票号码(\d+)', rtn, re.S)[0]
        busstr['发票号码'] = busnum
        print('发票号码' + busnum)
    except Exception as e:
        busstr['发票号码'] = ''
        pass
    try:
        busprice = re.findall(r'\w+元|\w+元整', rtn, re.S)[0]
        busstr['金额'] = busprice
        print(busprice)
    except Exception as e:
        busstr['金额'] = ''
        pass
    file_save(busstr)

def coach(rtn):
    flag = 4
    coach = '长途客车发票'
    coachstr = {}
    coachstr['票据类型'] = coach
    print('长途客车发票')
    try:
        coachcode = re.findall(r'发票代码:?(\d+)', rtn, re.S)[0]
        print('发票代码:' + coachcode)
        coachstr['发票代码'] = coachcode
    except Exception as e:
        coachstr['发票代码'] = ''
        pass
    try:
        coachnum = re.findall(r'发票号码(\d+)', rtn, re.S)[0]
        print('发票号码：' + coachnum)
        coachstr['发票号码'] = coachnum
    except Exception as e:
        coachstr['发票号码'] = ''
        pass
    try:
        coachprice = re.findall(r'\d+\.?\d+元|\d+\.\d{2}元？', rtn, re.S)[0]
        coach_price = money(coachprice,flag)
        print('金额：' + coach_price)
        coachstr['金额'] = coach_price
        # print('Jine')
    except Exception as e:
        coachstr['金额'] = ''
        pass
    try:
        coachdate = re.findall(r'\d+-\d+-\d+', rtn, re.S)[0]
        coachstr['日期'] = coachdate
        print('日期：' + coachdate)
    except Exception as e:
        coachstr['日期'] = ''
        pass
    file_save(coachstr)
def taxi(rtn):
    flag = 5
    print('出租车发票')
    taxi = '出租车发票'
    taxistr = {}
    taxistr['票据类型'] = taxi
    try:
        taxicode = re.findall(r'1\d{11}', rtn, re.S)[0]
        taxinum = re.findall(r'\d{12}.*?(\d{8})', rtn, re.S)[0]
        print(taxicode)
        print(taxinum)
        taxistr['发票编码'] = taxicode
        taxistr['发票号码'] = taxinum
    except Exception as e:
        taxistr['发票编码'] = ''
        taxistr['发票号码'] = ''
        pass
    try:
        taxiprice = re.findall(r'¥\d+\.?\d{2}', rtn, re.S)[0]
        print(taxiprice)
        taxistr['金额'] = taxiprice
    except Exception as e:
        taxistr['金额'] = ''
        pass
    try:
        taxidate = re.findall(r'\d{4}-\d{2}-\d{2}', rtn, re.S)[0]
        print(taxidate)
        taxistr['日期'] = taxidate
    except Exception as e:
        taxistr['日期'] = ''
        pass
    file_save(taxistr)

def boad(rtn):
    flag = 6
    boadstr = {}
    print('船渡发票')
    boadstr['票据类型'] = '船渡发票'
    try:
        boad_price = re.findall(r'票价.*?(\d+\.\d+)', rtn, re.S)[0]
        boadstr['金额'] = boad_price
        print('金额：' + boad_price)
    except Exception as e:
        boadstr['金额'] = ''
        pass
    try:
        start_end = re.findall(r'(\w+)-→(\w+)', rtn, re.S)[0]
        boad_start = start_end[0]
        boad_end = start_end[1]
        boadstr['起始站'] = boad_start
        boadstr['终点站'] = boad_end
        print('起始点：' + boad_start, '终点站：' + boad_end)
    except Exception as e:
        boadstr['起始站'] = ''
        boadstr['终点站'] = ''
        pass
    try:
        boad_num = re.findall(r'\w+(\d{12})', rtn, re.S)[0]
        boad_code = re.findall(r'号码\s+?(\d+)', rtn, re.S)[0]
        print('发票号码：' + boad_num, '发票编码：' + boad_code)
        boadstr['发票号码'] = boad_num
        boadstr['发票编码'] = boad_code
    except Exception as e:
        boadstr['发票号码'] = ''
        boadstr['发票编码'] = ''
        pass
    file_save(boadstr)







