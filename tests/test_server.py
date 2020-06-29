#!/usr/bin/python3
'''unit testing some functions'''
from ..empty_server import server


APP = server.create_app()


def test_index():
    '''testing index route'''
    response = APP.test_client().get('/?invalid=1')
    assert response.status_code == 200
    response_post = APP.test_client().post('/')
    assert response_post.status_code == 200


def test_api():
    '''testing api route'''
    response = APP.test_client().get('/api?invalid=1')
    assert response.status_code == 200


def test_fallback():
    '''testing others routes'''
    response = APP.test_client().get('/randomly?invalid=1')
    assert response.status_code == 200
