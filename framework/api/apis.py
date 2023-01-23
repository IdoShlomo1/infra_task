from typing import Optional, List

from . import Response
from .client import ApiClient
from .models import PostModel, UserModel


class UsersApi(ApiClient):
    def get_users(self) -> Optional[List['UserModel']]:
        url = self.url + '/users'
        result = self.get(url=url)
        return [UserModel.from_dict(user) for user in result.json()]

    def get_user(self, user_id: int) -> Optional[List['UserModel']]:
        url = self.url + '/users'
        result = self.get(url=url, params={'id': user_id})
        return [UserModel.from_dict(user) for user in result.json()]


class PostApi(ApiClient):
    def get_post_by_user_id(self, user_id) -> Optional[Response]:
        url = self.url + f'/users/{user_id}/posts'
        return self.get(url)

    def add_post(self, post: PostModel) -> Optional[Response]:
        # url = self.url + ''
        # return self.get(url, params={'id': user_id})
        ...
