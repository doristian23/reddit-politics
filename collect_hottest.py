import json
import requests
import argparse

def get_posts1(sub_name):
    data = requests.get(f"http://api.reddit.com/r/{sub_name}/hot?limit=100",
                        headers={'User-Agent': 'windows:requests by (u/dtian2/)'})

    # print(data.content)

    posts = data.json()['data']['children']
    posts = posts[:100]
    name = posts[-1]['data']['name']
    return posts, name


def get_more_posts1(sub_name, after):
    data = requests.get(f"http://api.reddit.com/r/{sub_name}/hot?limit=100&after={after}",
                        headers={'User-Agent': 'windows:requests by (u/dtian2/)'})

    posts = data.json()['data']['children']
    posts = posts[:100]
    name = posts[-1]['data']['name']
    return posts, name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help="output file name", required=True)
    parser.add_argument('subname', help="subreddit name")

    args = parser.parse_args()

    if args.o is not None and args.subname is not None:
        p, last = get_posts1(args.subname)
        p2, last2 = get_more_posts1(args.subname, last)
        p3, last3 = get_more_posts1(args.subname, last2)
        p4, last4 = get_more_posts1(args.subname, last3)
        p5, last5 = get_more_posts1(args.subname, last4)

        ps = [p, p2, p3, p4, p5]

        with open(args.o, 'w') as outfile:
            for line in p:
                json.dump(line, outfile)
                outfile.write('\n')

            for i in range(4):
                for line in ps[i + 1]:
                    json.dump(line, outfile)
                    outfile.write('\n')


if __name__ == "__main__":
    main()