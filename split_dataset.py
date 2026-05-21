import splitfolders

input_folder = "brain_tumor_dataset"
output_folder = "dataset"

splitfolders.ratio(
  input=input_folder,
  output=output_folder,
  seed=32,
  ratio=(0.7, 0.2, 0.1)
)