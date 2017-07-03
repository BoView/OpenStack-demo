from pecan import rest
from wsme import types as wtypes

from openstack_demo.api import expose

class V1Controller(rest.RestController):

    @expose.expose(wtypes.text)
    def get(self):
        return 'This is v1controller'