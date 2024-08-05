#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import shutil
import hashlib
import argparse
import logging

def valid_directory(path):
    """
    Check if the provided path is a valid directory.

    Parameters
    ----------
    path : str
        The path to be checked.

    Returns
    -------
    str
        The original path if it is a valid directory.

    Raises
    ------
    argparse.ArgumentTypeError
        If the path is not a valid directory.
    """
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory")

def valid_log_file_path(path):
    """
    Check if the directory for the provided log file path exists, and create it if necessary.

    Parameters
    ----------
    path : str
        The log file path to be checked.

    Returns
    -------
    str
        The original path if the directory is valid.

    Raises
    ------
    argparse.ArgumentTypeError
        If the directory for the log file path is not valid and cannot be created.
    """
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            raise argparse.ArgumentTypeError(f"Cannot create directory '{directory}': {e}")
    return path

def calculate_md5(file_path):
    """
    Calculate the MD5 checksum of a file.

    Parameters
    ----------
    file_path : str
        The path to the file for which the MD5 checksum is to be calculated.

    Returns
    -------
    str
        The MD5 checksum of the file as a hexadecimal string.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sync_directories(source_directory, output_directory):
    """
    Synchronize the contents of the source directory with the output directory.

    Parameters
    ----------
    source_directory : str
        The path to the source directory.
    output_directory : str
        The path to the output directory.

    Notes
    -----
    - This function will delete items in the output directory that are not present in the source directory.
    - It will copy files from the source directory to the output directory if they do not exist or if they differ.
    - Directories are created in the output directory if they exist in the source directory but not in the output directory.
    - It will recursively synchronize the contents of the directories.
    - The synchronization is based on the MD5 checksum of the files.
    - It will log the actions taken during synchronization.

    Returns
    -------
    None
    """

    source_items = {item_name: os.path.join(source_directory, item_name) for item_name in os.listdir(source_directory)}
    output_items = {item_name: os.path.join(output_directory, item_name) for item_name in os.listdir(output_directory)}

    # Delete items in output that are not in source
    for item in output_items:
        if item not in source_items:
            output_item = output_items[item]
            if os.path.isdir(output_item):
                shutil.rmtree(output_item)
                logging.info(f'Deleting directory {output_item}')
            else:
                os.remove(output_item)
                logging.info(f'Deleting file {output_item}')

    for item_name, source_item_path in source_items.items():
        output_item = os.path.join(output_directory, item_name)
        # Process directories
        if os.path.isdir(source_item_path):
            # Create the directory in the output directory if it does not exist
            if not os.path.exists(output_item):
                os.mkdir(output_item)
                logging.info(f'Creating directory {output_item}')
            # Recursively synchronize the directories
            sync_directories(source_item_path, output_item)
        # Synchronize everything else, including files, symlinks etc.    
        else:
            if not os.path.exists(output_item):
                shutil.copy2(source_item_path, output_item)
                logging.info(f'Copying file {source_item_path} to {output_item}')
            else:
                source_md5 = calculate_md5(source_item_path)
                output_md5 = calculate_md5(output_item)
                if source_md5 != output_md5:
                    shutil.copy2(source_item_path, output_item)
                    logging.info(f'Copying file {source_item_path} to {output_item}')

def main(source_directory, output_directory, log_file_path, time_to_sync):

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_file_path), logging.StreamHandler()])
    
    # Infinite loop to sync the directories
    while True:
        logging.info("Starting synchronization...")
        # Synchronize the directories
        sync_directories(source_directory, output_directory)
        logging.info(f"Synchronization complete. Sleeping for {time_to_sync} seconds...")
        # Sleep for the specified time
        time.sleep(time_to_sync)

def parse_arguments():

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-s', '--source-directory',
                        type=valid_directory,
                        required=True,
                        dest='source_directory',
                        help='Source directory containing the files and folders to be synchronized.')

    parser.add_argument('-o', '--output-directory',
                        type=valid_directory,
                        required=True, dest='output_directory',
                        help='Output directory to store the sync files.')
    
    parser.add_argument('-l', '--log-file-path',
                        type=valid_log_file_path,
                        required=True,
                        dest='log_file_path',
                        help='Path to store the log file.')

    parser.add_argument('-t', '--time-to-sync',
                        type=int,
                        required=False,
                        default=86400,
                        dest='time_to_sync',
                        help='Time to synchronize the files (seconds).')

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_arguments()
    main(**vars(args))