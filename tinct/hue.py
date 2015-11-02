from beautifulhue.api import Bridge

class Hue:

    def __init__(self, user_id, bridge_ip):
        self.user_id = user_id
        self.bridge_ip = bridge_ip
        self.bridge = Bridge(device={'ip': bridge_ip}, user={'name': user_id})

    def groups(self):
        return self.bridge.group.get({'which': 'all'})
