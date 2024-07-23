from stem import Signal
from stem.control import Controller
from rich.console import Console

console = Console()

TOR_PASSWORD = 'your_tor_password'

def connect_to_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        console.print("[bold green]Successfully connected to Tor.[/bold green]")

def renew_tor_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=TOR_PASSWORD)
        controller.signal(Signal.NEWNYM)
        console.print("[bold green]Tor connection renewed.[/bold green]")
