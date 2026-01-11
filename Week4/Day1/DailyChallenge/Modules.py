import requests
import time

def measure_load_time(url):
    start_time = time.time()
    
    response = requests.get(url)
    response.raise_for_status()  # raise an error if site not available
    
    end_time = time.time()
    
    return end_time - start_time

urls = ["https://www.google.com","https://www.ynet.com", "https://www.imdb.com"]
for url in urls:
    load_time = measure_load_time(url)
    print(f"Page {url} loaded in {load_time:.3f} seconds")