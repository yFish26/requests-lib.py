"""Tests for requests.packages module."""

import pytest

from requests import packages


class TestPackagesModule:
    """Test suite for packages module."""

    def test_packages_module_exists(self):
        """Test that packages module is importable."""
        assert packages is not None
        
