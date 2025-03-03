# coding=utf-8
import os, time
from obs import Convertor

def main():
    try:
        xxd = Convertor()
        xxd.toDesktop()
        xxd.toDocx()
        xxd.toBib()
        xxd.toHTML()
        iframes = xxd.fetch_iframes(xxd.content)
        if len(iframes)>0:
            html = xxd.ex_html
            while not os.path.exists(html):
                # 阻塞一下，pandoc转换格式需要时间
                time.sleep(1)
            with open(html, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            idx = 0
            content = []
            for line in lines:
                if line.startswith('<iframe'):
                    line = iframes[idx]
                    idx += 1
                content.append(line)
            content = '\n'.join(content)
            with open(html, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(str(e)) 

def test():
    fp = r"X:\projects\working\05-Life\01-Album\私房菜\菜少只能各种拌面.md"
    try:
        xxd = Convertor()
        xxd.md = fp
        xxd.toDesktop()
        xxd.toDocx()
        xxd.toBib()
        xxd.toHTML()
    except Exception as e:
        print(str(e)) 

if __name__=='__main__':
    main() 
    # test()  
    # 2022-03-22 19:47:06 complete

