import os
import sys

BASE_URL = os.environ.get("PYPISTATS_BASE_URL", "https://pypistats.com")
API_KEY = os.environ.get("PYPISTATS_API_KEY", "")


def validate_api_key():
    if not API_KEY:
        print("Error: PYPISTATS_API_KEY is required.\n")
        print("To get an API key:")
        print("  1. Sign up at https://pypistats.com")
        print("  2. Go to your dashboard and generate an API key")
        print("  3. Export it in your shell:\n")
        print('     export PYPISTATS_API_KEY=pyps_your_key_here\n')
        print("Free tier API keys work. Get one at https://pypistats.com/pricing")
        sys.exit(1)
