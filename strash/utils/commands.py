def str__shred_file_recursive(dirpath: str, iterations: str) -> str:
    """Method that stores the recycle bin cleanup code structure."""
    return (
        f'find "{dirpath}" -depth -type f -exec shred -n {iterations} -v -z -u {{}} \\;'
    )


def str__shred_file(filepath: str, iterations: str) -> str:
    """Returns a string for shred command for files"""
    return f"shred -n {iterations} -v -z -u {filepath};"


def str__delete_folder_empty(dirpath: str) -> str:
    """Method that returns string to delete empty folders."""
    return f'find "{dirpath}" -type d -empty -delete'
