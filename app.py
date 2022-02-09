import logging

# configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s"
)


def init():
    while True:
        try:
            logging.info("Running...")
        except:
            logging.exception("Error")


#
if __name__ == '__main__':
    logging.info("Starting...")
    init()
