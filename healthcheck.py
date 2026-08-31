#!/usr/bin/env python3
"""
Simple healthcheck script for the cortex-take-home-demo service.
Checks that a target endpoint responds successfully within a timeout.
"""

import sys
import time
import urllib.request

DEFAULT_URL = "https://example.com/health"
TIMEOUT_SECONDS = 5


def check_endpoint(url: str = DEFAULT_URL, timeout: int = TIMEOUT_SECONDS) -> bool:
    try:
        start = time.time()
        with urllib.request.urlopen(url, timeout=timeout) as response:
            elapsed = time.time() - start
            print(f"Status: {response.status} | Response time: {elapsed:.2f}s")
            return response.status == 200
    except Exception as e:
        print(f"Healthcheck failed: {e}")
        return False


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    success = check_endpoint(target)
    sys.exit(0 if success else 1)
