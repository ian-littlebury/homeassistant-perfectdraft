from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

DOMAIN = "perfectdraft"


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PerfectDraft."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is None:
            data_schema = vol.Schema(
                {
                    vol.Required("email"): str,
                    vol.Required("password"): str,
                    vol.Required("api_key"): str,
                    vol.Required("recaptcha_site_key"): str,
                    vol.Required("recaptcha_token"): str,
                }
            )
            return self.async_show_form(step_id="user", data_schema=data_schema)

        return self.async_create_entry(
            title="PerfectDraft",
            data=user_input,
        )
