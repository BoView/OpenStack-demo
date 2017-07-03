from pecan import rest
from wsme import types as wtypes
# import wsmeext.pecan as wsme_pecan
#add api/expose.py and import
from openstack_demo.api import expose
from openstack_demo.api.controllers.v1 import controller as v1_controller

class RootController(rest.RestController):
    v1 = v1_controller.V1Controller()
    # @wsme_pecan.wsexpose(wtypes.text)
    @expose.expose(wtypes.text)
    def get(self):
        return "Hello,SunLinBo!!!"