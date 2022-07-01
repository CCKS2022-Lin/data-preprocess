import re
import torch
from tqdm import tqdm
import pickle
import argparse
from transformers import AutoTokenizer, AutoModel


def read_dataset(p):
    with open(p) as f:
        cnt = 0
        dropped = 0
        doc = {}
        for line in f:
            if line.strip() == '':
                cnt = 0
                if doc["q"] is not None and doc["rel"] is not None:
                    yield doc
                else:
                    dropped += 1
                doc = {}
            else:
                cnt += 1
                if cnt == 1:
                    doc["q"] = line.strip().split(':')[1]
                if cnt == 2:
                    if line.count('.') > 1:
                        doc["rel"] = None
                    else:
                        rel = re.match(r".*\{\s*(\?\w|<.*>|\".*\")\s*(\?\w|<.*>|\".*\")\s*(\?\w|<.*>|\".*\").*}.*",
                                       line).group(2)
                        if len(rel) > 2:
                            doc["rel"] = rel[1:-1]
                            # print(line.strip())
                        else:
                            doc["rel"] = None
                if cnt == 3:
                    ans = line.strip().split("\t")[0]
                    if ans.startswith("\"") or ans.startswith("<"):
                        doc["ans"] = ans[1:-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Encode dataset.")
    parser.add_argument("file", type=str, help="path the the input dataset file")
    args = parser.parse_args()
    print(f"parsing file {args.file}")
    path_frag = args.file.split(".")
    path_frag[-1] = "bin"
    output_path = ".".join(path_frag)
    print(f"writing output to {output_path}")

    pretrained_model = "hfl/chinese-roberta-wwm-ext"
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model)
    encoder = AutoModel.from_pretrained(pretrained_model)

    dataset = list(read_dataset(args.file))

    with torch.no_grad():
        for item in tqdm(dataset):
            tokens = tokenizer(item["q"], return_tensors="pt")
            encoded_input = encoder(**tokens).last_hidden_state[:, 1, :]
            item["input"] = encoded_input.view(-1).tolist()

    with open(output_path, "wb") as f:
        pickle.dump(dataset, f)
