from closed_range.closed_range import ClosedRange


def test_range_to_str():
    # arrange
    # 閉区間の数字の定義
    lower_endpoint = 3
    upper_endpoint = 8
    # 期待される答えの定義
    expected = "[3, 8]"
    # 閉区間クラスのインスタンス化
    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    # act
    # メソッドの実行
    actual = closed_range.__repr__()
    # assert
    # チェック
    assert actual == expected


def test_is_proper_range():
    # arrange
    # 正しい上端と下端を定義 [3, 8]
    lower_endpoint = 3
    upper_endpoint = 8
    expected_status = True
    # act
    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    actual_status = closed_range.is_proper_range()
    # assert
    assert actual_status == expected_status


def test_is_not_proper_range_for_invalid_lower():
    lower_endpoint = 9
    upper_endpoint = 8
    expected_status = False

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    actual_status = closed_range.is_proper_range()

    assert actual_status == expected_status


def test_is_not_proper_range_for_same_endpoint():
    lower_endpoint = 8
    upper_endpoint = 8
    expected_status = False

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    actual_status = closed_range.is_proper_range()

    assert actual_status == expected_status


def test_given_value_is_included():
    # given value を定義
    given_value = 5
    lower_endpoint = 3
    upper_endpoint = 8

    # インスタンス作成
    closed_range = ClosedRange(lower_endpoint, upper_endpoint)

    # チェックメソッドの呼び出し
    actual: bool = closed_range.is_included(given_value)

    # True かどうかチェック
    assert actual is True


def test_is_equal_to_another_range():
    lower_endpoint = 3
    upper_endpoint = 8
    expected_status = True

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    another_closed_range = ClosedRange(lower_endpoint, upper_endpoint)

    actual: bool = closed_range.is_same_range(another_closed_range)

    assert actual is expected_status


def test_is_not_equal_to_another_range():
    lower_endpoint = 3
    upper_endpoint = 8
    another_lower_endpoint = 2
    expected_status = False

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    another_closed_range = ClosedRange(another_lower_endpoint, upper_endpoint)

    actual: bool = closed_range.is_same_range(another_closed_range)

    assert actual is expected_status


def test_is_included_to_another_range():
    lower_endpoint = 3
    upper_endpoint = 8
    another_lower_endpoint = 2
    expected_status = True

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    another_closed_range = ClosedRange(another_lower_endpoint, upper_endpoint)

    actual: bool = closed_range.is_included_to_another_range(another_closed_range)

    assert actual is expected_status


def test_is_not_included_to_another_range():
    lower_endpoint = 3
    upper_endpoint = 8
    another_lower_endpoint = 4
    expected_status = False

    closed_range = ClosedRange(lower_endpoint, upper_endpoint)
    another_closed_range = ClosedRange(another_lower_endpoint, upper_endpoint)

    actual: bool = closed_range.is_included_to_another_range(another_closed_range)

    assert actual is expected_status
