def ft_crisis_response(file_name: str) -> None:
    """Tries to access a file and, if successful, prints its content"""
    try:
        with open(file_name, 'r') as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            text: str = file.read()
            print(f"SUCCESS: Archive recovered - '{text}'")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print(f"RESPONSE: A {type(e).__name__} occured")
        print(f"{e}")
        print("STATUS: Crisis handled, security maintained\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    ft_crisis_response('lost_archive.txt')
    ft_crisis_response('classified_data.txt')
    ft_crisis_response('standard_archive.txt')
    print("All crisis scenarios handled successfully. Archives secure.")
