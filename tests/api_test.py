import random
from framework import PostFactory
from framework.utils import AllureManager


@AllureManager.allure_step
def report_mail(email):
    pass


def test_add_post_to_random_user(api_client):
    user_id = random.randint(1, 10)
    user_response = api_client.user.get_user(user_id)
    with AllureManager.allure_step(f"Get user by id={user_id}"):
        report_mail(user_response.obj[0].email)
        # print("user_response", user_response.obj[0])
    with AllureManager.allure_step(f"Get all user posts"):
        posts = api_client.post.get_post_by_user_id(user_id).obj
        for post in posts:
            assert 0 < post.id <= 100, "Post Id is not between 1 and 100"
        AllureManager.attach_as_json(name='Posts', obj=posts)

    with AllureManager.allure_step(f"Add new post"):
        new_post = PostFactory(userId=user_id)
        add_post_response = api_client.post.add_post(user_id, new_post)
        assert add_post_response.obj.title == new_post.title
        assert add_post_response.obj.body == new_post.body
        assert add_post_response.stats_code == 200, f"Expecting status code <200> got <{add_post_response.stats_code}>"
