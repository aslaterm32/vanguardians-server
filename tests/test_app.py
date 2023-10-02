def test_home(client):
    response = client.get("/")
    assert response.status == "200 OK"
    assert response.json[0] == {
        "message": "Welcome",
        "description": "Vanguardians API",
        "endpoints": [
            "GET /",
            "GET /users",
            "POST /users" "GET /guardians",
            "GET /guardians/:id",
        ],
    }


def test_users(client):
    response = client.get("/users")
    response_length = len(response.json)
    assert response.status == "200 OK"
    assert "username", "password" in response.json[0].keys()


def test_register(client):
    response = client.post(
        "/register", data={"username": "test_username", "password": "test_password"}
    )
    print(response)
