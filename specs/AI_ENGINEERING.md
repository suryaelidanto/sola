## 1. Type-Safe LLM Interfaces (OpenAI Native)
Raw string outputs are strictly forbidden.
SOLA mandates the use of **OpenAI Structured Outputs** (`client.chat.completions.create` with `response_format` or `.parse`).

### Anti-Pattern
```python
# ❌ Old Way (Instructor) - Third party dependency
import instructor
client = instructor.from_openai(AsyncOpenAI())
```

### ✅ SOLA "Golden Standard"
```python
from pydantic import BaseModel
from openai import AsyncOpenAI

class ExtractionResult(BaseModel):
    entities: list[str]
    confidence: float

client = AsyncOpenAI()

# Native Parsing (Zero-Overhead)
completion = await client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=[...],
    response_format=ExtractionResult,  # <--- Strict Schema Guarantee
)

result = completion.choices[0].message.parsed
print(result.confidence) 
```

---

## 2. Reliability & Retries
LLMs are non-deterministic. Network glitches happen.
SOLA services must implement automatic retries for validation errors.

- **OpenAI Native** ensures JSON validity via `response_format`.
- Retries should be handled via `tenacity` or custom logic if the schema logic itself fails (rare with Structured Outputs).

---

## 3. Security & Injection Defense
Never trust user input directly in a prompt.
- Use **Prompt Templates** (Jinja2 or f-strings) strictly.
- Treat all user input as untrusted.
- (Optional) Use a "Prompt Firewall" before processing heavy tasks.

---

## 4. Evaluation-Driven Development (EDD)
Don't just verify manually.
Every AI feature must have a corresponding test in `tests/evals/`.

### The Metric Triad
1.  **Faithfulness**: Does the answer come from the context?
2.  **Answer Relevancy**: Did we answer what was asked?
3.  **JSON Compliance**: Is the output structure valid? (Handled by Pydantic)
