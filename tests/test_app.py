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


def test_login(client):
    response = client.post(
        "/login", json={"username": "test_username", "password": "test_password"}
    )
    assert response.status == "200 OK"


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


def test_get_scores_route(client):
    response = client.get("/scores")
    assert response.status == "200 OK"
    for item in response.json:
        assert "score_id", "value" in item.keys()


def test_post_scores_route(client):
    response = client.get("/users")
    test_id = response.json[-1]["user_id"]
    response = client.post("/scores", json={"value": "3000", "user_id": test_id})
    assert response.status == "201 CREATED"


def test_scores_id_route(client):
    response = client.get("/users")
    test_id = response.json[-1]["user_id"]
    response = client.get(f"/scores/{test_id}")
    assert response.status == "200 OK"
    for item in response.json:
        assert item["user_id"] == test_id
        assert "score_id", "value" in item.keys()


def test_stats_route(client):
    response = client.get("/users")
    test_id = response.json[-1]["user_id"]
    response = client.post(
        "/stats",
        json={
            "hours_played": 1,
            "metres_gained": 1,
            "enemies_defeated": 1,
            "damage_given": 1,
            "damage_recieved": 1,
            "user_id": test_id,
        },
    )
    stat_id = response.json["stat_id"]
    assert response.status == "201 CREATED"
    assert response.json == {
        "stat_id": stat_id,
        "hours_played": 1,
        "metres_gained": 1,
        "enemies_defeated": 1,
        "damage_given": 1,
        "damage_recieved": 1,
        "user_id": test_id,
    }
    response = client.post(
        "/stats",
        json={
            "hours_played": 1,
            "metres_gained": 1,
            "enemies_defeated": 1,
            "damage_given": 1,
            "damage_recieved": 1,
            "user_id": test_id,
        },
    )
    assert response.status == "201 CREATED"
    assert response.json == {
        "stat_id": stat_id,
        "hours_played": 2,
        "metres_gained": 2,
        "enemies_defeated": 2,
        "damage_given": 2,
        "damage_recieved": 2,
        "user_id": test_id,
    }


def test_scores_id_route(client):
    response = client.get("/users")
    test_id = response.json[-1]["user_id"]
    print(test_id)
    response = client.get(f"/stats/2")
    print(response)


def test_logout(client):
    response = client.post(
        "/login", json={"username": "new_test_username", "password": "test_password"}
    )
    token = response.json["token"]
    response = client.delete(
        "/logout",
        headers={"token": token},
        json={"test_data": "test_data"},
    )  # n.b test_data added as json as werkzeug does not currently support setting the content type for delete requests: https://stackoverflow.com/questions/24073488/flask-test-client-testing-delete-request-with-data
    assert response.status == "202 ACCEPTED"


# def test_delete_user(client):
#     response = client.get("/users")
#     test_id = response.json[-1]["user_id"]
#     response = client.delete(
#         f"/users/{test_id}", json={"test_data": "test_data"}
#     )  # see line 64 comment
#     assert response.status == "200 OK"
