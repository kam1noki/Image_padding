

class a():
    def load_json(self):
        file=json.load(open(r"C:\Users\KAMINOKI\Desktop\boxes.json"))
        print(file["boxes"][1]["rectangle"])
    
    def image_padding(self,type):
        file=json.load(open(r"C:\Users\KAMINOKI\Desktop\boxes.json"))
        self.left,self.top=file["boxes"][1]["rectangle"]["left_top"]  #读入左上角坐标
        self.right,self.bottom=file["boxes"][1]["rectangle"]["right_bottom"]  #读入右下角坐标
        bg_Image=Image.open(r"C:\Users\KAMINOKI\Desktop\test.png")   #读入背景图
        pad_Image=Image.open(r"C:\Users\KAMINOKI\Desktop\test2.png")    #读入嵌入图
        if(type==1):      #拉伸填充
            pad_Image=pad_Image.resize((self.right-self.left,self.bottom-self.top))
            bg_Image.paste(pad_Image,(self.left,self.top),mask=None)
            bg_Image.save(r"C:\Users\KAMINOKI\Desktop\result.jpg")
            print("保存完毕")
        if(type==2):
            pad_w,pad_h=pad_Image.size
            if((pad_w<self.right-self.left)&(pad_h<self.bottom-self.top)):  #判断嵌入图是否小于box
                rate=min((self.right-self.left)/pad_w,(self.bottom-self.top)/pad_h)  #计算宽高中最接近box规格的一项的扩大率
                pad_w=int(rate*pad_w)
                pad_h=int(rate*pad_h)
                pad_Image=pad_Image.resize((pad_w,pad_h))
                bg_Image.paste(pad_Image,(self.left,self.top),mask=None)
            else:
                rate=min((self.right-self.left)/pad_w,(self.bottom-self.top)/pad_h)   #计算宽高中比box大且距离box规格最远的的一项的扩大率
                pad_w=int(rate*pad_w)
                pad_h=int(rate*pad_h)
                pad_Image=pad_Image.resize((pad_w,pad_h))
                bg_Image.paste(pad_Image,(self.left,self.top),mask=None)
            bg_Image.save(r"C:\Users\KAMINOKI\Desktop\result.jpg")
            print("保存完毕")

if __name__=="__main__":
    import json
    from PIL import Image
    a().load_json()
    type=input("请选择填充方式：1、拉伸填充  2、保持原比例 \n")
    a().image_padding(int(type))
    