import os
import glob


def delete_log_files(directory='.'):
    log_files = glob.glob(os.path.join(directory, "**/*.log"), recursive=True)

    for log_file in log_files:
        try:
            os.remove(log_file)
        except:
            pass


delete_log_files()
