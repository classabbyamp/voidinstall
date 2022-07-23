from typing import Callable


class ConfigureTask:
    def __init__(self, id: str, **kwargs):
        self.id = id


class StringTask(ConfigureTask):
    def __init__(self, label: str, password=False,
                 validator: Callable[[str], str] | None = None, **kwargs):
        self.label = label
        self.password = password
        self.validate = validator
        super().__init__(**kwargs)

    def do_configure(self, raw: str) -> dict:
        out = {}
        if self.validate:
            out["data"] = self.validate(raw)
        return out


class SelectTask(ConfigureTask):
    def __init__(self, label: str, multi=False, **kwargs):
        self.label = label
        self.multi = multi
        super().__init__(**kwargs)


class InstallTask:
    def __init__(self):
        ...
