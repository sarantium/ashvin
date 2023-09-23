# Learning Langchain

## 1. Model I/O

![Langchain Model I/O](/docs/assets/model-io.png)

### 1.1 Prompts

![Prompts](/docs/assets/prompts_0.png)

#### 1.1.1 Prompt Templates

![Prompt Templates](/docs/assets/prompts_1.png)

##### 1.1.1.1 Basic Prompt Template

Input :

This is the modern, recommended input

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

Input :

This is an alternative, basic way of generating the Prompt Template and is seen in alot of the older tutorials available online. If you do it this way, then if the input variables don't match the template variables, it will raise an exception.

```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["adjective"],
    template="Tell me a {adjective} joke."
)
```

##### 1.1.1.2 Chat Prompt Template

![Alt text](/docs/assets/prompts_2.png)
Input

```python

```

### 1.2 Language Models
