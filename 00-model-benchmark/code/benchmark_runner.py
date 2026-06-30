def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    RESULTS_DIR = BASE_DIR / "results"
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    output_file = RESULTS_DIR / f"benchmark_{timestamp}.md"

    results = []

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as report:

        report.write("# MODEL BENCHMARK REPORT\n\n")
        report.write(f"Timestamp: {timestamp}\n\n")

        for model in MODELS:

            print("\n" + "="*90)
            print(f"MODEL : {model}")
            print("="*90)

            report.write(
                f"\n# {model}\n\n"
            )

            for bench in BENCHMARKS:

                print(f"Running: {bench['name']}")

                output = run_model(
                    model,
                    bench["prompt"]
                )

                score = score_response(
                    output["response"],
                    bench["expected"]
                )

                row = {
                    "model": model,
                    "benchmark": bench["name"],
                    "category": bench["category"],
                    "score": score,
                    **output
                }

                results.append(row)

                print(
                    f"Latency : {output['latency_sec']} sec"
                )

                print(
                    f"TTFT    : {output['ttft_sec']} sec"
                )

                print(
                    f"TPS     : {output['tokens_per_sec']}"
                )

                print(
                    f"Score   : {score}"
                )

                report.write(
f"""## {bench['name']}

Category : {bench['category']}

Latency : {output['latency_sec']} sec

TTFT : {output['ttft_sec']} sec

Prompt Tokens : {output['prompt_tokens']}

Output Tokens : {output['output_tokens']}

Tokens/sec : {output['tokens_per_sec']}

Score : {score}

### RESPONSE

{output['response']}

"""
                )

                if output["thinking"]:

                    report.write(
f"""
### THINKING

{output['thinking']}

"""
                    )

        import pandas as pd

        df = pd.DataFrame(results)

        csv_file = RESULTS_DIR / f"benchmark_{timestamp}.csv"

        df.to_csv(
            csv_file,
            index=False
        )

        leaderboard = (
            df.groupby("model")
              .agg(
                    avg_score=("score","mean"),
                    avg_latency=("latency_sec","mean"),
                    avg_ttft=("ttft_sec","mean"),
                    avg_tps=("tokens_per_sec","mean"),
                    tests=("benchmark","count")
              )
              .sort_values(
                    "avg_score",
                    ascending=False
              )
        )

        leaderboard_file = RESULTS_DIR / f"leaderboard_{timestamp}.csv"

        leaderboard.to_csv(
            leaderboard_file
        )

    print("\n")
    print("="*90)
    print("BENCHMARK COMPLETE")
    print("="*90)
    print(f"Markdown    : {output_file}")
    print(f"CSV         : {csv_file}")
    print(f"Leaderboard : {leaderboard_file}")