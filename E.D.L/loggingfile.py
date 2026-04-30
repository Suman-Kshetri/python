import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", filename="E.D.L/calculationLog.log",filemode="a")

def calculate_total(price, tax_rate):
    logging.debug(f"price = {price}, tax_rate = {tax_rate}")
    total = price + (price + tax_rate)
    logging.debug(f"total = {total}")
    return total

calculate_total(100, 0.1)

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="E.D.L/appfile.log",
    filemode="a"
)

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")