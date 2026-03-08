# pypistats-cli

Check PyPI package health, download trends, and version breakdowns from your terminal.

Powered by [pypistats.com](https://pypistats.com).

[![PyPI version](https://img.shields.io/pypi/v/pypistats-cli)](https://pypi.org/project/pypistats-cli/)
[![Python 3.9+](https://img.shields.io/pypi/pyversions/pypistats-cli)](https://pypi.org/project/pypistats-cli/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyPI Stats](https://pypistats.com/api/badges/pypistats-cli?period=month)](https://pypistats.com/packages/pypistats-cli)

## Install

```bash
pip install pypistats-cli
```

## Setup

An API key is **required**. Get one for free at [pypistats.com](https://pypistats.com):

1. Sign up at [pypistats.com](https://pypistats.com)
2. Go to your dashboard and generate an API key
3. Export it in your shell:

```bash
export PYPISTATS_API_KEY=pyps_your_key_here
```

Add it to your `~/.bashrc` or `~/.zshrc` to persist across sessions.

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
- **AI Summary** (PRO/Enterprise) — AI-powered health analysis and insights

## Tiers

| Feature | Free | Pro | Enterprise |
|---------|------|-----|------------|
| Download stats | Yes | Yes | Yes |
| Health score | Yes | Yes | Yes |
| Version breakdown | Yes | Yes | Yes |
| AI Summary | No | Yes | Yes |
| Rate limit | 10/min | 60/min | 300/min |

Get your API key at [pypistats.com/pricing](https://pypistats.com/pricing).

## Requirements

- Python 3.9+
- Dependencies: [click](https://pypi.org/project/click/), [httpx](https://pypi.org/project/httpx/), [rich](https://pypi.org/project/rich/)

## License

MIT
