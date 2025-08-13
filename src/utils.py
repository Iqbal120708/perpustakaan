import time

from rich.console import Console
from rich.progress import track
from rich.spinner import Spinner
from db_instance  import db
from home import home

console = Console()


def loading():
    console.print("[bold magenta]Perpustakaan[/bold magenta]\n")
    
    for step in track(db.load_steps(), description="Loading..."):
        time.sleep(0.1)

    console.clear()


def task_decorator(spinner_config):
    if not isinstance(spinner_config, dict):
        raise ValueError("Parameter 'spinner' harus bertipe dict")

    def decorator(func):
        def wrapper(*args, **kwargs):
            console.clear()
            output_func = func(*args, **kwargs)
            # load_spinner = output_func.get("load_spinner") if isinstance(output_func, dict) else True
            # if load_spinner:
            spinner = Spinner(
                "dots",
                text=f"[{spinner_config["color_text"]}]{spinner_config["text"]}[/{spinner_config["color_text"]}]",
            )
            with console.status(spinner):
                time.sleep(2)
            home()

        return wrapper

    return decorator
    
# def cari_by_id(data, target_id):
#     for item in data:
#         if item.get("id") == target_id:
#             return item
#     return None

def get_data_and_validate_id(id):
    if id is None:
        console.print("[bold red]Harus menyertakan id[/bold red]")
        return
    if not id.isdigit():
        console.print("[bold red]Id harus angka[/bold red]")
        return
    else:
        id_int = int(id)
        
    item = db.get_item_by_id(id_int)
    if item is None:
        console.print("[bold red]Data tidak ditemukan[/bold red]")
        return
    
    return item