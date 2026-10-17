#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys

PROC = Path("/proc")


def get_processes():
    processes = {}

    for entry in PROC.iterdir():
        if not entry.name.isdigit():
            continue

        try:
            stat = (entry / "stat").read_text()
            left = stat.find("(")
            right = stat.rfind(")")

            processes[int(entry.name)] = {
                "pid": int(entry.name),
                "name": stat[left + 1:right],
                "state": stat[right + 2:].split()[0],
                "ppid": int(stat[right + 2:].split()[1]),
            }
        except (OSError, ValueError, IndexError):
            continue

    return processes


def scan_zombies():
    processes = get_processes()
    zombies = [p for p in processes.values() if p["state"] == "Z"]

    print(f"\nProcesses scanned: {len(processes)}")
    print("\nZOMBIE PROCESSES")
    print("-" * 65)

    if not zombies:
        print("No matching processes found.")
    else:
        print(f"{'PID':<10}{'PPID':<10}{'STATE':<10}NAME")
        for p in zombies:
            print(
                f"{p['pid']:<10}{p['ppid']:<10}"
                f"{p['state']:<10}{p['name']}"
            )


def test_orphan():
    print("\nStarting controlled orphan-process test...\n")
    try:
        subprocess.run(
            [sys.executable, "src/process_test.py"],
            timeout=10,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print("The test timed out.")


def main():
    while True:
        print("\n" + "=" * 65)
        print(" ZOMBIE AND ORPHAN PROCESS DETECTION SYSTEM")
        print("=" * 65)
        print("1. Scan for zombie processes")
        print("2. Run orphan-process test")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            scan_zombies()
        elif choice == "2":
            test_orphan()
        elif choice == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
