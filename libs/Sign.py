#-*- coding:utf-8-*-

import hashlib
import hmac
import random
import binascii
import time

# timestamp = subprocess.Popen('date +%s', shell=True, stdout=subprocess.PIPE)


class Sign:

    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey
    def make(self,requestHost, requestUri, params, method= 'GET'):
        list = {}
        for param_key in params:
            if method == 'post' and str(params[param_key])[0:1] == "@":
                continue
            list[param_key] = params[param_key]
        srcStr = method.upper() + requestHost + requestUri + '?' + '&'.join(k.replace("_", ".") + "=" + str(list[k]) for k in sorted(list.keys()))

        srcStr = str.encode(srcStr)
        hashed = hmac.new(self.secretKey, srcStr, hashlib.sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]




def main():

    secretKey = b''
    secretId = ''
    Nonce = ''.join(map(str, [random.randint(0, 9) for _ in range(6)]))
    url = 'cvm.api.qcloud.com'
    common = {
        'Action': 'DescribeInstances',
        'Nonce': Nonce,
        'Region': 'gz',
        'SecretId': secretId,
        'Timestamp': int(time.time()),
        'instanceIds.0': 'ins-gdhkajhc',
        'limit': 20,
        'offset': 0,
    }
    sign = Sign(secretId, secretKey)
    Signure = sign.make(url, '/v2/index.php', common).decode()
    print(Signure)

if __name__=='__main__':
    main()




