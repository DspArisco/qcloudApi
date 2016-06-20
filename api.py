#-*- coding:utf-8-*-


class QcloudApi:
    def __init__(self, module, params):
        self.module = module
        self.params = params
    def _factory(self, secretId, secretKey):
        if (self.module == 'cvm'):
            from conf.cvm import Cvm
            service = Cvm(secretId, secretKey)
            service.check_config()

        else:
            print("Error, no module")
        return service

    def call(self, secretId, secretKey):
        service = self._factory(secretId, secretKey)
        return service.send(service.requestHost, service.requestUri, self.params)



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
    # service.factory(secretId, secretKey)

    # service.factory(secretId, secretKey)





