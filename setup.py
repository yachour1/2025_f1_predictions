import os
import sys
from pathlib import Path

def setup_environment():
    # Create cache directory
    cache_dir = Path("f1_cache")
    if not cache_dir.exists():
        cache_dir.mkdir()
        print(f"✅ Created cache directory at: {cache_dir.absolute()}")
    else:
        print(f"✅ Cache directory already exists at: {cache_dir.absolute()}")

    # Verify Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("⚠️ Warning: This project requires Python 3.8 or higher")
        return False

    print("\n🎉 Environment setup complete!")
    print("\nTo start using the project:")
    print("1. Make sure you're in the virtual environment (venv)")
    print("2. Run: python prediction1.py")
    return True

if __name__ == "__main__":
    setup_environment() 