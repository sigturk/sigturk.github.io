import yaml
import sys
import re


def main():
    with sys.stdin as fin:
        papers = yaml.safe_load(fin)


    print("Accepted papers:\n")

    for paper_dict in papers:
        paper_id = paper_dict["id"]
        title = paper_dict["title"]
        authors = [
            re.sub(
                pattern=r"\s+",
                repl=" ",
                string=f"{author_dict['first_name']} {author_dict.get('middle_name', '')} {author_dict['last_name']}",
            )
            for author_dict in paper_dict["authors"]
        ]
        print(f"{paper_id}. {title}")
        print(", ".join(authors))
        print()


if __name__ == "__main__":
    main()
