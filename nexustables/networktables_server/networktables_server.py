import fastapi
from singleton_decorator import singleton
import uvicorn


@singleton
class NetworkTablesServer:
    def __init__(self, team_number, port=3838, ):
        self.team_number = team_number
        self.app = fastapi.FastAPI()
        self.port = port

    def start(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)
