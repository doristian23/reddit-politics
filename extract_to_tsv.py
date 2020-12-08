import json
import random
import csv
import argparse


def get_random_posts(in_f, n):
    posts = []
    with open(in_f) as f:
        posts.append(['Name', 'title', 'coding'])
        lines = f.readlines()
        rand_lines = random.sample(lines, k=n)
        for i in rand_lines:
            i = json.loads(i)
            posts.append([i['data']['name'], i['data']['title'], ''])

        #print(len(posts))
        #print(random.choices(posts, k=n))

    return posts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help="outfile name", required=True)
    parser.add_argument('json_file', help="json file name")
    parser.add_argument('num_posts_to_output', help="number of posts to output")

    args = parser.parse_args()

    num = 0
    try:
        num = int(args.num_posts_to_output)
    except:
        print("num_posts_to_output must be a number")
        return

    posts = get_random_posts(args.json_file, num)

    with open(args.o, 'w', newline="") as outfile:
        wr = csv.writer(outfile, delimiter='\t')
        for line in posts:
            wr.writerow(line)


if __name__ == "__main__":
    main()




