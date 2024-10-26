import logging

def setup_logging():
    """
    Set up the logging configuration.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
        handlers=[
            logging.FileHandler("app.log"),  # Log to a file
            logging.StreamHandler()  # Also log to console
        ]
    )

# Call the setup_logging function to configure logging
setup_logging()
