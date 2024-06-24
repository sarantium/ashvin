#Release vs Deployment

### Distinguish between Releasing a Model and Deploying a System and the Implications for Regulation

The distinction between releasing a model and deploying a system is critical in understanding the practical implications of AI regulations like SB 1047.

- **Impact of Releasing a Model**: Releasing models, especially as open source, allows broad access and further innovation. However, the model itself is just a list of numbers and code, posing no inherent risk.

  Example: OpenAI's released weights and code can be freely used and modified by anyone.
  
  ```mermaid
  graph LR
    R[Released Model] --> |Distribute| D1[Developer 1]
    R --> |Distribute| D2[Developer 2]
    R --> |Distribute| D3[Developer 3]
  ```

- **Impact of Deploying a System**: Deploying a model involves its integration into an application or service, which can influence environments and thus has the potential to cause harm.

  Example: ChatGPT is a deployment using OpenAI’s models, providing a user interface for interaction.
  
  ```mermaid
  graph LR
    A[Application] --> B((Model))
    B --> C[User Interaction]
  ```