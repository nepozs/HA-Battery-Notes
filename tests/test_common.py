"""Test Battery Notes common functions."""

from unittest.mock import patch

import pytest

from custom_components.battery_notes.common import isfloat

pytest_plugins = "pytest_homeassistant_custom_component"


def test_isfloat():
    """Test isfloat."""

    x = None
    assert isfloat(x) == False
    assert isfloat("A") == False
    assert isfloat(1) == True
    assert isfloat(1.1) == True

