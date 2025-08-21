# File Archiver Script

A Python script to **move files from a source directory to a destination directory based on a modification date cutoff**. It's useful for cleaning up old files and offers an optional dry run mode to preview what would be moved.

-----

## Features

  - Moves files older than a specified cutoff date.
  - Maintains the original directory structure in the destination.
  - Provides a **dry run** mode for testing without moving files.
  - Generates a log of all files that were (or would be) moved, including their sizes and modification dates.
  - Logs the total size of moved files and the elapsed time.
  - Automatically creates destination directories if they don't exist.

-----

## Requirements

  - Python 3.6+
  - Standard Python libraries only (`os`, `shutil`, `datetime`, `logging`).

-----

## Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/file-archiver.git
    cd file-archiver
    ```

2.  **Configure the script:**
    Edit the following variables in `file_archiver.py`:

    ```python
    SOURCE_DIR = 'path/to/source'
    DEST_DIR = 'path/to/destination'
    CUTOFF_DATE = datetime.datetime(2025, 1, 1)  # Format: YYYY, MM, DD
    DRY_RUN = True  # Set to False to actually move files
    ```

      - `SOURCE_DIR`: The directory where files currently reside.
      - `DEST_DIR`: The directory where old files will be moved.
      - `CUTOFF_DATE`: Files modified before this date will be moved.
      - `DRY_RUN`: Set to `True` to test without moving files, `False` to actually move them.

3.  **Run the script:**

    ```bash
    python file_archiver.py
    ```

4.  **Check the output:**

      - `items_to_move.txt` — This file lists the files that were (or would be) moved, their modification dates, file sizes, the total size, and the elapsed time.
      - The console will display logs for progress and warnings.

-----

## Logging

The script uses Python's `logging` module.

  - The default log level is `INFO`.
  - **Dry run mode** will log files that would be moved without performing the move.

### Example Output

```bash
DRY RUN: Would move file /source/file1.txt to /destination/file1.txt
DRY RUN: Would move file /source/folder/file2.txt to /destination/folder/file2.txt
Total size of moved items: 12.45 MB
Elapsed time: 0.05 minutes
```

-----

## License

This project is licensed under the MIT License.
