# -*- encoding=utf8 -*-
__author__ = "Ke"

from airtest.core.api import *

auto_setup(__file__)


# 当前屏幕尺寸
screen = G.DEVICE.snapshot(quality=ST.SNAPSHOT_QUALITY)
global ver, hor, offset 
(ver, hor) = (screen.shape[0], screen.shape[1]) 
offset = (36,87) # 上状态栏尺寸固定36，下操作栏尺寸固定51，总共87
#offset = (0, 0) # 使用 ADB 的情况下，这种连接的实际使用情况为0
print("\n窗口的分辨率为{}*{},游戏画面的分辨率为{}*{}\n".format(hor, ver, hor, (ver-offset[1]-2)))

def TransPosition(App_position):
    print("touch((int({:.2f}*hor), int({:.2f}*(ver-offset[1])+offset[0])))".format(App_position[0]/hor,App_position[1]/(ver-offset[1])))
    
TransPosition((1250,300))

# 所有的菜单选项都以一个暂停两秒进行
menu = [(int(0.098*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.232*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.366*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.500*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.634*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.768*hor),int(0.936*(ver-offset[1])+offset[0])),
        (int(0.902*hor),int(0.936*(ver-offset[1])+offset[0]))]

class maoxian(object):
    def __init__(self):
        self.zhuxian = (int(0.6 *hor), int(0.4 *(ver-offset[1])+offset[0]))
        self.tansuo  = (int(0.78*hor), int(0.25*(ver-offset[1])+offset[0]))
        self.dixia   = (int(0.89*hor), int(0.25*(ver-offset[1])+offset[0]))
        self.diaocha = (int(0.78*hor), int(0.5 *(ver-offset[1])+offset[0]))
        self.tuandvi = (int(0.89*hor), int(0.5 *(ver-offset[1])+offset[0]))
        self.JJC     = (int(0.6 *hor), int(0.75*(ver-offset[1])+offset[0]))
        self.PJJC    = (int(0.8 *hor), int(0.75*(ver-offset[1])+offset[0]))
        self.huodong = (int(0.45*hor), int(0.75*(ver-offset[1])+offset[0]))
maoxians = maoxian()

fanhui   = (int(0.01 *hor), int(0.05*(ver-offset[1])+offset[0]))
kongbai  = (int(0.50 *hor), int(0.12*(ver-offset[1])+offset[0]))

OK_danxiang    = (int(0.58*hor), int(0.68*(ver-offset[1])+offset[0]))
OK_duoxiang    = (int(0.55*hor), int(0.88*(ver-offset[1])+offset[0])) #刚好不会碰到冒险的位置
OK_zhenghe     = (int(0.58*hor), int(0.83*(ver-offset[1])+offset[0]))

OK_jiesuan     = (int(0.84*hor), int(0.91*(ver-offset[1])+offset[0]))

Battle_jiahao  = (int(0.91*hor), int(0.62*(ver-offset[1])+offset[0]))
Battle_saodang = (int(0.75*hor), int(0.62*(ver-offset[1])+offset[0]))
Battle_kaishi  = (int(0.87*hor), int(0.84*(ver-offset[1])+offset[0]))

#扭蛋
def Missoin_niudan():
    touch(menu[5])
    sleep(2.0)
    touch((int(0.92*hor),int(0.14*(ver-offset[1])+offset[0])))
    sleep(1.0)
    touch((int(0.76*hor),int(0.64*(ver-offset[1])+offset[0])))
    sleep(1.0)
    touch((int(0.61*hor),int(0.68*(ver-offset[1])+offset[0])))
    sleep(5.0)
    touch(OK_zhenghe)
    sleep(2.0)

#探索
def Mission_tansuo():
    for i in range(2):
        touch(menu[3])
        sleep(2.0)
        touch(maoxians.tansuo)
        sleep(1.0)
        touch((int((0.62+0.24*i)*hor), int(0.5*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch((int(0.75*hor), int(0.25*(ver-offset[1])+offset[0]))) #首个
        sleep(1.0)
        touch((int(0.91*hor), int(0.62*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch((int(0.73*hor), int(0.62*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch((int(0.61*hor), int(0.68*(ver-offset[1])+offset[0])))
        sleep(5.0)
        touch(fanhui)
        sleep(1.0)

#两个竞技场
def Mission_JJC():
    # range 前一个是JJC，后一个是PJJC
    for i in range(2):
        touch(menu[3])
        sleep(2.0)
        touch((int((0.6 + 0.2*i)*hor), int(0.75*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch(kongbai) #防守成功
        sleep(1.0)
        touch((int(0.3 *hor), int(0.65*(ver-offset[1])+offset[0]))) #收取
        sleep(1.0)
        touch(OK_danxiang)
        sleep(1.0)
        touch((int(0.5 *hor), int(0.3 *(ver-offset[1])+offset[0]))) #找第一个人打架
        sleep(2.0)
        for j in range(int(1+2*i)):
            touch(Battle_kaishi)
            sleep(1.0)
        sleep(int(120 - 20*i))
        touch(OK_jiesuan)
        sleep(5.0)
        touch(OK_duoxiang) #排名上升的结算确认
        sleep(2.0)
    
#地下城
def Mission_dixia(Area, Mission_quit = 0):
    # Mission_quit 表示是否提前撤退
    team = [(int(0.833*hor), int(0.320*(ver-offset[1])+offset[0])),
            (int(0.833*hor), int(0.540*(ver-offset[1])+offset[0])),
            (int(0.833*hor), int(0.760*(ver-offset[1])+offset[0]))]
    if Area == 3:
        Layers = [(int(0.73*hor), int(0.60*(ver-offset[1])+offset[0])),
                  (int(0.71*hor), int(0.58*(ver-offset[1])+offset[0])),
                  (int(0.35*hor), int(0.53*(ver-offset[1])+offset[0])),
                  (int(0.69*hor), int(0.53*(ver-offset[1])+offset[0])),
                  (int(0.30*hor), int(0.41*(ver-offset[1])+offset[0])),
                  (int(0.30*hor), int(0.41*(ver-offset[1])+offset[0]))]
    elif Area == 4:
        Layers = [(int(0.50*hor), int(0.50*(ver-offset[1])+offset[0])),
                  (int(0.65*hor), int(0.50*(ver-offset[1])+offset[0])),
                  (int(0.50*hor), int(0.50*(ver-offset[1])+offset[0])),
                  (int(0.40*hor), int(0.50*(ver-offset[1])+offset[0])),
                  (int(0.50*hor), int(0.50*(ver-offset[1])+offset[0]))]
    touch(menu[3])
    sleep(2.0)
    touch(maoxians.dixia)
    sleep(2.0)
    touch((int((0.25*Area - 0.12)*hor), int(0.5 *(ver-offset[1])+offset[0]))) #3孤塔 4暗棱
    sleep(3.0)
    touch((int(0.7 *hor), int(0.7 *(ver-offset[1])+offset[0]))) # 确认
    sleep(5.0)
    for i in range(int(len(Layers))-1):
        touch(Layers[i])
        sleep(2.0)
        touch(Battle_kaishi) # 挑战
        sleep(1.0)
        #以下为队伍选择
        if i < 4:
            touch((int(0.903*hor),int(0.160*(ver-offset[1])+offset[0]))) # 队伍
            sleep(1.0)
            touch(team[0]) # 第一队
            sleep(1.0)
        if i == 4:
            touch((int(0.903*hor),int(0.160*(ver-offset[1])+offset[0]))) # 队伍
            sleep(1.0)
            touch(team[1]) # 第二队
        if i == 5:
            touch((int(0.903*hor),int(0.160*(ver-offset[1])+offset[0]))) # 队伍
            sleep(1.0)
            touch(team[2]) # 第三队 
            '''
        if i == 6:
            touch((int(0.903*hor),int(0.160*(ver-offset[1])+offset[0]))) # 队伍
            sleep(1.0)
            swipe(team[2], team[0], duration = 1.0)
            touch(team[1]) # 第四队
            '''
        sleep(1.0)
        touch(Battle_kaishi) # 战斗开始
        sleep(100)
        touch(OK_jiesuan) # 确认
        sleep(4.0)
        touch(OK_duoxiang) # OK
        sleep(6.0)
    if Mission_quit == 1: # 是否打不过进行跑路
        touch((int(0.92*hor), int(0.79*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch(OK_danxiang)
        sleep(1.0)
        
        
#行会点赞
def Mission_dianzan():
    touch(menu[0])
    sleep(2.0)
    touch((int(0.73*hor), int(0.80*(ver-offset[1])+offset[0])))
    sleep(3.0)
    touch((int(0.25*hor), int(0.67*(ver-offset[1])+offset[0])))
    sleep(2.0)
    touch((int(0.90*hor), int(0.38*(ver-offset[1])+offset[0])))
    sleep(2.0)
    touch(OK_danxiang)
    sleep(1.0)
    
#公会体力
def Mission_gonghui():
    touch(menu[4])
    sleep(4.0)
    touch((int(0.95*hor),int(0.80*(ver-offset[1])+offset[0])))
    sleep(2.0)
    touch(OK_duoxiang)
    sleep(2.0)
    
#副本主线
def fuben(n):
    for i in range(n):
        sleep(1.0)
        touch(Battle_kaishi)
        touch(Battle_kaishi)
        sleep(180)
        touch(kongbai) #好感度空白
        sleep(1.0)
        touch(kongbai) #空白
        sleep(1.0)
        touch(OK_jiesua)
        sleep(3.0)
        touch(kongbai) #商店空白
        touch(OK_jiesuan)
        sleep(3.0)
        touch(kongbai) #剧情空白

        
#扫荡，定义扫荡次数
def Battle_Clean(Cleantimes):
    touch(Battle_jiahao, times = Cleantimes)
    sleep(1.0)
    touch(Battle_saodang)
    sleep(1.0)
    touch(OK_danxiang)
    sleep(1.0)
    touch(OK_duoxiang) # 
    sleep(1.0)
    touch(OK_duoxiang) # 白OK
    sleep(1.0)
    
#副本困难
def Mission_kunnan(): 
    sleep(1.0)
    touch(menu[3])
    sleep(2.0)
    touch(maoxians.huodong)
    sleep(3.0)
    touch(fanhui)
    sleep(8.0)
    touch(fanhui)
    sleep(8.0)
    touch(fanhui)
    sleep(2.0)
    touch(maoxians.zhuxian)
    sleep(3.0)
    touch((int(0.90*hor), int(0.15*(ver-offset[1])+offset[0]))) #确保进入困难本
    sleep(3.0)
    touch((int(0.13*hor), int(0.45*(ver-offset[1])+offset[0]))) #困难第一关的位置
    sleep(1.0)
    for i in range(5):
        Battle_Clean(2)
        touch((int(0.84*hor), int(0.25*(ver-offset[1])+offset[0]))) #另一个空白
        sleep(1.0)
        touch((int(0.84*hor), int(0.25*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch((int(0.97*hor), int(0.46*(ver-offset[1])+offset[0]))) #下一步
        sleep(1.0)
    touch(fanhui)

#限时商店
def Mission_shop():
    sleep(1.0)
    touch(menu[0])
    sleep(4.0)
    touch((int(0.65*hor), int(0.80*(ver-offset[1])+offset[0])))
    sleep(2.0)
    for kind in range(16):
        touch((int(0.30*hor), int(0.63*(ver-offset[1])+offset[0])))
        sleep(1.0)
        touch((int(0.60*hor), int(0.83*(ver-offset[1])+offset[0])))
        touch((int(0.60*hor), int(0.88*(ver-offset[1])+offset[0])))
        sleep(1.0)
        if kind < 8:
            touch((int(0.94*hor), int(0.13*(ver-offset[1])+offset[0])))
        else:
            touch((int(0.27*hor), int(0.13*(ver-offset[1])+offset[0]))) # 首页的体力选项
        sleep(1.0)
        if kind == 7:
            touch((int(0.27*hor), int(0.13*(ver-offset[1])+offset[0]))) # 首页的体力选项
            sleep(1.0)
        
'''
Mission_shop()
sleep(10)
'''
Missoin_niudan()
Mission_tansuo()
Mission_dianzan()
Mission_JJC()
Mission_gonghui()
Mission_kunnan()

Mission_shop()

Mission_dixia(4, 1)

'''

#Battle_Clean(5)
#kunnan(5)
#fuben(10)
'''
