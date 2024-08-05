# folder_sync_tool
# sync_folders

`sync_folders.py` is a Python script designed to synchronize files and folders between a source directory and an output directory at specified intervals. It includes logging functionality to keep track of synchronization activities.

## Requirements

- Python 3.x
- Required Python packages (install via `pip`):
  - `argparse`
  - `os`
  - `time`
  - `logging`

## Usage

To run the script, use the following command:

```bash
python sync_folders.py [options]
```

### Options

The script accepts the following options:

- `-s`, `--source-directory`: Source directory containing the files and folders to be synchronized. This is a required argument.
- `-o`, `--output-directory`: Output directory to store the synchronized files. This is a required argument.
- `-l`, `--log-file-path`: Path to store the log file. This is a required argument.
- `-t`, `--time-to-sync`: Time interval to synchronize the files (in seconds). This is an optional argument with a default value of `86400` seconds (24 hours).

### Example

To synchronize files from `/path/to/source` to `/path/to/output` and log activities to `/path/to/logfile.log` every 24 hours:

```bash
python sync_folders.py -s /path/to/source -o /path/to/output -l /path/to/logfile.log
```

## Functions

### [`parse_arguments()`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fummi%2FDocuments%2Fgithub%2Fsync_tool%2Fsync_folders.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A157%2C%22character%22%3A4%7D%5D "sync_folders.py")

Parses command-line arguments and returns them.

### [`main(source_directory, output_directory, log_file_path, time_to_sync)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fummi%2FDocuments%2Fgithub%2Fsync_tool%2Fsync_folders.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A142%2C%22character%22%3A4%7D%5D "sync_folders.py")

Main function that sets up logging, synchronizes directories, and sleeps for the specified time interval.

### [`valid_directory(path)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fummi%2FDocuments%2Fgithub%2Fsync_tool%2Fsync_folders.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A10%2C%22character%22%3A4%7D%5D "sync_folders.py")

Checks if the provided path is a valid directory.

### [`valid_log_file_path(path)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fummi%2FDocuments%2Fgithub%2Fsync_tool%2Fsync_folders.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A34%2C%22character%22%3A4%7D%5D "sync_folders.py")

Checks if the directory for the provided log file path exists, and creates it if necessary.

## Logging

The script logs synchronization activities to the specified log file. Ensure that the directory for the log file exists or can be created.

## Synchronization

The script uses the [`sync_directories`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2Fummi%2FDocuments%2Fgithub%2Fsync_tool%2Fsync_folders.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A81%2C%22character%22%3A4%7D%5D "sync_folders.py") function to synchronize files and folders from the source directory to the output directory. After synchronization, it logs the completion message and sleeps for the specified time interval before the next synchronization cycle.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

[Mykyta Forofontov]
