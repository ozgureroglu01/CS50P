from seasons import validate_date

def test_validate_date():
    assert validate_date("2001-06-23") == True
    assert validate_date("June 23, 2001") == False
