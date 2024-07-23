from tor_controller import connect_to_tor, renew_tor_connection
from scraper import search_and_scan
from rich.console import Console

console = Console()

def main():
    console.print("[bold blue]Connecting to Tor...[/bold blue]")
    connect_to_tor()
    
    query = console.input("[bold green]Enter your search term: [/bold green]")
    search_and_scan(query)
    
    console.print("[bold blue]Renewing Tor connection...[/bold blue]")
    renew_tor_connection()
    
if __name__ == "__main__":
    main()
