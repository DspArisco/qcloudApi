# -*- coding:utf-8 -*-

from urllib.parse import urlencode
import requests

from libs.Sign import Sign
class Requests:

    def __init__(self, secretId, secretKey, params):
        self.secretId = secretId
        self.secretKey = secretKey
        import time
        import random
        Nonce = ''.join(map(str, [random.randint(0, 9) for _ in range(6)]))
        conf = {
            'Nonce': int(Nonce),
            'SecretId': secretId,
            'Region': 'gz',
            'Timestamp': int(time.time()),
            'limit': 20,
            'offset': 0
        }
        self.params = params.copy()
        self.params.update(conf)

    def generateUrl(self, method= 'GET'):
        sign = Sign(self.secretId, self.secretKey)
        self.params['Signature'] = sign.make(requestHost, requestUrl, self.params, method).decode()
        self.params = urlencode(self.params)
        url = "https://%s%s" % (requestHost, requestUrl)
        if method.upper() == 'GET':
            url += '?' + self.params
        return url

    def send(self, requestHost, requestUrl, method='GET'):
        sign = Sign(self.secretId, self.secretKey)
        self.params['Signature'] = sign.make(requestHost, requestUrl, self.params, method).decode()
        # print(params)
        # self.params=urlencode(self.params)
        url = 'https://%s%s' % (requestHost, requestUrl)
        s =requests.Session()
        # url += '?' + self.params
        r = s.get(url, params=self.params)

        return r.text




# def main():



if __name__=='__main__':
    # main()
    secretKey = b''
    secretId = ''
    requestHost = 'cvm.api.qcloud.com'
    requestUrl = '/v2/index.php'
    params = {
        'Action': 'DescribeInstances',
        'instanceIds.0': 'ins-gdhkajhc',
    }
    service = Requests(secretId, secretKey, params)
    # service.config['name'] = "Hello"
    print(service.send(requestHost, requestUrl))

    # print

    # method = 'GET'
    # Nonce = ''.join(map(str, [random.randint(0, 9) for _ in range(6)]))
    # requestHost = 'cvm.api.qcloud.com'
    # requestUrl = '/v2/index.php'
    # params = {
    #     'Action': 'DescribeInstances',
    #     'Nonce': int(Nonce),
    #     'Region': 'gz',
    #     'SecretId': secretId,
    #     'Timestamp': int(time.time()),
    #     'instanceIds.0': 'ins-gdhkajhc',
    # }
    #
    # service = Requests(secretId, secretKey)
    # name = service.send(requestHost, requestUrl, params, method)
    # print(name)



