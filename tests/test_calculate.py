 
import pytest

from src.calculate import (
    do_calculation,
    )


def test_do_calculation_01():
    """
    Test invalid input 
    """

    input = '1'

    with pytest.raises(TypeError):
        result = do_calculation(input)


def test_do_calculation_02():
    """
    Test invalid input 
    """

    input = [1]

    with pytest.raises(TypeError):
        result = do_calculation(input)


def test_do_calculation_03():
    """
    Test invalid input 
    """

    input = -1

    with pytest.raises(AssertionError):
        result = do_calculation(input)


def test_do_calculation_04():
    """
    Test invalid input 
    """

    input = -0.0001

    with pytest.raises(AssertionError):
        result = do_calculation(input)


def test_do_calculation_05():
    """
    Test valid input
    """

    input = 0
    result = do_calculation(input)
    correct_result = 1
    assert result == correct_result


def test_do_calculation_06():
    """
    Test valid input
    """

    input = 1
    result = do_calculation(input)
    correct_result = 2
    assert result == correct_result
    assert True == False


def test_do_calculation_07():
    """
    Test valid input
    """

    input = 2.51
    result = do_calculation(input)
    correct_result = 3.51
    assert abs(result - correct_result) < 1e-6


def test_do_calculation_08():
    """
    Test valid input
    """

    input = 100_002
    result = do_calculation(input)
    correct_result = 100_003
    assert abs(result - correct_result) < 1e-6
