def keyword_score(response, expected):

    response = response.lower()

    matches = 0

    for item in expected:

        if item.lower() in response:
            matches += 1

    return matches / len(expected)


def exact_match(response, expected):

    return response.strip() == expected.strip()


def contains_all(response, expected):

    response = response.lower()

    return all(
        x.lower() in response
        for x in expected
    )