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

    # config = {
    #     'Region': 'gz',
    #     'SecretId': 'AKIDncWHFWiqpFHSkHiNUniE2BLFM93cwou',
    #     'secretKey': b'rHCAxuRIiQKsU1yQ6DSdMijRcFD8ENnv',
    #     'method': 'GET'
    # }
    # base = Base(config)
    # print(base.print_lol())
