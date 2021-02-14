import numpy as np
import matplotlib.image as mpimg
import torch.nn as nn
import torch
import argparse

CHARS = " .,-~:;=!*#$@"[::-1]


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def convert_image_to_text(
    file_path: str, output_file_path: str = None, size_reduction: float = 1.0
):
    img = mpimg.imread(file_path)
    data = rgb2gray(img)
    data_scaled = (data - data.min()) / (data.max() - data.min())
    scaled = nn.AvgPool2d(
        kernel_size=(int(size_reduction * 2), int(size_reduction)),
        stride=(int(size_reduction * 2), int(size_reduction)),
    )(torch.Tensor(data_scaled).reshape(1, data.shape[0], data.shape[1])).numpy()[0]
    text_arr = ""

    limits = (1 / len(CHARS)) * (np.arange(len(CHARS)) + 1)

    for arr in scaled:
        app_ = []
        for pixel in arr:
            app_.append(CHARS[np.where(limits == limits[pixel <= limits][0])[0][0]])
        text_arr += "".join(app_) + "\n"

    print(text_arr)
    if output_file_path is not None:
        with open(output_file_path, "w") as f:
            f.write(text_arr)


parser = argparse.ArgumentParser()

parser.add_argument("--file_path", type=str, help="Path to the image to convert. ")

parser.add_argument(
    "--output_file_path",
    type=str,
    default=None,
    help="The output path for the file. Default to the name of the file. ",
)

parser.add_argument(
    "--size_reduction",
    type=float,
    default=1.0,
    help="Retrieve a more granular representation of the data through average poolings. ",
)

args = parser.parse_args()

if __name__ == "__main__":
    convert_image_to_text(
        file_path=args.file_path,
        output_file_path=args.output_file_path,
        size_reduction=args.size_reduction,
    )
