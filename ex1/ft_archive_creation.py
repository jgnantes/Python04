def ft_archive_creation(file_name: str) -> None:
    """"""
    try:
        file = open(file_name, 'w')
    except (FileNotFoundError, PermissionError) as e:
        print(f"A {type(e).__name__} occured: '{e}'")
        print(f"The file {file_name} could no be found or accessed")
        return

    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    file.write("[ENTRY 003] Archived by Data Archivist trainee")
    print("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    ft_archive_creation('new_discovery.txt')
