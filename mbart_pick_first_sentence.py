import sys
import argparse

if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Convert generated texts after segmentation into the format suitable for eval"
    )

    parser.add_argument("infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("outfile", nargs="?", type=argparse.FileType("w"), default=sys.stdout)

    args: argparse.Namespace = parser.parse_args()

    prev_sentence: str = ""
    for l in map(str.strip, args.infile):
        if not prev_sentence and l:
            args.outfile.write(f"{l.strip('# ')}\n")

        prev_sentence = l
