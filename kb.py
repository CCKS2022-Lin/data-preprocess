from pymongo import MongoClient


def import_data():
    with open('data/triple.txt', 'r') as f:
        for line in f:
            try:
                sub, rel, obj = line.split('\t')
                sub = sub[1:-1]
                rel = rel[1:-1]
                obj = obj[1:-4]

                yield {
                    "subject": sub,
                    "relation": rel,
                    "object": obj
                }
            except Exception:
                pass


if __name__ == '__main__':
    URL = "mongodb://localhost:27017"
    client = MongoClient(URL)

    db = client["ccks"]
    collection = db["triple"]

    tmp = []
    cnt = 0
    for triple in import_data():
        tmp.append(triple)

        if len(tmp) == 5000:
            print(f"inserted: {cnt * 5000}")
            cnt += 1
            collection.insert_many(tmp)
            tmp = []

    if len(tmp) > 0:
        collection.insert_many(tmp)

    print("creating indices...")
    collection.create_index("subject")
    collection.create_index("object")
