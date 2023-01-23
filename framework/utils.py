import json
import allure
from allure import attachment_type
from framework.api import Response
from typing import Any


def json_reader(file_path) -> Any:
    with open(file_path) as f:
        return json.load(f)


class AllureManager:
    allure_step = allure.step

    @staticmethod
    def attach_as_json(name='', obj=None):
        allure.attach(name=name, body=json.dumps(obj, default=lambda p: p.__dict__, indent=4),
                      attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def report_response(response, *args, **kwargs):
        with allure.step("Api Call"):
            if isinstance(response, Response):
                allure.attach(
                    f"{response.request.method}",
                    name="response.request.method",
                    attachment_type=attachment_type.TEXT
                )
                allure.attach(
                    f"{response.request.url}",
                    name="response.request.url",
                    attachment_type=attachment_type.TEXT
                )
                allure.attach(
                    f'{response.status_code}',
                    name="response.status_code",
                    attachment_type=attachment_type.TEXT
                )
                allure.attach(
                    json.dumps(response.json(), indent=4),
                    name="response.json",
                    attachment_type=attachment_type.JSON
                )
                allure.attach(
                    json.dumps(response.json(), indent=4),
                    name="response.json",
                    attachment_type=attachment_type.JSON
                )
                try:
                    allure.attach(
                        json.dumps(json.loads(response.request.body), indent=4),
                        name="response.request.body",
                        attachment_type=attachment_type.JSON
                    )
                except TypeError:
                    pass

