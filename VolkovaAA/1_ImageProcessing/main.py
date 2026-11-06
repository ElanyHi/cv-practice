import argparse
import sys
import logging
import cv2
from image_processing import ImageFilter
from utils import read_image

logging.basicConfig(level=logging.INFO, format='[ %(levelname)s ] %(message)s')
logger = logging.getLogger()

def parse_params(param_str: str) -> dict:
    params = {}
    if not param_str:
        return params

    for item in param_str.split(','):
        if '=' in item:
            key, val = item.split('=', 1)
            key = key.strip()
            val = val.strip()
            try:
                params[key] = float(val)
            except ValueError:
                params[key] = val
    return params

def cli_argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--image',
                        help='image',
                        type=str,
                        required=True,
                        dest='image_path')
    parser.add_argument('-o', '--output',
                        help='output',
                        default = "result.png",
                        type=str,
                        required=True)
    parser.add_argument('-f', '--filter',
                        help='filter',
                        default = "grayscale",
                        type=str,
                        required=True)
    parser.add_argument('-p', '--params',
                        help='params',
                        type=str,
                        default="")
    
    args = parser.parse_args()

    return args


def main():
    args = cli_argument_parser()
    try:
        image = read_image(args.image_path)
        
        params_dict = args.__dict__.copy()
        params_dict.update(parse_params(args.params))
        
        filter_processing = ImageFilter.get_filter(image, params_dict)
        result = filter_processing.apply_filter()
        cv2.imwrite(args.output, result)
    except Exception as ex:
        logger.error((f'{str(ex)}'))
        return 1
    return 0


if __name__=='__main__':
    sys.exit(main() or 0)