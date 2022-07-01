import itertools
import random

if __name__ == '__main__':
    with open('data/训练集.txt') as f:
        dataset = []
        tmp = []
        for line in f:
            if line.strip() == "":
                dataset.append(tmp)
                tmp = []
            else:
                tmp.append(line)

    random.shuffle(dataset)
    print(f"total sample: {len(dataset)}")

    val_data = dataset[:len(dataset) // 10]
    train_data = dataset[len(dataset) // 10:]

    with open('./split_datasets/train.txt', 'w') as f:
        for item in train_data:
            item.append("\n")
        train_data = list(itertools.chain(*train_data))
        for line in train_data:
            f.write(line)

    with open('./split_datasets/val.txt', 'w') as f:
        for item in val_data:
            item.append("\n")
        val_data = list(itertools.chain(*val_data))
        for line in val_data:
            f.write(line)
