# SQL_Tor - DarkWeb Vulnability Scraper


This program uses Ahmia to find onion-based websites based on your search input. It will then check all the URLs to determine whether they are dynamic and might be vulnerable to SQL injection. If so, you can use your SQL expertise to practice taking down those filthy businesses on the Tor browser.

## Requirements

- Python 3.x
- Tor (configured and running)
- Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/sql_tor.git
    cd sql_tor
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure Tor is installed and running. You can download Tor from [here](https://www.torproject.org/download/).

4. Update the `tor_controller.py` file with your Tor password:
    ```python
    TOR_PASSWORD = 'your_tor_password'
    ```

## Usage

1. Start Tor:
    Make sure the Tor service is running. You can start Tor from the command line or use the Tor Browser.

2. Run the main script:
    ```bash
    python main.py
    ```

3. Enter your search term when prompted:
    The script will use Ahmia to search for onion-based websites related to your input.

4. The script will:
    - Display the search results.
    - Visit each link found in the search results.
    - Check for dynamic URLs on each visited page.
    - Test dynamic URLs for SQL injection vulnerabilities.

## Warning

Use this project ethically and legally. The dark web can contain dangerous and illegal content. Ensure you do not violate any laws.

## Notes

- This project is for educational purposes only. Unauthorized use of this tool is prohibited.
- Ensure that the Tor service is properly configured and running before using this script.
- The script includes retry and cooldown mechanisms to handle potential scraping issues.

## License

This project is licensed under the MIT License.
