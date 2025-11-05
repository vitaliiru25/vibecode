import pytest
import requests
from bs4 import BeautifulSoup
import http.server
import threading
import socket
import os

def get_free_port():
    """Get a free port on the system"""
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

@pytest.fixture(scope="session")
def server():
    """Start a local HTTP server"""
    port = get_free_port()
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    
    # Start the server in a new thread
    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
    
    yield f"http://localhost:{port}"
    
    httpd.shutdown()
    httpd.server_close()

def test_file_exists():
    """Test if index.html exists"""
    assert os.path.exists('index.html')

def test_file_not_empty():
    """Test if index.html is not empty"""
    assert os.path.getsize('index.html') > 0

def test_page_accessibility(server):
    """Test if the page is accessible"""
    response = requests.get(f"{server}/index.html")
    assert response.status_code == 200

def test_page_content():
    """Test the content of the page"""
    with open('index.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Test for required elements
        assert soup.find('header') is not None
        assert soup.find('nav') is not None
        assert soup.find('main') is not None
        assert soup.find('footer') is not None
        
        # Test navigation links
        nav_links = soup.find_all('a')
        assert len(nav_links) >= 2
        
        # Test main sections
        sections = soup.find_all('section')
        assert len(sections) >= 2
        
        # Test headings
        assert soup.find('h1') is not None
        assert len(soup.find_all('h2')) >= 2
