from langchain_ollama import ChatOllama
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.4
)

def ask(i):
    start = time.time()

    response = llm.invoke(f"Who are you? Request #{i}")

    end = time.time()

    return {
        "request": i,
        "time": round(end - start, 2),
        "answer": response.content
    }

NUM_REQUESTS = 10

start = time.time()

with ThreadPoolExecutor(max_workers=NUM_REQUESTS) as executor:
    futures = [executor.submit(ask, i) for i in range(NUM_REQUESTS)]

    for future in as_completed(futures):
        result = future.result()
        print(f"Request {result['request']} completed in {result['time']} sec")

print(f"\nTotal Time: {round(time.time() - start, 2)} sec")