"""Constants for Battery Notes tests."""

from homeassistant.const import (
    CONF_DEVICE_ID,
)

from custom_components.battery_notes.const import (
    CONF_BATTERY_TYPE,
    CONF_BATTERY_QUANTITY,
    CONF_BATTERY_LOW_THRESHOLD,
)

# Mock config data to be used across multiple tests
MOCK_CONFIG = {
    CONF_DEVICE_ID: "c6294da5c8b7555b8e8c502ff19cffb0",
    CONF_BATTERY_TYPE: "PP3",
    CONF_BATTERY_QUANTITY: 1,
    CONF_BATTERY_LOW_THRESHOLD:30,
    }
