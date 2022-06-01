from unittest.mock import MagicMock, patch

from tests import client


class TestGithubPopularity:

    def test_valid_url_traling_slash(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "success",
                "detail": {},
            },
            "data": {},
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity/",
                headers=header,
                json={"repo_address": "https://github.com/tiangolo/fastapi"},
            )
            assert response.status_code == 200

    def test_valid_url(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "success",
                "detail": {},
            },
            "data": {},
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity",
                headers=header,
                json={"repo_address": "https://github.com/tiangolo/fastapi"},
            )
            assert response.status_code == 200

    def test_url_not_found(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "Not Found",
                "detail": {},
            },
            "data": {},
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity",
                headers=header,
                json={"repo_address": "https://github.com/tiangolofastapi"},
            )
            assert response.status_code == 404

    def test_invalid_url(self):
        override = "services.perform_request"
        mock_response = {
            "info": {
                "message": "",
                "detail": {},
            },
            "data": {},
        }
        with patch(override) as requests:
            header = {"Content-Type": "application/vnd.api+json"}
            requests.return_value = MagicMock(status_code=200, headers=header, json=lambda: mock_response)
            response = client.post(
                url="/api/v1/check_popularity",
                headers=header,
                json={"repo_address": "https://github.comtiangolofastapi"},
            )
            assert response.status_code == 400

            response = client.post(
                url="/api/v1/check_popularity",
                headers=header,
                json={"repo_address": "https:www.github.comtiangolofastapi"},
            )
            assert response.status_code == 400
