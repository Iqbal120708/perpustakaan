import time

from rich.console import Console
from rich.progress import track
from rich.spinner import Spinner

from home import home

console = Console()


def loading():
    console.print("[bold magenta]Perpustakaan[/bold magenta]\n")

    for step in track(range(10), description="Loading..."):
        time.sleep(0.1)

    console.clear()


def task_decorator(spinner_config):
    if not isinstance(spinner_config, dict):
        raise ValueError("Parameter 'spinner' harus bertipe dict")

    def decorator(func):
        def wrapper(*args, **kwargs):
            console.clear()
            func(*args, **kwargs)
            spinner = Spinner(
                "dots",
                text=f"[{spinner_config["color_text"]}]{spinner_config["text"]}[/{spinner_config["color_text"]}]",
            )
            with console.status(spinner):
                time.sleep(2)
            home()

        return wrapper

    return decorator
    
def cari_by_id(data, target_id):
    for item in data:
        if item.get("id") == target_id:
            return item
    return None


