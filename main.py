import os
import shutil
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)23s -  [%(levelname)6s] - %(name)20s: %(message)s')
logger = logging.getLogger(__name__)

# REAL RUN OR DRY RUN
DRY_RUN = True  # Set to True for dry run, False for actual move
if DRY_RUN:
    logger.warning('Running in DRY RUN mode. No files will be moved.')

# Start timer
start_time = datetime.datetime.now()
logger.info(f'Starting script at {start_time}')

# Paths
SOURCE_DIR = '//zeus/PrzekierowaneFoldery$/a.jakubczak/Desktop/Adam workfolder/ISO'
DEST_DIR = '//zeus/PrzekierowaneFoldery$/a.jakubczak/Desktop/Adam workfolder/backup'

# Cutoff date
CUTOFF_DATE = datetime.datetime(2025, 1, 1) #YYYY, MM, DD

# Create list of items that will be moved
items = ''
total_size = 0

# Ensure destination directory exists
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)
    logger.info(f'Created destination directory: {DEST_DIR}')

# Walk through the source directory and find files to move
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        file_size = round(os.path.getsize(file_path) / (1024 * 1024), 2)  # Size in MB

        if file_mtime < CUTOFF_DATE:
            relative_path = os.path.relpath(file_path, SOURCE_DIR)
            total_size += file_size
            logger.debug(f'File to move: {relative_path}, Modified: {file_mtime}, Size: {file_size} MB')

            # Directory the file will be moved to
            backup_path = os.path.join(DEST_DIR, relative_path)
            items += f'{backup_path}\n{file_mtime}\n{file_size}\n\n'

            # Move the file
            if DRY_RUN:
                logger.info(f'DRY RUN: Would move file {file_path} to {backup_path}')
            else:
                os.makedirs(os.path.dirname(backup_path), exist_ok=True)
                shutil.move(file_path, backup_path)
                logger.info(f'Moving file: {file_path} to {backup_path}')

# Write items, elapsed time and total size .txt file
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds() / 60  # Convert to minutes
logger.info(f'Finished script at {end_time}, elapsed time: {elapsed_time} minutes')

items += f'Total size of moved items: {total_size} MB\n'
items += f'Elapsed time: {elapsed_time} minutes\n'
with open('items_to_move.txt', 'w', encoding='UTF8') as f:
    f.write(items)