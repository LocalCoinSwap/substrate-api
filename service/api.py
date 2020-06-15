from flask_restful import Resource

from .logger import Logger

# use 'Api:class_name' as extra.namespace tag
log = Logger("Api", True, True, False)
log.info("Loading API....")


class HeartBeat(Resource):
    """
    Are we alive?
    """

    def get(self):
        return True


def get_resources(api):
    api.add_resource(HeartBeat, "/HeartBeat")
