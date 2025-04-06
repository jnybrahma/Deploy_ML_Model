from my_module import square

    
def test_square_return_value_type_int():
    # when
    subject = square(2)

    # Then
    assert isinstance(subject, int)