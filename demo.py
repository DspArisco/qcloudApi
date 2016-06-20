#-*- coding:utf-8-*-

from api import QcloudApi

if __name__ == '__main__':
    module = 'cvm'
    secretKey = b''
    secretId = ''
    params = {
        'Action': 'DescribeInstances',
        'instanceIds.0': 'ins-gdhkajhc',
    }

    service = QcloudApi(module, params)
    print(service.call(secretId, secretKey))
