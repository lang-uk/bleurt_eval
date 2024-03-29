# bleurt_eval

Evaluation of titles generated by Ukrainian model for GPT2 using BLEURT.

## Experiment setup:
 - Results generated by three models (small, medium and large) were evaluated.
 - Files were converted using `python convert_titles.py news_sample.small.out.jsonl reference.small.txt candidate.small.txt`
 - Bleurt installed from master (at commit `cebe7e6f996b40910cfaa520a63db47807e3bf5c`)
 - using BLEURT-20 model
```bash
$ python -m bleurt.score_files   -candidate_file=candidate.small.txt   -reference_file=reference.small.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores.small.txt
$ python -m bleurt.score_files   -candidate_file=candidate.medium.txt   -reference_file=reference.medium.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores.medium.txt
$ python -m bleurt.score_files   -candidate_file=candidate.large.txt   -reference_file=reference.large.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores.large.txt

$ python -m bleurt.score_files   -candidate_file=candidate.mbart.1k.txt   -reference_file=reference.small.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores.mbart.1k.txt
$ python -m bleurt.score_files   -candidate_file=candidate.mbart.5k.txt   -reference_file=reference.small.txt  -bleurt_checkpoint=bleurt/BLEURT-20 -scores_file=scores.mbart.5k.txt
```

Combined files for the review available at `bleurt.eval.small.csv`, `bleurt.eval.medium.csv` and `bleurt.eval.large.csv`.
|        | mean               | median             |
|--------|--------------------|--------------------|
| small  | 0.5432437893003226 | 0.5374010503292084 |
| medium | 0.5675271535292268 | 0.5721611678600311 |
| large  | 0.5906959722489119 | 0.5916261672973633 |
| mbart.1k | 0.7408332733213902 | 0.8061753809452057 |
| mbart.5k | 0.7135102691948414 | 0.7874233424663544 |

 
## bert_score reported on the same data.
bert_score version 0.3.13
two multilang models:
 - xlm-roberta-large, ranked 48
 - bert-base-multilingual-cased, ranked 81
 
 
 ### xlm-roberta-large eval
 ```bash
$ time bert-score -r reference.small.txt -c candidate.small.txt -m xlm-roberta-large
```

`xlm-roberta-large_L17_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.910866 R: 0.903273 F1: 0.906873`

 
```bash
$ time bert-score -r reference.medium.txt -c candidate.medium.txt -m xlm-roberta-large
```
`xlm-roberta-large_L17_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.915702 R: 0.906600 F1: 0.910944`

 ```bash
 $ time bert-score -r reference.large.txt -c candidate.large.txt -m xlm-roberta-large
 ```
 
`xlm-roberta-large_L17_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.916548 R: 0.909308 F1: 0.912751`

```bash
$ time bert-score -r reference.small.txt -c candidate.mbart.1k.txt -m xlm-roberta-large
```

`xlm-roberta-large_L17_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.935879 R: 0.942202 F1: 0.938712`

```bash
$ time bert-score -r reference.small.txt -c candidate.mbart.5k.txt -m xlm-roberta-large
```
`xlm-roberta-large_L17_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.930015 R: 0.935764 F1: 0.932630`


|        | P        | R        | F1       |
|--------|----------|----------|----------|
| small  | 0.910866 | 0.903273 | 0.906873 |
| medium | 0.915702 | 0.906600 | 0.910944 |
| large  | 0.916548 | 0.909308 | 0.912751 |
| mbart.1k  | 0.935879 | 0.942202 | 0.938712 |
| mbart.5k  | 0.930015 | 0.935764 | 0.932630 |


### bert-base-multilingual-cased eval

```bash
$ time bert-score -r reference.small.txt -c candidate.small.txt -m bert-base-multilingual-cased
```
`bert-base-multilingual-cased_L9_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.780336 R: 0.766688 F1: 0.772851`

```bash
$ time bert-score -r reference.medium.txt -c candidate.medium.txt -m bert-base-multilingual-cased
```
`bert-base-multilingual-cased_L9_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.790484 R: 0.775623 F1: 0.782396`


 ```bash
 $ time bert-score -r reference.large.txt -c candidate.large.txt -m bert-base-multilingual-cased
 ```
 
`bert-base-multilingual-cased_L9_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.792963 R: 0.780369 F1: 0.786095`

```bash
$ time bert-score -r reference.small.txt -c candidate.mbart.1k.txt -m bert-base-multilingual-cased
```

`bert-base-multilingual-cased_L9_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.839130 R: 0.863765 F1: 0.850054`

```bash
$ time bert-score -r reference.small.txt -c candidate.mbart.5k.txt -m bert-base-multilingual-cased
```
`bert-base-multilingual-cased_L9_no-idf_version=0.3.12(hug_trans=4.26.1)_fast-tokenizer P: 0.819808 R: 0.847989 F1: 0.832732`
|        | P        | R        | F1       |
|--------|----------|----------|----------|
| small  | 0.780336 | 0.766688 | 0.772851 |
| medium | 0.790484 | 0.775623 | 0.782396 |
| large  | 0.792963 | 0.780369 | 0.786095 |
| mbart.1k  | 0.839130 | 0.863765 | 0.850054 |
| mbart.5k  | 0.819808 | 0.847989 | 0.832732 |
