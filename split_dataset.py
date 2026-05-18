import splitfolders

input_folder = "raw_dataset"
output_folder = "datatest"

splitfolders.ratio(
  input=input_folder,
  output=output_folder,
  seed=42,
  ratio=(0.7, 0.2, 0.1)
)