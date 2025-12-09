from __future__ import annotations

import importlib.metadata

import test_cp_1 as m


def test_version():
    assert importlib.metadata.version("test_cp_1") == m.__version__
