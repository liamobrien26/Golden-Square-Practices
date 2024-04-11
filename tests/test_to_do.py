from lib.to_do import added_to_list

def test_added_to_list():
    assert added_to_list(["#TODO clean room", "Apple"]) == ["#TODO clean room"]