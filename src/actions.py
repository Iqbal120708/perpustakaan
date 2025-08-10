import sys
import time

from rich.console import Console
from rich.spinner import Spinner

import db
from utils import task_decorator, cari_by_id

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

@task_decorator(spinner_config={"color_text": "bold yellow", "text": "Memperbarui data..."})
def update(id):
    if id is None:
        console.print("[bold red]Harus menyertakan id[/bold red]")
        return
    if not id.isdigit():
        console.print("[bold red]Id harus angka[/bold red]")
        return
    else:
        id_int = int(id)
        
    hasil = cari_by_id(db.table_data, id_int)
    if hasil is None:
        console.print("[bold red]Data tidak ditemukan[/bold red]")
        return
    
    console.print("[yellow]Ubah Data[/yellow]")
    print()
    
    console.print(f"[magenta]Masukkan Judul Baru ([italic dim]{hasil['title']}[/italic dim]):[/magenta]", end=" ")
    title = input()

    console.print(f"[green]Masukkan Nama Author ([italic dim]{hasil['author']}[/italic dim]):[/green]", end=" ")
    author = input()

    console.print(f"[blue]Masukkan Tahun Terbit ([italic dim]{hasil['years']}[/italic dim]):[/blue]", end=" ")
    years = int(input())
    
    for data in db.table_data:
        if data["id"] == id_int:
            data["title"] = title
            data["author"] = author
            data["years"] = years


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
