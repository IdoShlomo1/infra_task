import json
from typing import Any, List
from dataclasses import dataclass


@dataclass
class ObjectDict:
    @staticmethod
    def from_dict(obj: dict) -> Any:
        ...

    @property
    def dict(self) -> dict:
        return json.loads(json.dumps(self, default=lambda x: x.__dict__))


# ------------------------------- User -------------------------------


@dataclass
class Geo(ObjectDict):
    lat: str
    lng: str

    @staticmethod
    def from_dict(obj: Any) -> 'Geo':
        return Geo(**obj)


@dataclass
class Address(ObjectDict):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

    @staticmethod
    def from_dict(obj: dict) -> 'Address':
        obj['geo'] = Geo.from_dict(obj.get("geo"))
        return Address(**obj)


@dataclass
class Company(ObjectDict):
    name: str
    catchPhrase: str
    bs: str

    @staticmethod
    def from_dict(obj: Any) -> 'Company':
        return Company(**obj)


@dataclass
class UserModel(ObjectDict):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    @staticmethod
    def from_dict(obj: dict) -> 'UserModel':
        obj['address'] = Address.from_dict(obj.get("address"))
        obj['company'] = Company.from_dict(obj.get("company"))
        return UserModel(**obj)


UserList = List[UserModel]
# ------------------------------- Post -------------------------------


@dataclass
class PostModel(ObjectDict):
    userId: int
    id: int
    title: str
    body: str

    @staticmethod
    def from_dict(obj: dict) -> 'PostModel':
        return PostModel(**obj)


# PostList = List[PostModel]
