# 银行回单及对账单的识别、火车票机票的识别、其他单据的识别
# 要求混合识别、系统自动分类、各类单据需要识别的关键信息模板由系统预先定义

from nameko.standalone.rpc import ClusterRpcProxy
import paper_re

# 出租车
# dirName = 'local/20170814134929990391'
# fileName = 'pic0049.JPG'
#火车 testdata.txt
dirName = 'local/20170821105407371168'
fileName = 'image00035.JPG'
# #船渡
##testdata1.txt
# dirName = 'local/20170814144147937928'
# fileName = 'pic0062.JPG'
# # # #地铁
# dirName = 'local/20170821105506462742'
# fileName = 'image00056.JPG'
# #飞机
# dirName = 'local/20170814140429947755'
# fileName = 'pic0056.JPG'
# 大巴
# dirName = 'local/20170814144913082941'
# fileName = 'pic0064.JPG'
#长途汽车
# dirName = 'local/20170814144434164768'
# fileName = 'pic0063.JPG'

try:
    rpcsvrip = '47.93.227.224'
    rpcmqname = 'bill_invoice'
    CONFIG = {'AMQP_URI': "amqp://dzf:" + rpcmqname + "@" + rpcsvrip + '/dzfhost'}
    with ClusterRpcProxy(CONFIG) as cluster_rpc:
        rtn = cluster_rpc.imgRecog.recogbillimage(dirName, fileName)
    if rtn:
        if isinstance(rtn, dict) and rtn.get('err_msg'):
            print(rtn.get('err_msg'))
        else:

            paper_re.pretreatment(rtn,dirName,fileName)
            if ('市政'in rtn) or ('一卡通' in rtn) or ('地铁' in rtn) or('铁运营' in rtn):
                paper_re.sub(rtn)

            elif ('船票' in rtn):
                paper_re.boad(rtn)

            elif ('航空' in rtn) or ('航班' in rtn):
                print('飞机发票')

            elif ('新空调' in rtn) or ('等座' in rtn) or('铁路' in rtn):
                paper_re.train(rtn)

            elif ('巴士' in rtn):
                paper_re.bus(rtn)

            elif ('旅客' in rtn) or ('机打客票' in rtn) or('客运' in rtn):
                paper_re.coach(rtn)

            elif('预约叫车'in rtn) or ('出租' in rtn) or('Distance' in rtn):
                paper_re.taxi(rtn)

            else:
                print('没有这种类型')

except Exception as error:
    print('caught this error (rpc): ' + repr(error))



