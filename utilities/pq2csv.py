# Conver a directory of parquet files to CSV

import pandas as pd
from pathlib import Path
import argparse
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-f", "--force", default=False, action='store_true', required=False)

    args = parser.parse_args()

    if Path(args.output).exists() and not args.force:
        print(f'{args.output!r} exists. Will not rewrite unless forced.')
        exit()

    data_dir = Path(args.directory)
    full_df = pd.concat(
        pd.read_parquet(parquet_file)
        for parquet_file in tqdm(data_dir.glob('*.parquet'), desc=f'Processing directory {args.directory}')
    )
    full_df.to_csv(args.output)


if __name__ == "__main__":
    main()
