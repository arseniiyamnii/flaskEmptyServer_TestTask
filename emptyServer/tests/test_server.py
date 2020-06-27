#!/usr/bin/python3
import sys
sys.path.append('..')
import server
import pytest
app=server.create_app()
def test_index():
    response=app.test_client().get('/?invalid=1')
    assert response.status_code == 200

