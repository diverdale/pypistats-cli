from rich.console import Console
from rich.panel import Panel
from rich.text import Text

SPARK_CHARS = "▁▂▃▄▅▆▇█"


def sparkline(values: list[float]) -> str:
    if not values:
        return ""
    lo, hi = min(values), max(values)
    rng = hi - lo if hi != lo else 1
    return "".join(SPARK_CHARS[min(int((v - lo) / rng * 7), 7)] for v in values)


def health_bar(score: int, width: int = 10) -> str:
    filled = round(score / 100 * width)
    return "█" * filled + "░" * (width - filled)


def format_downloads(n: int | float) -> str:
    n = int(n)
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def render_check(pkg_data: dict, health_data: dict, days: int, summary_data: dict | None = None) -> None:
    console = Console()

    metadata = pkg_data.get("metadata", {})
    trend = pkg_data.get("trend", [])
    versions = pkg_data.get("versions", [])

    name = metadata.get("name", "unknown")
    version = metadata.get("latest_version", "?")

    # Calculate total downloads and trend
    downloads_list = [int(d.get("total_downloads", 0)) for d in trend]
    total = sum(downloads_list)
    spark = sparkline(downloads_list)

    # Growth: compare last 7 days vs previous 7 days
    if len(downloads_list) >= 14:
        recent = sum(downloads_list[-7:])
        previous = sum(downloads_list[-14:-7])
        growth = ((recent - previous) / previous * 100) if previous > 0 else 0
    elif len(downloads_list) >= 2:
        mid = len(downloads_list) // 2
        recent = sum(downloads_list[mid:])
        previous = sum(downloads_list[:mid])
        growth = ((recent - previous) / previous * 100) if previous > 0 else 0
    else:
        growth = 0

    growth_str = f"+{growth:.1f}%" if growth >= 0 else f"{growth:.1f}%"
    growth_arrow = " ↑" if growth > 0 else " ↓" if growth < 0 else ""
    growth_color = "green" if growth > 0 else "red" if growth < 0 else "white"

    score = health_data.get("score", 0)
    bar = health_bar(score)

    # Build output
    lines = Text()

    lines.append(f"  Downloads ({days}d):  ", style="dim")
    lines.append(f"{spark}  ", style="cyan")
    lines.append(f"{format_downloads(total)}\n", style="bold")

    lines.append("  Trend:            ", style="dim")
    lines.append(f"{growth_str}{growth_arrow}\n", style=growth_color)

    lines.append("  Health:           ", style="dim")
    score_color = "green" if score >= 70 else "yellow" if score >= 40 else "red"
    lines.append(f"{bar} ", style=score_color)
    lines.append(f"{score}/100\n", style=f"bold {score_color}")

    if metadata.get("license"):
        lines.append("  License:          ", style="dim")
        lines.append(f"{metadata['license']}\n")

    if metadata.get("author"):
        lines.append("  Author:           ", style="dim")
        lines.append(f"{metadata['author']}\n")

    # Version breakdown
    if versions:
        lines.append("\n")
        lines.append("  Top Versions\n", style="bold")
        total_ver = sum(int(v.get("download_count", 0)) for v in versions)
        for v in [v for v in versions if v.get("version")][:5]:
            count = int(v.get("download_count", 0))
            pct = (count / total_ver * 100) if total_ver > 0 else 0
            bar_width = max(1, round(pct / 100 * 20))
            lines.append(f"  {v['version']:<12}", style="dim")
            lines.append("█" * bar_width, style="blue")
            lines.append(f"  {pct:.1f}%\n", style="dim")

    # AI Summary (PRO/ENTERPRISE only)
    if summary_data and summary_data.get("summary"):
        lines.append("\n")
        lines.append("  AI Summary", style="bold")
        lines.append(" (PRO)\n", style="dim")
        for line in summary_data["summary"].strip().split("\n"):
            lines.append(f"  {line}\n", style="white")

    panel = Panel(
        lines,
        title=f"[bold]{name}[/bold] v{version}",
        border_style="blue",
        padding=(1, 1),
    )
    console.print(panel)
