def ft_vault_security(file_name: str, lines: list) -> None:
    """"""
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    with open(file_name, 'w') as file:
        for line in lines:
            try:
                file.write(line)
            except Exception as e:
                print(f"A {type(e).__name__} occured: {e}")
                print(f"'{line}' could not be written in {file_name}\n")

    with open(file_name, 'r') as file:
        text = file.read()
        print(text)

    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_name = "file.txt"
    lines: list = [
        "SECURE EXTRACTION:\n",
        "[CLASSIFIED] Quantum encryption keys recovered\n",
        "[CLASSIFIED] Archive integrity: 100%\n\n",
        42,
        "SECURE PRESERVATION:\n",
        "[CLASSIFIED] New security protocols archived\n"
    ]
    ft_vault_security(file_name, lines)
