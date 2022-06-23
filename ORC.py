# 百度ocr提供了模板，我们直接复制就ok
# 下载通用文字识别的python sdk,一定要放在你写的代码的文件夹下面
from aip import AipOcr
from os import path


def baiduOCR(picfile, outfile):  # picfile:图片文件名 outfile:输出文件
    filename = path.basename(picfile)  # 图片名称
    # 百度提供
    """ 你的 APPID AK SK """
    APP_ID = '22995443'  # 这是你产品服务的appid
    API_KEY = 'kzztY1j5NXT5qWhPKpgwjSc0'  # 这是你产品服务的appkey
    SECRET_KEY = 'OcoKKRIlMZgsSf2FRbwPE0DbOaZbkZxN'  # 这是你产品服务的secretkey
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(picfile, 'rb')
    img = i.read()

    print("正在识别图片：\t" + filename)
    """ 调用通用文字识别（高精度版） """
    message = client.basicAccurate(img)
    print("识别成功！")
    print(message['words_result'][0]['words'])
    i.close()
    with open(outfile, 'a+') as fo:  # 这边是写进.txt文件
        fo.writelines("*" * 60 + '\n')  # 搞点花里胡哨的做区分
        fo.writelines("识别图片：\t" + filename + "\n" * 2)
        fo.writelines("文本内容：\n")
        # 输出文本内容
        for text in message.get('words_result'):  # 识别的内容
            fo.writelines(text.get('words') + '\n')
        fo.writelines('\n' * 2)
    print("文本导出成功！")
    print()


if __name__ == '__main__':
    outfile = 'D:/export1.txt'  # 保存的文件
    baiduOCR('D:/pic1.png', outfile)
    print('图片文本提取结束！文本输出结果位于 %s 文件中。' % outfile)