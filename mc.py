import random
#import anvil
from random import choice
import os
import re

try:
    import anvil
except ImportError:
    os.system("pip install anvil-parser")
    import anvil
#此处更新来自于@https://github.com/World-sudo的贡献


kuai=0
def chus():
    global block_id_map
    block_id_map={}
    block_id_map["0"]="air"
    block_id_map["104"]="stone"
    block_id_map["1"]="bedrock"
    block_id_map["3"]="water"
    block_id_map["101"]="dirt"
    block_id_map["106"]="sand"
    block_id_map["107"]="gravel"
    block_id_map["4095"]="stone"
    block_id_map["108"]="sandstone"
    block_id_map["6"]="flowing_lava"
    block_id_map["5"]="lava"
    block_id_map["402"]="coal_ore"
    block_id_map["100"]="grass_block"
    block_id_map["124"]="netherrack"
    block_id_map["401"]="iron_ore"
    block_id_map["667"]="red_sand"
    block_id_map["218"]="oak_leaves"
    block_id_map["23"]="jungle_wood"
    block_id_map["734"]="chest"
    block_id_map["1180"]="chest"
    block_id_map["801"]="chest"
    block_id_map["425"]="mossy_stone_bricks"
    block_id_map["502"]="cracked_stone_bricks"
    block_id_map["540"]="dark_oak_planks"
    block_id_map["210"]="spruce_planks"
    block_id_map["563"]="acacia_planks"
    block_id_map["209"]="jungle_planks"
    block_id_map["4"]="flowing_water"
    block_id_map["202"]="birch_log"
    block_id_map["207"]="birch_planks"
    block_id_map["422"]="chiseled_stone_bricks"
    block_id_map["411"]="iron_block"
    block_id_map["201"]="spruce_planks"
    block_id_map["200"]="oak_wood"

def extract_coordinates(s):
    numbers = re.findall(r'-?\d+', s)
    return (int(numbers[0]), int(numbers[1])) if len(numbers) >= 2 else None



def convert_block_id(custom_id):
    global kuai
    kuai=kuai+1
    """返回对照表中对应的 Minecraft 方块名和属性。如果没有，返回 ???"""
    try:
        return block_id_map[str(custom_id)]
    except:
        block_id_map[str(custom_id)]="iron_block"
        return block_id_map[str(custom_id)]



dai=os.listdir()
#dai=["x14z13.r"]
def chuasd():
    global yan_se
    global schu
    global ming
    global asd
    global yui
    global bina_l
    global sgu_f
    global y
    global x,z,qwe,chu_yun,yuan_x,yuan_z,qi_x,qi_z,region


    yan_se={}
    schu=open("总集","a")
    while dai[0][-1]!="r":
        del dai[0]
    ming=dai[0]
    del dai[0]
    print(ming)
    asd=open(ming,"r")
    asd=asd.readlines()
    yui={}
    bina_l=0
    sgu_f=0
    y=0
    x,z=0,0
    qwe={}
    chu_yun=[]
    region=anvil.EmptyRegion(extract_coordinates(ming)[0],extract_coordinates(ming)[1])
    print(region)
    yuan_x=extract_coordinates(ming)[0]*512
    yuan_z=extract_coordinates(ming)[1]*512
    qi_x=0
    qi_z=0

def extract_numbers(s):
    try:
        # 去掉首字符并分割
        s = s.rstrip('\n')  # 支持末尾多个\n的情况（如"\n\n"）
        content=s[1:]
        num_strs=content.split('/')
        num1=int(num_strs[0])
        num2=int(num_strs[1])

        return (num1,num2)

    except:pass



def decompress_string(s):
    s=s.rstrip('\n')  # 支持末尾多个\n的情况（如"\n\n"）
    result=[]
    try:
        for segment in s.split('/'):
            count_str,value=segment.split('-')
            count=int(count_str)
            result.extend([value]*count)

        return result
    except:
        #print(s)
        iop=1/0


def zhu_hs():
    global yan_se
    global schu
    global ming
    global asd
    global yui
    global bina_l
    global sgu_f
    global y
    global x,z,qwe,chu_yun,yuan_x,yuan_z,qi_x,qi_z,region

    try:
        chuasd()
        chus()
        while True:
            if asd[bina_l][0]=="空":
                sgu_f=0

            if sgu_f==1:
                if asd[bina_l][0]!="实":
                    y=y+1
                    dfg=decompress_string(asd[bina_l])
                    rty=0
                    try:
                        while True:
                            #yui[str((qi_x+x)-yuan_x)+"/"+str(y)+"/"+str((qi_z+z)-yuan_z)]=dfg[rty]
                            region.set_block(anvil.Block('minecraft', convert_block_id(dfg[rty])),(qi_x+x),y,(qi_z+z))
                            rty=rty+1
                            z=z+1
                            if z==16:
                                z=0
                                x=x+1

                    except Exception as e:
                        #print(e)
                        #print(x)
                        x=0
                        z=0

            if asd[bina_l][0]=="实":
                schu.write(asd[bina_l])
                sgu_f=1
                qi_x=extract_numbers(asd[bina_l])[0]
                qi_z=extract_numbers(asd[bina_l])[1]
                #print(extract_numbers(asd[bina_l]))
                y=0
            bina_l=bina_l+1
            if bina_l%10000==0:
                print(bina_l)
    except Exception as e:
        print(bina_l)
        print("aaa"+str(kuai))
        print(e)




# Create `Block` objects that are used to set blocks
stone = anvil.Block('minecraft', 'stone')

print("保存")
# Save to a file
zhu_hs()
region.save('r.'+str(extract_coordinates(ming)[0])+'.'+str(extract_coordinates(ming)[1])+'.mca')
