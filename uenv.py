import os


with open(".env") as f:
    for line in f:
        if not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ[key] = value.strip()
