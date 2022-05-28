import httpx


async def perform_request(url, headers=None, data=None, method=None, **kwargs):
    try:
        if method.lower() == "post":
            async with httpx.AsyncClient() as client:
                return await client.post(
                    url=url,
                    headers=headers,
                    json=data,
                    auth=None,
                    **kwargs,
                )
        elif method.lower() == "delete":
            async with httpx.AsyncClient() as client:
                return await client.delete(
                    url=url,
                    headers=headers,
                    **kwargs,
                )
        elif method.lower() == "get":
            async with httpx.AsyncClient() as client:
                return await client.get(
                    url=url,
                    headers=headers,
                    **kwargs,
                )
    except Exception as ex:
        print(ex)
        return {"code": 500, "message": str(ex)}
