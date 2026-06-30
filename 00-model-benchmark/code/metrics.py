def tokens_per_second(eval_count, eval_duration):

    if eval_duration == 0:
        return 0

    return eval_count / (eval_duration / 1e9)


def ttft(prompt_duration):

    return prompt_duration / 1e9


def total_time(total_duration):

    return total_duration / 1e9


def throughput(eval_count, total_duration):

    if total_duration == 0:
        return 0

    return eval_count / (total_duration / 1e9)