import urllib.request
import json

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def save_anm(filename,html):
    with open(filename,'wb') as file:
        file.write(html)


def Start_download():
    JsonDir = 'E:\CatchAnm\mycatch.json'
    file = open(JsonDir,'r')
    res = file.read()
    dic =json.loads(res)

    for i in range(len(dic)):
        url = dic[i]['anm_url']
        num = len(url)
        for j in range(num):
            html = open_url(url[j])
            filename = url[j].split("/")[-1]
            trueUrl = 'http://imgsrc.baidu.com/forum/pic/item/'+filename
            trueHtml = open_url(trueUrl)
            print('开始下载文件:'+filename)
            savename = 'E:\\CatchAnm\downloads\\'+filename
            save_anm(savename,trueHtml)

    print('下载主程序运行完毕')

if __name__ == '__main__':
    Start_download()

        
