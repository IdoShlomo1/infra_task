from typing import Callable, Optional, List, Dict
from framework.api import Session, Response
from loguru import logger

from json.decoder import JSONDecodeError


def log_request(response, *args, **kwargs):
    _data = ''
    try:
        _data = response.json()
    except JSONDecodeError as e:
        logger.exception(e)

    logger.info(f'Api Request: method={response.request.method}, args={args}, kwargs={kwargs}, response={_data}')


class ApiClient:
    def __init__(self, session: Session, url: str, hooks: Optional[List[Callable]] = None,
                 headers: Optional[Dict] = None):
        self.url = url
        self.session = session
        self.session.hooks['response'] = [log_request]

        if hooks:
            self.session.hooks['response'].extend(hooks)
        if headers:
            self.session.headers.update(headers)

    def _call(self, method, *args, **kwargs) -> Response:
        """
        :param method:
        :param args:
        :param kwargs:
        :return: Response
        """
        response = self.session.request(method, *args, **kwargs)
        response.raise_for_status()
        return response

    def get(self, *args, **kwargs):
        return self._call('GET', *args, **kwargs)

    def post(self, *args, **kwargs) -> Response:
        return self._call('POST', *args, **kwargs)

    def put(self, *args, **kwargs) -> Response:
        return self._call('PUT', *args, **kwargs)

    def delete(self, *args, **kwargs) -> Response:
        return self._call('DELETE', *args, **kwargs)

    def patch(self, *args, **kwargs) -> Response:
        return self._call('PATCH', *args, **kwargs)

