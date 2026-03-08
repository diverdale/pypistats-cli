import click
from rich.console import Console

from . import __version__


@click.group()
@click.version_option(__version__, prog_name="pypistats")
def cli():
    """PyPI package analytics from pypistats.com"""
    pass


@cli.command()
@click.argument("package")
@click.option("--days", default=30, help="Number of days to analyze", show_default=True)
def check(package: str, days: int):
    """Show download stats, health score, and version info for a package."""
    from .config import validate_api_key
    from .api import fetch_package, fetch_health, fetch_summary, PackageNotFoundError, InvalidApiKeyError
    from .display import render_check

    validate_api_key()

    console = Console()

    with console.status(f"[blue]Fetching stats for {package}...", spinner="dots"):
        try:
            pkg_data = fetch_package(package, days)
            health_data = fetch_health(package)
        except PackageNotFoundError:
            console.print(f"[red]Package '{package}' not found on pypistats.com[/red]")
            ctx = click.get_current_context()
            ctx.exit(1)
        except InvalidApiKeyError:
            console.print("[red]Invalid API key. Check your PYPISTATS_API_KEY environment variable.[/red]")
            ctx = click.get_current_context()
            ctx.exit(1)
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
            ctx = click.get_current_context()
            ctx.exit(1)

    # Fetch AI summary if tier supports it
    summary_data = None
    tier = pkg_data.get("tier", "FREE")
    if tier in ("PRO", "ENTERPRISE"):
        with console.status("[blue]Generating AI summary...", spinner="dots"):
            summary_data = fetch_summary(package)

    render_check(pkg_data, health_data, days, summary_data)
