import os

def save_file(file_content: bytes, file_name: str, directory: str = "temp") -> str:
    """Save the uploaded audio file to a specific directory.

    Args:
        file_content (bytes): The audio file content in bytes.
        file_name (str): The file name.
        directory (str): The directory where the file will be saved.

    Returns:
        str: The file path of the saved audio file.
    """

    # Create the directory if it does not exist
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{file_name}")
    
    with open(file_path, "wb") as audio_file:
        audio_file.write(file_content)
    
    return file_path

def delete_file(file_path: str) -> None:
    """Delete a file from the filesystem.

    Args:
        file_path (str): The path of the file to delete.
    """
    if os.path.isfile(file_path):
        os.remove(file_path)
