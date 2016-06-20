#-*- coding:utf-8-*-
import sys
import os
sys.path.append(os.path.split(os.path.realpath(__file__))[0] + os.sep + '..')

from libs.request import Requests

class Base:
    def __init__(self, SecretId, secretKey):
        self.SecretId = SecretId
        self.secretKey = secretKey

    def check_config(self):
        if isinstance(self.secretKey, bytes) is False:
            print("please input secretKey bytes type")
            exit()


    def send(self, requestHost, requestUrl, params):
        r = Requests(self.SecretId, self.secretKey, params)
        return r.send(requestHost, requestUrl)




if __name__ == '__main__':
    secretKey = b''
    secretId = ''
    requestHost = 'cvm.api.qcloud.com'
    requestUrl = '/v2/index.php'
    params = {
        'Action': 'DescribeInstances',
        'instanceIds.0': 'ins-gdhkajhc',
    }
    service = Base(secretId, secretKey)
    print(service.send(requestHost, requestUrl, params))
    # service.config['name'] = "Hello"
    # print(service.send(requestHost, requestUrl))


