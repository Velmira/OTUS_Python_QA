import json
import random
import pytest
from DDT.base_request import BaseRequest

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'
base_request = BaseRequest(BASE_URL)


def test_1():
    """Test #1 - LIST BREWERIES"""
    test1 = base_request.get('')
    assert test1.ok is True


def test_2():
    """Test #2 - Random Brewery"""
    test1 = base_request.get("random")
    assert test1.ok is True


type = [("micro"), ("nano"),
        ("regional"), ("brewpub"),
        ("large"), ("planning"),
        ("bar"), ("contract"),
        ("proprietor"), ("closed")]


@pytest.mark.parametrize("type",
                         type)
def test_3(type):
    """Test #3 - BY TYPE"""
    test_3 = base_request.get(f"?by_type={type}")
    assert test_3.ok is True


@pytest.mark.parametrize("size",
                         [random.randint(0, 50)])
def test_4_1(size):
    """Test #4_1 - BY SIZE - UP TO 50"""
    test_4_1 = base_request.get(f"random?size={size}")
    list = json.loads(test_4_1.text)

    list_id = []
    for i in list:
        list_result = {
            key: value
            for key, value in i.items()
            if key in "id"
        }
        list_id.append(list_result)

    assert len(list) == size
    assert test_4_1.ok is True


@pytest.mark.parametrize("size",
                         [51])
def test_4_2(size):
    """Test #4_2 - BY SIZE - MORE THAN 50"""
    test_4_2 = base_request.get(f"random?size={size}")
    list = json.loads(test_4_2.text)

    list_id = []
    for i in list:
        list_result = {
            key: value
            for key, value in i.items()
            if key in "id"
        }
        list_id.append(list_result)

    assert len(list) == 50
    assert test_4_2.ok is True


type = [('micro'), ('nano'), ('regional'),
        ('brewpub'), ('large'), ('planning'),
        ('bar'), ('contract'), ('proprietor'),
        ('closed')]


@pytest.mark.parametrize("type",
                         type)
def test_5(type):
    """Test #5 - BY TYPE"""
    test_5 = base_request.get(f"?by_type={type}")
    list = json.loads(test_5.text)
    for i in range(len(list)):
        assert list[i].get('brewery_type') == type
        assert test_5.ok is True
