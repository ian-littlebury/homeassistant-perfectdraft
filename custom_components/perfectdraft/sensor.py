from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up PerfectDraft sensors from a config entry."""
    data: dict[str, Any] = hass.data[DOMAIN][entry.entry_id]
    email = data.get("email", "unknown")

    # For now we expose a single dummy sensor just to show the wiring works
    async_add_entities(
        [
            PerfectDraftDummySensor(
                entry_id=entry.entry_id,
                email=email,
            )
        ],
        update_before_add=True,
    )


class PerfectDraftDummySensor(SensorEntity):
    """A dummy sensor representing a PerfectDraft machine."""

    _attr_has_entity_name = True

    def __init__(self, entry_id: str, email: str) -> None:
        self._attr_unique_id = f"perfectdraft_{entry_id}_dummy"
        self._attr_name = "PerfectDraft Dummy Status"
        self._email = email
        self._attr_native_unit_of_measurement = None

    @property
    def native_value(self) -> str:
        # Just returns a static string for now
        return f"Configured for {self._email}"
