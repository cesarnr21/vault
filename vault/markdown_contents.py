"""
Script Parsers Markdown File for all headers and 
rewrittes the file with a Table of Contents that link to the rest of the file.

It looks for the string `[Insert Table of Contents Here]` and will place the ToC there
"""

from pathlib import Path


def main():
    project_path = Path(__file__).parent.parent / 'data/'
    file_name = project_path / 'test.md'

    #file_name = project_path.parent / 'README.md'

    """COMMENT OUT WHEN NOT USING"""
    #file = Path(input('Enter full path for file: '))

    contents, headers, placement = file_parser(file_name)
    generate_table(file_name, contents, headers, placement, '*')


def hdr_cleanup(headers: list, fenced_blocks: list, hdr_point: list) -> list:
    """
    Description
    -----------
    Used to cleanup the header, finds uneccessary `#` characters and removes them

    Parameters
    ----------
    headers: `list`
        - a list that includes all the headers in format [index, header_rank, header_string]
        elements from this lists are being removed, and then gets returned.

    hdr_point: `list`
        - includes a copy of the indexes from headers and is easier to use.
    """
    to_rm = [ ]

    # used to remove `#` characters inside fenced-code blocks
    for i in range(len(fenced_blocks)):
        if i % 2 == 0:
            for x in hdr_point:
                if fenced_blocks[i] <= x <= fenced_blocks[i + 1]:
                    to_rm.append(x)

    # trying to remove other '#' characters
    # for iter in headers:
    #     if (iter[0] not in to_rm) and iter[2][0] != '#':
    #         to_rm.append(headers.index(iter))

    if headers[0][0] == 0:              # remove the main title header
        to_rm.append(0)

    # remove indexes from both `header` and `hdr_point` to keep the indexing between the two consistent
    for i in to_rm:
        where = hdr_point.index(i)
        headers.pop(where)
        hdr_point.pop(where)

    return headers


def file_parser(file_name: str):
    """
    Description
    -----------
    Used to parse a markdown file and store headers. Headers are usually defined using `#` characters
    but these characters are also in other places. calls on `hdr_cleanup()` to remove those cases

    Return
    ------
    contents : `list[str]`
        - includes all of the content from the file. This is due to the fact later in the script,
        writing the file removes all of the content of the file, so it has to be rewritten

    headers: `list`
        - a list that includes all the headers in format `[index, header_rank, header_string]`

    placement: `int`
        - stores the line where the table of contents will be inserted
    """
    with open(file_name, 'r') as file:
        contents = file.readlines()

    headers = [ ]
    hdr_point = [ ]
    fenced_blocks = [ ]

    for i in range(len(contents)):
        if '#' in contents[i]:
            rank = contents[i].count('#')
            hdr_point.append(i)
            headers.append([i, rank, contents[i]])

        if '```' in contents[i]:
            fenced_blocks.append(i)

    try:
        placement = contents.index('[Insert Table of Contents Here]\n')
    except ValueError:
        # here look for similar wording to the string above
        print('insertion string not found')
        exit() # remove this after adding exception handling

    header = hdr_cleanup(headers, fenced_blocks, hdr_point)

    return contents, header, placement


def generate_table(file_name: str, contents: list, headers: list, placement: int, delimeter: str) -> None:
    """
    Description
    -----------
    Creates the Table of Contents and rewrittes the file with the table at the index where the string is placed

    Parameters
    ----------
    contents: `list[str]`
        - due to a python/computing limitation, when writing data to file, it can only be appended at the end
        or all content from the file is overwritten.

    delimeter: `str`
        - character used for bullet points, acceptable characters `['', '-', '*']` default is None. 
    """
    table = f'## Table of Contents\n'
    new_file = [ ]
    ranks = [ ]

    for line in headers:
        ranks.append(line[1])

    max_rank = min(ranks)

    for line in headers:
        hold = line[2].partition((line[1] * '#') + ' ')[2].partition('\n')[0]
        new_line = new_line = hold.lower().replace(' ', '-')
        tab = 4 * ' '
        table = table + ((line[1] - max_rank) * tab) + f'{delimeter} [{hold}](#{new_line})\n'

    table = table + '\n' + (60 * '-') + '\n'
    new_file = contents[:placement]
    new_file.append(table)
    new_file.append(contents[placement + 1:])

    with open(file_name, 'w+') as file:
        for line in new_file:
            file.writelines(line)


if __name__ == '__main__':
    main()
