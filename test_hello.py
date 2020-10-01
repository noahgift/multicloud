from hello import speak


def test_speak():
    assert "bob" in speak("bob")
