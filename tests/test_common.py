"""Test Battery Notes common functions."""

from unittest.mock import patch

import pytest

from custom_components.battery_notes.common import isfloat

pytest_plugins = "pytest_homeassistant_custom_component"


# This fixture checks isfloat when not valid.
def test_isfloat():
    assert isfloat("A") == False
