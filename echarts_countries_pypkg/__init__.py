# flake8: noqa
import os

from echarts_countries_pypkg._version import __version__
from echarts_countries_pypkg._version import __author__
from lml.plugin import PluginInfoChain, PluginInfo
from pyecharts.js_extensions import JsExtension


@PluginInfo('pyecharts_js_extension', tags=['map'])
class Pypkg():
    def __init__(self):
        __package_path__ = os.path.dirname(__file__)
        __registry_json__ = os.path.join(
            __package_path__, "resources")
        self.js_extension = JsExtension.from_registry_path(__registry_json__)
