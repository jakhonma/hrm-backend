
def directory_path(instance: str, filename: str):
    class_name = instance.__class__.__name__.lower()
    return f"{class_name}/{filename}"