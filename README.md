# img-to-chars
Convert an img to a character image!

An example can be found in the `imgs`, where [this image](https://book-of-mario.fandom.com/wiki/Darkness?file=Darkness.png) was converted to text.

## Install

Do:

```bash
pip install -r requirements.txt
```

## Run

To run an image, do:

```
python3 index.py --file_path=<FILE_PATH> --output_file_path=<OUTPUT_FILE_PATH>
```

where:
- `file_path` is the path to the image to convert to a `.txt`-file.
- `output_file_path` is the path to the output `.txt`-file.

If your image is too granular, you can reduce the granularity through the `--size_reduction` argument. If you want to reduce the number of pixels in half, set it to `2` etc.

## Some additional notes

This is not fully tested yet! If you try to use it and it does not work, please submit an issue so I can improve it!
