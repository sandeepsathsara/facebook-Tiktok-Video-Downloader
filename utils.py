def format_bytes(size):
    # Convert bytes to human-readable
    for unit in ['B','KB','MB','GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
