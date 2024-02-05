import json
from random import randint
import pytest

from DDT.base_request import BaseRequest

BASE_URL = 'https://jsonplaceholder.typicode.com'
base_request = BaseRequest(BASE_URL)


@pytest.mark.parametrize('num', [randint(0, 100)])
def test_1_1(num):
    """Test #1_1 - Getting a resource - number is up to 100"""
    test_1_1 = base_request.get(f'posts/{num}')
    assert test_1_1.ok is True
    assert json.loads(test_1_1.text)['id'] == num


@pytest.mark.parametrize('num', [101])
def test_1_2(num):
    """Test #1_2 - Getting a resource - number is more than 100"""
    test_1_2 = base_request.get(f'posts/{num}')
    assert test_1_2.status_code == 404
    assert json.loads(test_1_2.text) == {}


def test_2():
    """Test #2 - Listing all resources - comments"""
    test_2 = base_request.get("comments")
    list_comments = json.loads(test_2.text)
    assert test_2.ok is True
    assert len(list_comments) == 500


headers = {"Content-Type": "application/json; charset=utf-8"}


def test_3():
    """Test #3 - Creating a resource"""
    test_3 = base_request.post("posts", {
        "title": "foo", "body": "bar", "userId": 1})
    assert test_3["userId"] == "1"
    assert test_3["title"] == "foo"
    assert test_3["body"] == "bar"
    assert test_3["id"] == 101


@pytest.mark.parametrize('id', [(1), (10), (30)])
def test_4(id):
    """Test #4 - Updating a resource"""
    test_4 = base_request.put(f'/posts/{id}', {
        "title": "foo", "body": "bar", "userId": f'{id}'})
    assert test_4["userId"] == f'{id}'
    assert test_4["title"] == "foo"
    assert test_4["body"] == "bar"


@pytest.mark.parametrize('id', [(1), (10), (30)])
def test_5(id):
    """Test #4 - Deleting a resource"""
    test_4 = base_request.delete(f'/posts/{id}')
    assert test_4.ok is True
    assert test_4.text == '{}'
