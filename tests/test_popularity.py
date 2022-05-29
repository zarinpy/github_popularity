from tests import client
from unittest.mock import patch, MagicMock


class TestGithubPopularity:

    def test_valid_url_traling_slash(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "success",
                "detail": {},
            },
            "data": {}
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity/",
                headers=header,
                json={"repo_address": "https://github.com/tiangolo/fastapi"}
            )
            assert response.status_code == 200

    def test_valid_url(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "success",
                "detail": {},
            },
            "data": {}
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity",
                headers=header,
                json={"repo_address": "https://github.com/tiangolo/fastapi"}
            )
            assert response.status_code == 200
