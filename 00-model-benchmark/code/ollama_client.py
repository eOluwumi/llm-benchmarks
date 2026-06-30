import requests
import time


class OllamaClient:

    def __init__(self, url="http://localhost:11434/api/generate"):
        self.url = url

    def generate(self, model, prompt, temperature=0, num_predict=256):

        start = time.time()

        response = requests.post(
            self.url,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature,
                    "num_predict": num_predict
                }
            }
        )

        latency = time.time() - start

        r = response.json()

        return {
            "response": r.get("response", ""),
            "thinking": r.get("thinking", ""),
            "latency": latency,
            "prompt_tokens": r.get("prompt_eval_count", 0),
            "completion_tokens": r.get("eval_count", 0),
            "prompt_duration": r.get("prompt_eval_duration", 0),
            "eval_duration": r.get("eval_duration", 0),
            "total_duration": r.get("total_duration", 0),
        }