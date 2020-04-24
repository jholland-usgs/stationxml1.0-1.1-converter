import argparse
import glob
import os

from lxml import etree


def parseargs():
    """
    Parse commandline arguments

    Returns
    -------
    args parsed from input
    """
    parser = argparse.ArgumentParser(prog="xslt_converter.py")
    parser.add_argument("xslt",
                        help="The xslt file to convert input to output with")

    parser.add_argument("input",
                        help="Either the directory or file to be converted. Wildcards are permitted. This does restrict to .xml if directory provided.")

    parser.add_argument("output",
                        help="The directory to output converted xml files into")

    parser.add_argument("-f", "--force_completion", help="Force completion despite failures", action='store_true')

    args = parser.parse_args()
    return args


def convert_single_file(transform, input_file_path, output_dir):
    """
    Convert a single file with provided transform and write it out to the output_dir with the same basename.
    Parameters
    ----------
    transform etree.XSLT produced transform
    input_file_path str Path to the input file
    output_dir str Path to the output directory This will overwrite on conflicting names.

    Returns
    -------

    """
    with open(input_file_path, 'r') as input_file:
        xml_in = etree.parse(input_file)
        xml_out = transform(xml_in)
        file_out = open(os.path.join(output_dir, os.path.basename(input_file_path)), 'wb')
        file_out.write(etree.tostring(xml_out, pretty_print=True, xml_declaration=True, encoding='UTF-8))


def convert_from_paths(xslt, input, output, force_completion=False):
    """
    Convert all files in either a directory or a wildcard path matching glob. Output is written to a directory with a matching filename
    Parameters
    ----------
    xslt str Path to XSLT transform file
    input str Path to either a directory or wildcardable file path
    output str Path to output directory
    force_completion bool Upon exception, continue conversions.

    Returns
    -------

    """
    try:
        xslt_file = open(xslt, 'r')
        xslt_parsed =etree.parse(xslt_file)
        transform = etree.XSLT(xslt_parsed)
    except Exception as e:
        print("Error parsing XSLT file: {}".format(xslt))
        print(str(e))
        return

    try:
        if os.path.isdir(input):
            input = input + '/*.xml'
        input_paths = glob.iglob(input)
    except Exception as e:
        print("Error processing input path(s)")
        print(str(e))
        return

    try:
        if not os.path.isdir(output):
            print("Output must be a directory")
            return
    except Exception as e:
        print("Error processing output folder")
        print(str(e))
        return

    for file in input_paths:
        try:
            convert_single_file(transform, file, output)
        except Exception as e:
            print("Error converting file: {}".format(file))
            print(str(e))
            if force_completion:
                continue
            else:
                return


def main():
    args = parseargs()
    convert_from_paths(**vars(args))


if __name__ == "__main__":
    main()

