#!/usr/bin/env python3
"""Read-only Element API checker (skeleton).

Reads public market data only. Makes no write calls, places no orders,
and never prints the API key.

Usage:
    ELEMENT_API_KEY="..." python3 src/element_readonly.py --collection <slug>

Endpoint paths must be taken from Element's official OpenAPI/SDK
documentation (https://api.element.market/openapi/ and
https://github.com/element-market/element-js-sdk) once a key is granted.
This skeleton deliberately does not guess endpoint paths that were not
verified in that documentation.
"""

import argparse
import os
import sys
import time
import urllib.request


BASE_URL = "https://api.element.market"
# Respect Element's documented default: 120 requests/minute per API key.
MIN_INTERVAL_SECONDS = 0.5


def get_api_key() -> str:
    key = os.environ.get("ELEMENT_API_KEY", "").strip()
    if not key:
        print("ELEMENT_API_KEY is not set in the environment.", file=sys.stderr)
        print("Set it with: export ELEMENT_API_KEY=\"your-key-here\"", file=sys.stderr)
        sys.exit(1)
    return key


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only Element check.")
    parser.add_argument("--collection", required=True,
                        help="Collection slug or contract to check.")
    args = parser.parse_args()

    # The key is used only in the request header, never printed.
    api_key = get_api_key()
    _ = api_key

    print(f"Collection to check (read-only): {args.collection}")
    print(f"Base URL: {BASE_URL}")
    print("Status: skeleton — fill the verified endpoint path from the")
    print("official Element OpenAPI/SDK docs before making a live call.")
    time.sleep(MIN_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
