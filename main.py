import os
import shutil
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)23s -  [%(levelname)6s] - %(name)20s: %(message)s')
logger = logging.getLogger(__name__)

# Start timer
start_time = datetime.datetime.now()
logger.info(f'Starting script at {start_time}')

# Paths
SOURCE_DIR = ''
DEST_DIR = ''

# Cutoff date
CUTOFF_DATE = datetime.datetime(2025, 5, 30) #YYYY, MM, DD

# Create list of items that will be moved
items = ''
total_size = 0

# Ensure destination directory exists
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)
    logger.debug(f'Created destination directory: {DEST_DIR}')

# Walk through the source directory and find files to move
for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:
        file_path = os.path.join(root, file)
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        file_size = round(os.path.getsize(file_path) / (1024 * 1024), 2)  # Size in MB

        if file_mtime < CUTOFF_DATE:
            relative_path = os.path.relpath(file_path, SOURCE_DIR)
            items += f'{relative_path}\n{file_mtime}\n{file_size}\n\n'
            total_size += file_size
            logger.debug(f'File to move: {relative_path}, Modified: {file_mtime}, Size: {file_size} MB')

            # Directory the file will be moved to
            backup_path = os.path.join(DEST_DIR, relative_path)

            # Ensure the target directory exists
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)

            # Move the file
            shutil.move(file_path, backup_path)
            logger.info(f'Moved file to: {backup_path}')


# Write items, elapsed time and total size .txt file
end_time = datetime.datetime.now()
elapsed_time = (end_time - start_time).total_seconds()
logger.info(f'Finished script at {end_time}, elapsed time: {elapsed_time} seconds')


items += f'Total size of moved items: {total_size} MB\n'
items += f'Elapsed time: {elapsed_time} seconds\n'
with open('items_to_move.txt', 'w', encoding='UTF8') as f:
    f.write(items)