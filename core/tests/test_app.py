import pytest
from core import app as flask_app


@pytest.fixture
def app():
    return flask_app


def test_dashboard_hello(app):
    print(app)
    client = app.test_client()
    response = client.get('/dashboard/api/hello')
    assert response.status_code == 200
    assert response.get_json() == {"msg": "Hello Dashboard!"}


