from flask_restful import reqparse
from flask_restful import Resource


class PostResource(Resource):
    def __init__(self, typing):
        self.reqparse = reqparse.RequestParser()
        for parameter in typing:
            action = parameter.get("action", "store")
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action=action,
            )
        super(PostResource, self).__init__()
