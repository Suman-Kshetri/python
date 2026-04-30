import pandas as pd # type: ignore

input_file = 'data.csv'
output_file = 'processed_data.csv'
first_chunk = True

for chunk in pd.read_csv(input_file, chunksize=1000):
    # Process each chunk here
    print(chunk.head())
    chunk.to_csv(
        output_file,
        mode='w' if first_chunk else 'a',
        header=first_chunk,
        index=False
    )
    first_chunk = False
