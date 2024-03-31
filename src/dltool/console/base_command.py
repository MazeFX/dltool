from cleo.commands.command import Command


class BaseCommand(Command):
    def wrap_handle(self, args, io, command):  # type: (Args, IO, CliKitCommand) -> Optional[int]
        self._args = args
        self._io = io
        self._command = command
        self._start_console_app()
        return self.handle()

    def _start_console_app(self):
        pn_header = """
           <title-blue> .______   </><title-red>.__   __.  </>
           <title-blue> |   _  \  </><title-red>|  \ |  |  </>
           <title-blue> |  |_)  | </><title-red>|   \|  |  </>
           <title-blue> |   ___/  </><title-red>|  . `  |  </>
           <title-blue> |  |      </><title-red>|  |\   |  </>
           <title-blue> | _|      </><title-red>|__| \__|  </>
            
              <comment>Plan your norms</>
        """

        self.line(f"<comment>{pn_header}</>")
