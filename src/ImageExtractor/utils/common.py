import os

def ensure_make_dir(path: str) -> None:
    try:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        else:
            pass
    except Exception as e:
        raise e
    