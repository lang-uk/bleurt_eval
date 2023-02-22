import argparse
import json

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Convert JSONL with original and generated titles into the format suitable for BLEURT and bert_score eval"
    )

    parser.add_argument("infile", type=argparse.FileType("r"), help="Input jsonl file")
    parser.add_argument("out_reference", type=argparse.FileType("w"), help="Output file with original titles")
    parser.add_argument("out_candidate", type=argparse.FileType("w"), help="Output file with candidate titles")

    args: argparse.Namespace = parser.parse_args()

    for article in map(json.loads, args.infile):
        args.out_reference.write(article["title"].replace("\n", " ").strip() + "\n")
        predicted = article["generated_title"].replace("\n", " ").strip()
        if " рік: " in predicted:
            predicted, _ = predicted.split(" рік: ", 1)

        if " мітки: " in predicted:
            predicted, _ = predicted.split(" мітки: ", 1)

        args.out_candidate.write(predicted.strip() + "\n")
