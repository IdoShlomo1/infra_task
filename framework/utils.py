import json
import allure
from allure import attachment_type
from framework.api import Response


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


@allure.step
def report_step(name='', data=''):
    allure.attach(data, name=name, attachment_type=attachment_type.TEXT)
