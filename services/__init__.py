import httpx


async def perform_request(url, headers=None, data=None, method=None, **kwargs):

    def handle_response(response):
        if response.status_code != 500:
            return response.json(), response.status_code
        else:
            return None, 500

    try:
        if method.lower() == "post":
            async with httpx.AsyncClient() as client:
                result = await client.post(
                    url=url,
                    headers=headers,
                    json=data,
                    auth=None,
                    **kwargs,
                )
                return handle_response(result)
        elif method.lower() == "delete":
            async with httpx.AsyncClient() as client:
                result = await client.delete(
                    url=url,
                    headers=headers,
                    **kwargs,
                )
            return handle_response(result)
        elif method.lower() == "get":
            async with httpx.AsyncClient() as client:
                result = await client.get(
                    url=url,
                    headers=headers,
                    **kwargs,
                )
            return handle_response(result)
    except Exception as ex:
        return str(ex), 500
