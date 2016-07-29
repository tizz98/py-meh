import requests

from . import exceptions
from . import constants


def _make_request(endpoint, api_version=constants.API_VERSION, **params):
    from . import api_key

    if api_key is None:
        raise exceptions.NotConfigured(
            "An api key is required to make requests. Get one at: "
            "https://meh.com/developers-developers-developers"
        )

    request_url = "{base_url}/{api_version}/{endpoint}".format(
        base_url=constants.BASE_URL,
        api_version=api_version,
        endpoint=endpoint,
    )

    params.update({
        'apikey': api_key,
    })

    response = requests.get(request_url, params=params)

    if response.status_code == 200:
        try:
            json_data = response.json()
        except ValueError as e:
            raise exceptions.InvalidJson(
                "Error decoding JSON from response (%r) - (%s)" % (response, e)
            )

        return json_data
    elif response.status_code == 401:
        raise exceptions.ApiResponseError("Invalid api key")
    else:
        raise exceptions.ApiResponseError(
            "Expected 200 response from server, got %s" % response.status_code
        )


def get_current():
    return _make_request(constants.CURRENT_ENDPOINT)
