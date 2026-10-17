
# Zombie and Orphan Process Detection System

## Overview
A Linux-based project that identifies zombie processes
and demonstrates orphan-process behavior.

## Features
- Scans Linux processes through `/proc`.
- Identifies zombie processes using state Z.
- Demonstrates orphaning with a controlled parent-child test.
- Provides a command-line menu.
- Includes automated unit tests.

## Requirements
- Linux or a compatible Unix environment
- Python 3
- No external Python packages required

## Run the Application
From the project root:

```bash
python3 src/main.py
```

## Run the Orphan Test
Choose option 2 from the application menu.

## Run Automated Tests

```bash
python3 -m unittest discover -s tests -v
```

## Limitations
A process snapshot cannot reliably establish whether a process
was orphaned in the past. The orphan test demonstrates this
behavior by creating a child whose parent exits.

## Safety
The application monitors process information and does not
terminate system processes.
