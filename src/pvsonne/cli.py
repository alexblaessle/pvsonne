from pvsonne.api import PVSonne
import click
import pandas as pd
import logging
import time

@click.command()
@click.option("-n", "--ncalls", default=1, help="Number of calls.")
@click.option("-w", "--wait", default=1, help="Wait between tests seconds.")
@click.option("-o", "--out", default="sonnen_results.csv", help="Output file.")
@click.option("-l", "--logging_level", default=20, help="Logging level.")
# @click.option("-i", "--inf", default=0, help="Run infinitely.")
def run(ncalls, wait, out, logging_level):

    # Set logging level
    logging.getLogger().setLevel(logging_level)
    sb2=PVSonne()
    data=[]
    for curr in range(ncalls):
        logging.info(f"{curr+1}/{ncalls}: Calling API.")
        data.append(sb2.get_latest_data())
        time.sleep(wait)
    pd.DataFrame(data).to_csv(out)
    


if __name__ == "__main__":
    run()
