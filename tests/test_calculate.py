 
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
