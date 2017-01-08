#coding:utf-8
from urllib import request


class Html_downloader(object):


    def download(self,url):
        if url is None:
            return None
        responce = request.urlopen(url)

        if responce.status != 200:
            return None
        return responce.read()


