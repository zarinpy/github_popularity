from os.path import dirname, realpath
from sys import path

from fastapi.testclient import TestClient


project_root = dirname(dirname(realpath(__file__)))
path.append(project_root)

from main import app


client = TestClient(app)