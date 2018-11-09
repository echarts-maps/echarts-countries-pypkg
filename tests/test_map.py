# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map


def test_city_map():
    value = [1, 100]
    attr = ['Gujarat', 'Tamil Nadu']
    map = Map('India', width=800, height=600)
    map.add(
        '',
        attr,
        value,
        maptype='印度',
        is_visualmap=True,
        visual_text_color="#000",
    )
    html = map._repr_html_()
    assert "India" in html
    assert "nbextensions/echarts-countries-js" in html
