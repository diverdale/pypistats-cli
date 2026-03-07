# pypistats-cli

Check PyPI package health, download trends, and version breakdowns from your terminal.

Powered by [pypistats.com](https://pypistats.com).

[![PyPI version](https://img.shields.io/pypi/v/pypistats-cli)](https://pypi.org/project/pypistats-cli/)
[![Python 3.9+](https://img.shields.io/pypi/pyversions/pypistats-cli)](https://pypi.org/project/pypistats-cli/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI Stats](/api/badges/pypistats-cli?period=month)](/packages/pypistats-cli)

## Install

```bash
pip install pypistats-cli
```

## Usage

```bash
pypistats check requests
```

```
╭─ requests v2.32.5 ──────────────────────────────────╮
│                                                      │
│  Downloads (30d):  ▄▄▂▂▅▆▅▄▄▂▁▃▄▄▄▅▃▂▄▅▆█▄▂▂▁▆  1.0B │
│  Trend:            +0.1% ↑                           │
│  Health:           █████████░ 91/100                 │
│  License:          Apache-2.0                        │
│  Author:           Kenneth Reitz                     │
│                                                      │
│  Top Versions                                        │
│  2.32.5      ██████████████  69.6%                   │
│  2.31.0      ██  8.3%                                │
│  2.32.4      █  7.2%                                 │
│  2.32.3      █  5.4%                                 │
│  2.27.1      █  1.5%                                 │
╰──────────────────────────────────────────────────────╯
```

### Options

```bash
# Custom time window
pypistats check fastapi --days 7

# Help
pypistats --help
pypistats check --help
```

## Features

- **Download trends** with sparkline visualization
- **Health score** (0-100) based on download consistency, popularity, metadata, and growth
- **Version breakdown** showing adoption percentages
- **Package metadata** including license, author, and latest version

## API Key (Optional)

For higher rate limits, set your API key:

```bash
export PYPISTATS_API_KEY=your-key-here
```

Get an API key at [pypistats.com/pricing](https://pypistats.com/pricing).

## Requirements

- Python 3.9+
- Dependencies: [click](https://pypi.org/project/click/), [httpx](https://pypi.org/project/httpx/), [rich](https://pypi.org/project/rich/)

## License

MIT
