"""Tests for requests.adapters module."""

import pytest

from requests.adapters import HTTPAdapter


class TestHTTPAdapter:
    """Test suite for HTTPAdapter class."""

    def test_adapter_initialization(self):
        """Test that HTTPAdapter can be instantiated."""
        adapter = HTTPAdapter()
        assert adapter is not None
        assert isinstance(adapter, HTTPAdapter)

    def test_adapter_with_pool_connections(self):
        """Test HTTPAdapter with custom pool connections."""
        adapter = HTTPAdapter(pool_connections=20, pool_maxsize=30)
        assert adapter is not None
