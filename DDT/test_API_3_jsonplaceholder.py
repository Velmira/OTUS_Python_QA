import json
import random
from random import randint

import pytest

from DDT.base_request import BaseRequest

BASE_URL = 'https://dog.ceo/api/'
base_request = BaseRequest(BASE_URL)


def test_1():
    """Test #1 - LIST ALL BREEDS"""
    response = base_request.get('breeds/list/all')
    breeds = json.loads(response.text)['message']
    key_breeds = list(breeds.keys())
    assert response.ok is True
    assert json.loads(response.text)['status'] == 'success'
    return key_breeds


list_breeds = test_1()


@pytest.mark.parametrize('breed', [random.choice(list_breeds)])
def test_2(breed):
    """Test #2 - LIST ALL SUB-BREEDS FROM A BREED"""
    response = base_request.get(f'breed/{breed}/list')
    assert response.ok is True
    assert json.loads(response.text)['status'] == 'success'


@pytest.mark.parametrize('num', [randint(0, 50)])
def test_3_1(num):
    """Test #3_1 - DISPLAY MULTIPLE RANDOM IMAGES if NUM is up to 50"""
    response = base_request.get(f'breeds/image/random/{num}')
    assert len(json.loads(response.text)['message']) == num
    assert response.ok is True


@pytest.mark.parametrize('num', [51])
def test_3_2(num):
    """Test #3_2 - DISPLAY MULTIPLE RANDOM IMAGES if NUM is more than 50"""
    response = base_request.get(f'breeds/image/random/{num}')
    assert response.ok is True
    assert len(json.loads(response.text)['message']) == 50


breeds_and_sub_breeds = [('mastiff', 'bull'),
                         ('african', ''),
                         ('collie', 'border')]


@pytest.mark.parametrize("breed, breed_sub",
                         breeds_and_sub_breeds)
def test_4(breed, breed_sub):
    """Test #4 - SINGLE RANDOM IMAGE FROM A SUB BREED COLLECTION"""
    if breed_sub != '':
        response = base_request.get(f'breed/{breed}/{breed_sub}/images/random')
    else:
        response = base_request.get(f'breed/{breed}/images/random')
    assert response.ok is True
    assert json.loads(response.text)['status'] == 'success'


@pytest.mark.parametrize("breed, breed_sub",
                         breeds_and_sub_breeds)
def test_5(breed, breed_sub):
    """Test #5 - LIST ALL SUB-BREED IMAGES"""
    if breed_sub != '':
        response = base_request.get(f'breed/{breed}/{breed_sub}/images')
    else:
        response = base_request.get(f'breed/{breed}/images')
    assert response.ok is True
    assert json.loads(response.text)['status'] == 'success'
