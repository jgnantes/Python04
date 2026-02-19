def ft_archive_creation(file_name: str, txt_lines: list) -> None:
    """Creates a file and fills it with strings from a list"""
    try:
        file = open(file_name, 'w')
    except (FileNotFoundError, PermissionError) as e:
        print(f"A {type(e).__name__} occured: '{e}'")
        print(f"The file {file_name} could no be found or accessed")
        return
    except Exception as e:
        print(f"A {type(e).__name__} occured: '{e}'")
        print("The program cannot continue")
        return

    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    for line in txt_lines:
        try:
            file.write(f"{line}\n")
            print(f"{line}")
        except Exception as e:
            print(f"A {type(e).__name__} occured: {e}")
            print(f"'{line}' could not be written in {file_name}", end=' ')
            print("but the program continues!\n")
    print("")
    file.close()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name: str = 'new_discovery.txt'
    txt_lines: list = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    ft_archive_creation(file_name, txt_lines)
