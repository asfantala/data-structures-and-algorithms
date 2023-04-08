from array_insert_shift import insertShiftArray

def test_array_insert_shift():
    actual = insertShiftArray([2,4,6,-8], 16)
    expected = [2,4,16,6,-8]
    assert actual == expected


def test_array_insert_shift1():
    actual = insertShiftArray([2,4,-8], 16)
    expected = [2,4,16,-8]
    assert actual == expected

def test_array_insert_shift3():
    actual = insertShiftArray([-8], 16)
    expected = [-8,16]
    assert actual == expected

def test_array_insert_shift4():
    actual = insertShiftArray([],16)
    expected = [16]
    assert actual == expected    
