from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from novem.vis.plot import Plot


class NovemCustom:
    def __init__(self, api: "Plot") -> None:
        self.api: "Plot" = api

    @property
    def js(self) -> str:
        return self.api._read("/config/custom/custom.js")

    @js.setter
    def js(self, value: str) -> None:
        return self.api._write("/config/custom/custom.js", value)

    @property
    def css(self) -> str:
        return self.api._read("/config/custom/custom.css")

    @css.setter
    def css(self, value: str) -> None:
        return self.api._write("/config/custom/custom.css", value)
