import argparse
from page.pexels import Pexels
from page.unsplash import Unsplash


def Option():
    parser = argparse.ArgumentParser(description="Image crawling API with pexels and pixabay.")
    parser.add_argument("--web", type=str, required=True,
                        help="[pexels/unsplash].")
    parser.add_argument("--key", type=str, required=True,
                        help="Your API key from your crawling web.")
    parser.add_argument("--q", type=str, required=True,
                        help="The search query.")
    parser.add_argument("--num_page", type=int, default=1, metavar="NP",
                        help="Number of pages you want requesting.")
    parser.add_argument("--per_page", type=int, default=5, metavar="PP",
                        help="Number of results you are requesting per page.")
    parser.add_argument("--dir", type=str, default="data",
                        help="Directory to save your images")
    return parser


if __name__ == '__main__':
    opt = Option().parse_args()
    if opt.web == "pexels":
        crawler = Pexels(opt)
    else:
        crawler = Unsplash(opt)
    crawler()
    print("Done")
