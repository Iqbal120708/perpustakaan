import sys
import time

from rich.console import Console
from rich.spinner import Spinner
from rich.markdown import Markdown
import textwrap
from utils import task_decorator, get_data_and_validate_id
from db_instance import db

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
    
    db.create_item({"id": db.last_id + 1, "title": title, "author": author, "years": years})


@task_decorator(spinner_config={"color_text": "bold yellow", "text": "Memperbarui data..."})
def update(id):
    data = get_data_and_validate_id(id)
    if not data:
        return #{"load_spinner": False}

    console.print("[yellow]Ubah Data[/yellow]")
    print()

    console.print(f"[magenta]Masukkan Judul Baru ([italic]{data['title']}[/italic]):[/magenta]", end=" ")
    title = input()

    console.print(f"[green]Masukkan Nama Author ([italic]{data['author']}[/italic]):[/green]", end=" ")
    author = input()

    console.print(f"[blue]Masukkan Tahun Terbit ([italic]{data['years']}[/italic]):[/blue]", end=" ")
    years = int(input())

    new_item = {
        "title": title,
        "author": author,
        "years": years
    }
    db.update_item(new_item)


@task_decorator(spinner_config={"color_text": "bold red", "text": "Menghapus data..."})
def delete(id=None):
    data = get_data_and_validate_id(id)
    if not data:
        return #{"load_spinner": False}

    console.print("[yellow]Hapus Data[/yellow]")
    print()

    menu_text = f"""
        **Anda akan menghapus data**

        **ID: {data['id']}**  
        **Judul: {data['title']}**  
        **Pembuat: {data['author']}**  
        **Tahun Terbit: {data['years']}**
    """

    md = Markdown(textwrap.dedent(menu_text))
    console.print(md)

    console.print("[bold yellow]\nApakah yakin ingin menghapus data (y/n):[/bold yellow]", end=" ")
    opsi = input()

    if opsi != "y":
        return #{"load_spinner": False}

    db.delete_item()


def exit():
    spinner = Spinner("dots", text="[bold red]Keluar dari program...[/bold red]")
    with console.status(spinner):
        time.sleep(2)  # Simulasi proses
    sys.exit()
