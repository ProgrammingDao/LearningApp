"""Top level application definition."""

from attrs import define
from kivy.app import App


@define(slots=False)
class LearningApp(App):  # type: ignore
    """Learning application."""
