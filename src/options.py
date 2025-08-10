from rich.console import Console

from actions import add, delete, exit, update

console = Console()


def options():
    console.print("[bold cyan]Masukkan Opsi:[/bold cyan]", end=" ")
    user_opsi = input()

    true_opsi = {
        "add": add,
        "update": update,
        "delete": delete,
        "exit": exit,
    }

    path = user_opsi.strip().split("/")
    get_func = true_opsi.get(path[0])
    if get_func:
        return ("res_func", get_func(path[0]) if len(path) > 1 else get_func())
    else:
        console.print("[bold red]Opsi Tidak Valid[/bold red]")
