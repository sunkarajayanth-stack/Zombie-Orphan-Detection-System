#!/usr/bin/env python3

import os
import sys
import time


def main():
    if not hasattr(os, "fork"):
        print("This test requires a Unix/Linux environment.")
        sys.exit(1)

    child_pid = os.fork()

    if child_pid == 0:
        # Child process
        original_ppid = os.getppid()

        print(f"[CHILD] PID: {os.getpid()}", flush=True)
        print(f"[CHILD] Initial PPID: {original_ppid}", flush=True)

        # Allow the parent to exit.
        time.sleep(2)

        current_ppid = os.getppid()
        print(f"[CHILD] Current PPID: {current_ppid}", flush=True)

        if current_ppid != original_ppid:
            print("[RESULT] Child was reparented: orphan confirmed.")
        else:
            print(
                "[RESULT] Parent ID has not changed yet. "
                "Check the environment and retry."
            )

        sys.exit(0)

    else:
        # Parent process
        print(f"[PARENT] PID: {os.getpid()}", flush=True)
        print(f"[PARENT] Created child PID: {child_pid}", flush=True)
        print("[PARENT] Exiting now.", flush=True)

        # Exit without waiting for the child.
        os._exit(0)


if __name__ == "__main__":
    main()
