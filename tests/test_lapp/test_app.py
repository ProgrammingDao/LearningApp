"""Test cases for top level definition of the learning application."""

from kivy.app import App

from lapp.app import LearningApp


def test_learning_app_creation():
    my_app = LearningApp()

    assert isinstance(my_app, App)
