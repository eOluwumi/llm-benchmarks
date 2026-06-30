# Model Benchmark Framework

## Purpose

This framework provides a reproducible benchmarking pipeline for evaluating local
LLMs served through Ollama.

The goal is to compare models on:

- Accuracy
- Latency
- Time-to-first-token (TTFT)
- Throughput (tokens/sec)
- CPU utilization
- GPU utilization (future)
- Memory usage
- Cost efficiency

---

## Supported Backends

- Ollama
- Azure OpenAI (future)
- Azure AI Foundry (future)
- vLLM (future)

---

## Directory Layout

benchmarks/
    Benchmark definitions

code/
    Benchmark execution engine

config/
    Models, hardware and runtime configuration

infra/
    CPU/GPU instrumentation

results/
    Benchmark outputs

notebooks/
    Experimental analyses

---

## Run

python code/benchmark_runner.py

---

## Outputs

benchmark_results.csv

leaderboard.csv

benchmark_notes.md

---

## Future Work

- GPU benchmarking
- RAG benchmarks
- Long-context evaluation
- Agent benchmarks
- Code generation benchmarks
