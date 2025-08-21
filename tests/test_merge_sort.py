from src.merge_sort import merge_sort

def test_merge_sort():
    arr = [5, 2, 9, 1, 5, 6]
    merge_sort(arr)
    assert arr == [1, 2, 5, 5, 6, 9]