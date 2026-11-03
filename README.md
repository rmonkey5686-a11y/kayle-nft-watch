# Kayle NFT Watch — Personal Collection Tracker

A personal, read-only NFT research tool. It tracks collections the owner
follows across Robinhood, BNB Chain, and Ethereum — floor price, listings,
supply, and new drops — to decide which free or low-cost mints are worth
checking manually.

## What it does

- Reads public market data (collections, orders, assets) from the
  Element Public API.
- Caches results and respects rate limits (default: 120 requests/minute
  per API key, per Element's documentation).
- Produces a short, human-readable summary: collection, floor, listings,
  supply, and what changed since the last check.

## What it does NOT do

- It does not place, fill, or cancel orders automatically.
- It does not buy, sell, mint, sign, or connect a wallet on its own.
- It does not store, print, or commit any API key, seed phrase, password,
  or private key. The API key is read only from the environment
  (`ELEMENT_API_KEY`) at run time and is never written to this repo.

## How to use

1. Request an Element API key via Element's API Request Form.
2. Set it in your environment (do not paste it into any file here):

   ```bash
   export ELEMENT_API_KEY="your-key-here"
   ```

3. Run the read-only checker:

   ```bash
   python3 src/element_readonly.py --collection <collection-slug-or-contract>
   ```

   Endpoint paths are filled in from Element's official OpenAPI/SDK
   documentation once a key is granted; the script in this repo is a
   read-only skeleton and makes no write calls.

## Project status

- Draft, prepared for an Element API key application.
- No API key has been issued for this project yet.
- No automated trading is planned.

## Contact

- X: @Kaylepwsi (owner's account; the project is personal, not a
  company or a public marketplace).
- Element API contact for questions: api@element.market
