import json
from requests import Response


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"В ответе пришёл не JSON, а текст '{response.text}'"

        assert name in response_as_dict, f"В ответе нет ключа'{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_key_is_exist(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"В ответе пришёл не JSON, а текст '{response.text}'"
        assert name in response_as_dict, f"В ответе нет ключа'{name}'"

    @staticmethod
    def assert_json_keys_is_exist(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"В ответе пришёл не JSON, а текст '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"В ответе нет ключа'{name}'"

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"В ответе пришёл не JSON, а текст '{response.text}'"
        for name in names:
            assert name not in response_as_dict, f"В ответе не должно быть'{name}'"

    @staticmethod
    def assert_status_code(response: Response, expected_code):
        assert response.status_code == expected_code, \
            f"Неожиданный код ответа: ожидался {expected_code}, a пришёл {response.status_code}"

    @staticmethod
    def assert_exact_json(expected_dict, actual_json):
        expected_json = json.dumps(expected_dict, sort_keys=True)

        try:
            assert expected_json == actual_json
        except AssertionError:
            raise AssertionError(f"Ожидалось: {expected_json}\nПолучено: {actual_json}")
