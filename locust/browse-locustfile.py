from locust import FastHttpUser, task, between

class Browse(FastHttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 3)  # Simulate user think time between requests

    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def browse_page(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Host": "127.0.0.1:5000",
            "Priority": "u=0, i",
        }
        with self.client.get("/browse", headers=headers, catch_response=True) as resp:
            if resp.status_code != 200:
                resp.failure(f"Failed to load browse page: {resp.status_code}")