# -*- coding: utf-8 -*-

# @File    : unit.py
# @Date    : 2022-06-23
# @Author  : luoyu
import json

from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.table import Table
from rich.progress import track, Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn


def get_cookies():
    with open("cookies.txt") as f:
        cookies = f.read()
        cookies = {x['name']: x['value'] for x in json.loads(cookies)}
        print(cookies)
        return cookies


console = Console()


def progress_bar(total_percent,sessionId):
    _progress = Progress(TextColumn("[bold blue][progress.description]{task.description}"),
                         SpinnerColumn(finished_text="😊"),
                         BarColumn(style=Style(color="dark_goldenrod"),complete_style=Style(color="green4")),
                         TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                         TimeElapsedColumn())
    _bar = _progress.add_task(description=f"session:{sessionId[:5]}...", total=total_percent)
    return _progress, _bar


if __name__ == "__main__":
    pass
