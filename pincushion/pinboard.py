import datetime
import requests

from pincushion import settings, utils


def pb_post(
    url,
    title,
    description="",
    tags=[],
    timestamp=datetime.datetime.utcnow(),
    replace=True,
    shared=True,
    toread=False,
):

    api_token = getattr(settings, 'PINBOARD_API_TOKEN', '')
    username = getattr(settings, 'PINBOARD_USERNAME', '')
    auth_string = f"{username}:{api_token}"

    valid_title = title[:255]
    valid_description = description[:255]
    valid_tags = [tag[:255] for tag in tags]

    payload = {
        'auth_token': auth_string,
        'format': 'json',
        'url': url,
        'description': valid_title,
        'extended': valid_description,
        'tags': ','.join(valid_tags),
        'dt': utils.pb_date_format(timestamp),
        'replace': utils.bool_to_yesno(replace, True),
        'shared': utils.bool_to_yesno(shared, True),
        'toread': utils.bool_to_yesno(toread, False),
    }

    api_url = 'https://api.pinboard.in/v1/posts/add'

    response = requests.get(api_url, params=payload)
    if response.status_code == 200:
        try:
            response_json = response.json()
        except Exception:
            raise Exception(f"Pinboard API returned non-json: {response.text}")
        if response_json.get('result_code', None) == 'done':
            return True
        else:
            raise Exception(f"Pinboard API returned error json: {response_json}")
    raise Exception(f"Pinboard API Error: {response.status_code} - {response.text}")
