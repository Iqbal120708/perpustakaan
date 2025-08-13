import textwrap

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from db_instance  import db
#from db import Database

console = Console()


def home():
    console.clear()
    
    print(end="\n\n")
    menu_text = """
        **1. Tambah Data** (*add*)  
        **2. Ubah Data** (*update/:id*)  
        **3. Hapus Data** (*delete/:id*)  
        **4. Keluar** (*exit*)  
    """

    md = Markdown(textwrap.dedent(menu_text))
    console.print(md)

    print(end="\n")

    console.print(
        Panel.fit(
            "[bold cyan]Cara memilih:[/bold cyan]\n"
            "[green]• ketik perintah[/green] (misal: add atau update/2)",
            title="Panduan",
            border_style="yellow",
        )
    )

    print(end="\n")
    
    table = Table(title="Daftar Pengguna")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Author", style="green")
    table.add_column("Year", style="blue")

    for item in db.data:
        table.add_row(
            str(item["id"]), item["title"], item["author"], str(item["years"])
        )

    console.print(table)

    print(end="\n")
