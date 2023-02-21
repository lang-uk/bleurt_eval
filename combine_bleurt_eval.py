# python -m bleurt.score_files   -candidate_file=predicted.txt   -reference_file=expected.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores

import csv

with open("expected.txt", "r") as fp_in_expected:
    with open("predicted.txt", "r") as fp_in_predicted:
        with open("scores", "r") as fp_in_scores:
            with open("combined_bleurt_eval.csv", "w") as fp_out:
                w = csv.DictWriter(fp_out, fieldnames=["reference", "candidate", "bleurt_score"])
                w.writeheader()
                for reference, candidate, bleurt_score in zip(fp_in_expected, fp_in_predicted, fp_in_scores):
                    w.writerow(
                        {
                            "reference": reference.strip(),
                            "candidate": candidate.strip(),
                            "bleurt_score": bleurt_score.strip(),
                        }
                    )
