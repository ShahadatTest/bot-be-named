"""Regression for #431: MissingPermissions uses missing_permissions, not missing_perms."""

from types import SimpleNamespace

from nextcord.ext.commands import errors

from modules.error_logging.error_handling import ErrorHandler


def test_missing_permissions_lists_required_permissions():
    error = errors.MissingPermissions(["manage_messages", "kick_members"])
    handler = ErrorHandler(
        message=SimpleNamespace(guild=None),
        error=error,
        human_readable_msg="",
    )
    message = handler._ErrorHandler__user_error_message()
    assert "manage_messages" in message or "Manage Messages" in message
    assert "kick_members" in message or "Kick Members" in message
    assert "missing_perms" not in message
