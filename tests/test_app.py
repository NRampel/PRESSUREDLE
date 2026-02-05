import pytest
from app import create_app 

@pytest.fixture
def client():
    create_app.config['TESTING'] = True
    create_app.config['SECRET_KEY'] = 'test_key' 

    with create_app.test_client() as client:
        with create_app.app_context():
            yield client

def test_game_route_logic(client):
    setup = client.post('/set_difficulty', data={'difficulty': 'medium'}, follow_redirects=True)
    assert setup.status_code == 200
    response = client.post('/game_loop', data={'monster_guess': 'Pandemonium'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Pandemonium" in response.data