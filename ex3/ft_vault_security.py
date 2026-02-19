def ft_vault_security(file_name: str, txt_lines: list) -> None:
    """Safely creates a file, fills it with content
    prints it on the standrd output and closes the file"""
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    with open(file_name, 'w') as file:
        for line in txt_lines:
            try:
                file.write(line)
            except Exception as e:
                print(f"A {type(e).__name__} occured: {e}")
                print(f"'{line}' could not be written in {file_name}", end=' ')
                print("but the program continues!\n")

    with open(file_name, 'r') as file:
        text = file.read()
        print(text)

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_name = "file.txt"
    txt_lines: list = [
        "SECURE EXTRACTION:\n",
        "[CLASSIFIED] Quantum encryption keys recovered\n",
        "[CLASSIFIED] Archive integrity: 100%\n\n",
        42,
        "SECURE PRESERVATION:\n",
        open("security_protocols.txt", 'r').read()
    ]
    ft_vault_security(file_name, txt_lines)
