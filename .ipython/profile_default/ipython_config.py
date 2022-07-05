from custom_prompt import SimplePrompt

c = get_config()

c.TerminalInteractiveShell.prompts_class = SimplePrompt
c.TerminalInteractiveShell.separate_in = ""
c.TerminalInteractiveShell.confirm_exit = False
c.TerminalIPythonApp.display_banner = False
