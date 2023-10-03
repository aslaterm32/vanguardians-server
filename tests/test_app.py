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


def test_register(client):
    response = client.post(
        "/register", json={"username": "test_username", "password": "test_password"}
    )
    assert response.status == "201 CREATED"


def test_users(client):
    response = client.get("/users")
    assert response.status == "200 OK"
    assert "username", "password" in response.json[0].keys()
    assert response.json[-1]["username"] == "test_username"
    test_id = response.json[-1]["user_id"]


def test_patch_user(client):
    response = client.get("/users")
    test_id = response.json[-1]["user_id"]
    response = client.patch(f"/users/{test_id}", json={"username": "new_test_username"})
    assert response.status == "200 OK"
