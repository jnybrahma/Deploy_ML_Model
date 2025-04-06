from my_module import square

# Note file name prefix as test_xxx
    
def test_square_return_value_type_int():
    # when
    subject = square(2)

    # Then
    assert isinstance(subject, int)