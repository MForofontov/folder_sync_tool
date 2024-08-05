# folder_sync_tool
# sync_folders

`sync_folders.py` is a Python script designed to synchronize files and folders between a source directory and an output directory at specified intervals. It includes logging functionality to keep track of synchronization activities.

## Requirements

- Python 3.x
- Required Python packages (install via `pip`):
  - `argparse`
  - `os`
  - `time`
  - `shutil`
  - `hashlib`
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

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

[Mykyta Forofontov]
