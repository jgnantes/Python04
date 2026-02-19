import sys


def ft_stream_management() -> None:
    """Collects archivist input and demonstrates proper
    separation of standard and alert communication streams."""
    id: str = input("Input Stream active. Enter archivist ID: ")
    report: str = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {id}: {report}")
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
        )
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    ft_stream_management()
