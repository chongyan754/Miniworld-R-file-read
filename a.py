import re
#拆分


def a(s):
    s = s.strip()
    # 使用正则表达式去除时间戳和标签前缀
    result = re.sub(r'^\[\d{2}:\d{2}:\d{2}\]\[.*?\]\s*', '', s).strip()
    return result


chu=open("D:/来/"+"uio","a",encoding="utf-8")
asd=open("TriggerScript.log","r",encoding="utf-8")
asd=asd.readlines()
del asd[0]
zxc=0
while True:
    qwe=a(asd[zxc])
    if qwe[-1]=="r":
        chu=open("D:/来/"+qwe,"w")
    else:
        chu.write(qwe+"\n")
    zxc=zxc+1
