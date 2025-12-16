## Types of Transformer model

In the Transformer model, the **encoder** processes the input sequence to create a rich, contextual representation, while the **decoder** uses this representation to generate the output sequence word-by-word. The encoder focuses on understanding the input, using self-attention to weigh the relationships between tokens, and the decoder focuses on generating the output, using self-attention on its own generated tokens and encoder-decoder attention to focus on relevant parts of the encoder's output.

Research paper: https://arxiv.org/pdf/1706.03762

### Encoder based model (Auto encoding model)

**Where is this being used?:** Designed to understand the context of the tokens in the text/sentence. This can be useful for tasks like text/document classification, sentiment analysis, Named entity recognition (Identifying key information from unstructured text like people, organization, location).

BERT: https://arxiv.org/pdf/1810.04805

### Decorder based model (Auto regressive model)

**Where is this being used?:** Decoder-based transformer models are used in applications that require sequential generation and strong contextual understanding. Common use cases include natural language generation tasks such as text completion, chatbots, conversational agents, summarization, and machine translation (particularly on the target-language side).

### Encoder-Decoder model (Sequence to sequence model)

**Where is this being used?:** Sequence-to-sequence (Seq2Seq) models are used in problems where an input sequence must be transformed into a different output sequence, often with a different length and structure. They are widely applied in machine translation (e.g., translating sentences between languages), text summarization, and question answering.

