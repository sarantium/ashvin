# Learning Langchain

## 1. Model I/O

![Langchain Model I/O](/docs/assets/model-io.png)

### 1.1 Prompts

![Prompts](/docs/assets/prompts_0.png)

#### 1.1.1 Prompt Templates

![Prompt Templates](/docs/assets/prompts_1.png)

##### 1.1.1.1 Basic Prompt Template

Input :

```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
prompt_template.format(adjective="funny", content="chickens")
```

Output :

```python

"Tell me a funny joke about chickens."
```

##### 1.1.1.2 Chat Prompt Template

![Alt text](/docs/assets/prompts_2.png)
Input

```python

```
