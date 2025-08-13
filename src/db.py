import json
import os
from pathlib import Path
from rich.console import Console
import time
console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent

class Database:
    def __init__(self):
        self.db_path = os.path.join("data", "data.json")
        self.full_path = BASE_DIR / self.db_path
        self.data = self.read_json()
        self.item = None
        
    @property
    def last_id(self):
        return self.data[-1]["id"]
        
    def load_steps(self):
        for item in self.data:
            yield item
        
    # Fungsi bantu untuk baca file JSON
    def read_json(self):
        if not os.path.exists(self.full_path):
            console.print("[bold red]File tidak ditemukan. Buat file di lokasi 'perpustakaan/data/data.json'[/bold red]")
            return
        if os.path.exists(self.full_path) and os.path.getsize(self.full_path) == 0:
            with open(self.full_path, "w", encoding="utf-8") as f:
                f.write("[]")
                
        with open(self.full_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
            

    # Fungsi bantu untuk tulis file JSON
    def write_json(self):
        with open(self.full_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def get_item_by_id(self, item_id):
        for item in self.data:
            if item["id"] == item_id:
                self.item = item
                return self.item
        return
    
    # CREATE
    def create_item(self, item):
        data = self.data
        data.append(item)
        self.write_json()
        return item
        
    def update_item(self, new_item):
        for item in self.data:
            if item == self.item:
                self.data.remove(item)
        
         # Pastikan id ada di paling depan
        ordered_item = {"id": self.item["id"], **new_item}
        self.data.append(ordered_item)
        
        self.data.sort(key=lambda x: x["id"])
        
        self.write_json()
                
    def delete_item(self):
        for item in self.data:
            if item == self.item:
                self.data.remove(item)
                
        self.write_json()

# a = Database()
# print(a.data)
# print(a.create_item({"id":2, "title": "test", "author": "test", "years": 2025}))
# print(a.data)
# Contoh penggunaan
# if __name__ == "__main__":
#     # CREATE
#     create_item({"id": 1, "name": "Laptop", "qty": 5})
#     create_item({"id": 2, "name": "Mouse", "qty": 10})

#     # READ
#     print("All:", get_all_items())
#     print("By ID:", get_item_by_id(1))

#     # UPDATE
#     update_item(1, {"qty": 7})

#     # DELETE
#     delete_item(2)

#     print("Final:", get_all_items())