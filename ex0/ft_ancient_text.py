def ft_ancient_text(file_name: str):
    """"""
    try:
        file = open(file_name, 'r')
        text: str = file.read()
        file.close()
    except (FileNotFoundError, PermissionError) as e:
        print(f"A {type(e).__name__} occured: '{e}'")
        print(f"The file {file_name} could no be found or accessed")
        return

    print(f"Accesing Storage Vault: {file_name}")
    print("Connection established...\n")
    print(f"{text}\n")
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ft_ancient_text('ancint_fragment.txt')
