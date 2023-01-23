from typing import Optional, Any

from .client import ApiClient
from .models import PostModel, UserModel

from dataclasses import dataclass


@dataclass
class ApiResponse:
    stats_code: int
    obj: Any


class UsersApi(ApiClient):
    def get_users(self) -> Optional[ApiResponse]:
        url = self.url + '/users'
        result = self.get(url=url)
        users = [UserModel.from_dict(user) for user in result.json()]
        return ApiResponse(result.status_code, users)

    def get_user(self, user_id: int) -> Optional[ApiResponse]:
        url = self.url + '/users'
        result = self.get(url=url, params={'id': user_id})
        users = [UserModel.from_dict(user) for user in result.json()]
        return ApiResponse(result.status_code, users)


class PostApi(ApiClient):
    def get_post_by_user_id(self, user_id) -> Optional[ApiResponse]:
        url = self.url + f'/users/{user_id}/posts'
        result = self.get(url)
        return ApiResponse(result.status_code, [PostModel.from_dict(post) for post in result.json()])

    def add_post(self, user_id, post: PostModel) -> Optional[ApiResponse]:
        url = self.url + f'/users/{user_id}/posts'
        results = self.post(url, json=post.dict)
        return ApiResponse(results.status_code, PostModel.from_dict(results.json()))


class RestClient:
    def __init__(self, session, url):
        self.post = PostApi(session, url)
        self.user = UsersApi(session, url)
