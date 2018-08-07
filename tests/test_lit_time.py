# pylint:disable=missing-docstring
from unittest.mock import patch

import pytest

from fortlit import lit_time


@pytest.mark.parametrize(
    "time,expected",
    [
        (
            "00:00",
            (
                "\nAs \x1b[1m\x1b[95mmidnight\x1b[0m was striking bronze blows upon "
                "the dusky air, Dorian Gray, dressed commonly, and with a muffler "
                "wrapped round his throat, crept quietly out of his house.\n- The "
                "Picture of Dorian Gray, \x1b[1mOscar Wilde\x1b[0m\n"
            ),
        ),
        ("14:24", ""),
    ],
)
@patch("fortlit.lit_time.choice")
def test_create(mock_choice, time, expected):
    mock_choice.side_effect = lambda seq: seq[0]

    assert lit_time.create(time) == expected
