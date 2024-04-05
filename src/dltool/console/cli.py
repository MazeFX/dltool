#!/usr/bin/env python
"""Command Line Interface for DLTool.

This is a cli application based on the cleo library.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from cleo.application import Application as BaseApplication
from cleo.formatters.style import Style

from dltool import __version__

from .project_command import ProjectCommand

if TYPE_CHECKING:
    from cleo.events.console_events import COMMAND
    from cleo.io.inputs.input import Input
    from cleo.io.io import IO
    from cleo.io.outputs.output import Output


class Application(BaseApplication):
    title = """
        <blue>    ____  __ </blue><red> ______            __ </red>
        <blue>   / __ \/ / </blue><red>/_  __/___  ____  / / </red>
        <blue>  / / / / /  </blue><red> / / / __ \/ __ \/ /  </red>
        <blue> / /_/ / /___</blue><red>/ / / /_/ / /_/ / /___ </red>
        <blue>/_____/_____/</blue><red>_/  \____/\____/_____/ </red>

               """

    description = """
    The Delta Live Tool for easy setup of Delta Live Tables.
    """

    def __init__(self) -> None:
        super().__init__(self.title, __version__)

    @property
    def display_name(self) -> str:
        if self._display_name is None:
            return self._name
            # return re.sub(r"[\s\-_]+", " ", self._name).title()

        return self._display_name

    @property
    def long_version(self) -> str:
        if self._name:
            if self._version:
                return f"<b>{self.display_name}</b> (version <c1>{self._version}</c1>)"

            return f"<b>{self.display_name}</b>"

        return "<b>Console</b> application"

    def create_io(
        self,
        input: Input = None,
        output: Output = None,
        error_output: Output = None,
    ) -> IO:
        io = super().create_io(input, output, error_output)

        # Set our own CLI styles
        formatter = io.output.formatter

        formatter.set_style("blue", Style("blue"))
        formatter.set_style("red", Style("red"))
        formatter.set_style("green", Style("green"))

        formatter.set_style("c1", Style("cyan"))
        formatter.set_style("c2", Style("default", options=["bold"]))
        formatter.set_style("info", Style("blue"))
        formatter.set_style("comment", Style("green"))
        formatter.set_style("warning", Style("yellow"))
        formatter.set_style("debug", Style("default", options=["dark"]))
        formatter.set_style("success", Style("green"))

        # Dark variants
        formatter.set_style("c1_dark", Style("cyan", options=["dark"]))
        formatter.set_style("c2_dark", Style("default", options=["bold", "dark"]))
        formatter.set_style("success_dark", Style("green", options=["dark"]))

        io.output.set_formatter(formatter)
        io.error_output.set_formatter(formatter)

        self._io = io

        return io

    def _run_command(self, command: COMMAND, io: IO) -> int:
        io.write_line(self.long_version)

        super()._run_command(command, io)

        # if self._event_dispatcher is None:
        #     return command.run(io)

        # # Bind before the console.command event,
        # # so the listeners have access to the arguments and options
        # try:
        #     command.merge_application_definition()
        #     io.input.bind(command.definition)
        # except Exception:
        #     # Ignore invalid option/arguments for now,
        #     # to allow the listeners to customize the definition
        #     pass

        # command_event = ConsoleCommandEvent(command, io)
        # error = None

        # try:
        #     self._event_dispatcher.dispatch(command_event, COMMAND)

        #     if command_event.command_should_run():
        #         exit_code = command.run(io)
        #     else:
        #         exit_code = ConsoleCommandEvent.RETURN_CODE_DISABLED
        # except Exception as e:
        #     error_event = ConsoleErrorEvent(command, io, e)
        #     self._event_dispatcher.dispatch(error_event, ERROR)
        #     error = error_event.error
        #     exit_code = error_event.exit_code

        #     if exit_code == 0:
        #         error = None

        # terminate_event = ConsoleTerminateEvent(command, io, exit_code)
        # self._event_dispatcher.dispatch(terminate_event, TERMINATE)

        # if error is not None:
        #     raise error

        # return terminate_event.exit_code


def main() -> int:
    app = Application()

    # Add the commands
    app.add(ProjectCommand())

    exit_code: int = app.run()
    return exit_code


if __name__ == "__main__":
    main()
