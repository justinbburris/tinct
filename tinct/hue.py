from beautifulhue.api import Bridge

class Hue:

    def __init__(self, user_id, bridge_ip):
        self.user_id = user_id
        self.bridge_ip = bridge_ip
        self.bridge = Bridge(device={'ip': bridge_ip}, user={'name': user_id})

    def groups(self, group='all'):
        groups = self.bridge.group.get({'which': group})
        return groups['resource']

    def group_set_on(self, group='all', on=True):
        resource = {
                'which': group,
                'data': {
                    'action': {
                        'on': on
                        }
                    }
                }
        return self.bridge.group.update(resource)

    def lights(self, light):
        light = self.bridge.light.get({'which': light})
        return light['resource']
