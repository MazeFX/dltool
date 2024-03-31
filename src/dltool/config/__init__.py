import os
from pathlib import Path

import structlog

logger = structlog.get_logger(__name__)


def get_tool_path(name):
    paths = {"templates": Path(__file__).parent.parent.absolute().joinpath("project_templates")}

    try:
        p = paths[name]

    except KeyError:
        logger.exception("Configuration path unkown.")

    return p
