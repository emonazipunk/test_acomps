import json.decoder

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"В ответе нет куки с именем {cookie_name}"
        return response.cookies[cookie_name]

    def get_headers(self, response: Response, header_name):
        assert header_name in response.headers, f"В ответе не заголовка с именем {header_name}"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except:
            json.decoder.JSONDecodeError
            assert False, f"В ответе пришёл не JSON, а текст '{response.text}'"
        assert name in response_as_dict, f"В ответе нет ключа {name}"
        return response_as_dict[name]
