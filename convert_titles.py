import json

with open("expected.txt", "w") as fp_out_expected:
    with open("predicted.txt", "w") as fp_out_predicted:
        with open("out_topk=1.jsonl", "r") as fp_in:
            for article in map(json.loads, fp_in):
                fp_out_expected.write(article["title"].replace("\n", " ").strip() + "\n")
                predicted = article["generated_title"].replace("\n", " ").strip()
                if " рік: " in predicted:
                    predicted, _ = predicted.split(" рік: ", 1)

                if " мітки: " in predicted:
                    predicted, _ = predicted.split(" мітки: ", 1)

                fp_out_predicted.write(predicted.strip() + "\n")
