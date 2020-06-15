from flask_restful import Api
from flask_script import Manager
from flask_script import Server

from service.api import get_resources
from service.application import create_application
from service.settings import DEBUG_STATUS
from service.settings import PORTS
from service.settings import SERVICE_NAME

app = create_application()
manager = Manager(app)
api = Api(app)
get_resources(api)

if __name__ == "__main__":
    manager.add_command(
        "runserver",
        Server(
            use_debugger=DEBUG_STATUS,
            use_reloader=DEBUG_STATUS,
            port=PORTS[SERVICE_NAME],
        ),
    )
    manager.run()
