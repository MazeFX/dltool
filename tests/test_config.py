from __future__ import annotations

import os

from dltool.config import get_tool_path


def test_dltool_config_get_tool_path():
    test_name = "templates"

    test_path = get_tool_path(test_name)

    assert str(test_path) == os.getcwd() + "/src/dltool/templates"
