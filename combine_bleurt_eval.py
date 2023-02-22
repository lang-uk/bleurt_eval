import csv
import argparse
from typing import List
from statistics import mean, median

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Convert JSONL with original and generated titles into the format suitable for BLEURT and bert_score eval"
    )

    parser.add_argument("in_reference", type=argparse.FileType("r"), help="Input file with reference sentences")
    parser.add_argument("in_candidate", type=argparse.FileType("r"), help="Input file with candidate sentences")
    parser.add_argument("in_scores", type=argparse.FileType("r"), help="Input file with scores")
    parser.add_argument("out_combined", type=argparse.FileType("w"), help="Combined output csv file")

    args: argparse.Namespace = parser.parse_args()
    scores: List[float] = []

    w = csv.DictWriter(args.out_combined, fieldnames=["reference", "candidate", "bleurt_score"])
    w.writeheader()
    for reference, candidate, bleurt_score in zip(args.in_reference, args.in_candidate, args.in_scores):
        score = float(bleurt_score.strip())
        scores.append(score)
        w.writerow(
            {
                "reference": reference.strip(),
                "candidate": candidate.strip(),
                "bleurt_score": score,
            }
        )

    print(f"Samples {len(scores)}, mean: {mean(scores)}, median: {median(scores)}")
