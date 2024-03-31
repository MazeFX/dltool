# -*- coding: utf-8 -*-

import os
import sys
from typing import ClassVar

from cleo.helpers import argument, option
from cleo.io.inputs.argument import Argument
from cleo.io.inputs.option import Option

from dltool.project_management.classes import Project, ProjectConfig

from .base_command import BaseCommand


class ProjectCommand(BaseCommand):
    name = "project"
    description = "Project related action like init, config, etc.."

    arguments: ClassVar[list[Argument]] = [
        argument("action", "Action that you want to perform on the project.", optional=False),
        # argument("value", "Setting value.", optional=True, multiple=True),
    ]

    options: ClassVar[list[Option]] = [
        option("list", None, "List configuration settings."),
        option("unset", None, "Unset configuration setting."),
        option("local", None, "Set/Get from the project's local configuration."),
    ]

    help = (
        "Running <comment>models</> to assess the results.\n"
        "\n"
        "Input files can be put in the default The <comment>data</> directory. Or the search\n"
        "path can be provided as an argument.\n"
        "\n"
        "Output will be determined by the provided options. If no output options are\n"
        "provided the model output will printed out to the console."
    )

    def handle(self):
        # TODO - collect all actions needed
        action = self.argument("action")

        if action == "init":
            self._init_new_project()
            return
        else:
            text = "Hello"

        self.line("Unknown Action.")

    def _init_new_project(self):
        # TODO - write Verbose message on verbose mode for input parameters

        # Print the init project project instructions on the screen
        self.line("")
        self.line(
            "We need you to <comment>answer</comment> some questions for the options in generating a <info>new project</info>."
        )
        self.line("")
        self.line("")

        # FEATURE - check for tool settings

        # FEATURE - check for existing config yaml file for project

        # FEATURE - create new project
        project = Project(ProjectConfig, self.io)

        # Collect all inputs based on config class
        project_inputs = project.get_project_inputs()

        project.output_templates()

        # Print the init project finished message
        self.line("")
        self.line("<comment>Project successfully initiated.</comment>")
