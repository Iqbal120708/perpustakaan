import sys
import time

from rich.console import Console
from rich.spinner import Spinner

import db
from utils import task_decorator

console = Console()


@task_decorator(spinner_config={"color_text": "bold green", "text": "Menambah data..."})
def add():

    console.print("[bold green]Tambah Data[/bold green]")
    print()

    console.print("[magenta]Masukkan Judul:[/magenta]", end=" ")
    title = input()

    console.print("[green]Masukkan Nama Author:[/green]", end=" ")
    author = input()

    console.print("[blue]Masukkan Tahun Terbit:[/blue]", end=" ")
    years = int(input())

    db.last_id += 1
    db.table_data.append(
        {"id": db.last_id, "title": title, "author": author, "years": years}
    )


def update(id=None):
    if id is None:
        console.print("[bold red]Harus menyertakan id[/bold red]")
        return
    if not id.isdigit():
        console.print("[bold red]Id harus angka[/bold red]")
        return
    console.print("[yellow]Ubah Data[/yellow]")


def delete(id=None):
    if id is None:
        console.print("[bold red]Harus menyertakan id[/bold red]")
        return
    if not id.isdigit():
        console.print("[bold red]Id harus angka[/bold red]")
        return
    console.print("[red]Hapus Data[/red]")


def exit():
    spinner = Spinner("dots", text="[bold red]Keluar dari program...[/bold red]")
    with console.status(spinner):
        time.sleep(2)  # Simulasi proses
    sys.exit()
