import json
import argparse
from datetime import datetime, timezone


def change_title(post):
    keys = post.keys()
    if "title_text" in keys:
        post["title"] = post.pop("title_text")
        return post
    elif "title" in keys:
        return post
    else:
        return None


def std_time(post):
    keys = post.keys()
    if "createdAt" in keys:
        time = post['createdAt']
        dt = 0
        try:
            dt = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
        except:
            # print(dt)
            return None
        new_dt = datetime.fromtimestamp(dt.timestamp(), tz=timezone.utc)
        post['createdAt'] = new_dt.strftime('%Y-%m-%dT%H:%M:%S%z')
        return post
    else:
        return post


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help="input file name")
    parser.add_argument('-o', help="output file name")

    args = parser.parse_args()
    if args.i is not None and args.o is not None:
        out = []
        with open(args.i, 'r') as f1:
            for line in f1:
                try:
                    data = json.loads(line)
                except:
                    # print(data)
                    continue
                npost = change_title(data)
                if npost is not None:
                    nnpost = std_time(npost)
                    if nnpost is not None:
                        out.append(nnpost)

        with open(args.o, 'w') as outfile:
            for d in out:
                json.dump(d, outfile)
                outfile.write("\n")


if __name__ == "__main__":
    main()
