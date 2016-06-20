#-*- coding:utf-8-*-

from conf.base import Base

class Cvm(Base):
        requestHost = 'cvm.api.qcloud.com'
        requestUri = '/v2/index.php'



if __name__ == '__main__':
    secretKey = b''
    secretId = ''
    name = Cvm(secretId, secretKey)
    print(name.requestHost)

