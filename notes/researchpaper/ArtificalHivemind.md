Research paper: https://arxiv.org/pdf/2510.22954

### Artificial Hivemind effect
1. Intra-model homogenity: Single model provides repitive outputs.
2. Inter-model homogenity: Different models converge on similar ideas with minor variations in phrasing.

The paper introduces a dataset of 26K real world open ended queries like "What should I learn in software development to be relevant in future" or "Write me a essay". These queries can have diverse answers.

### Key findings
1. **Intra-model repetition** – A single language model, when sampled multiple times on the same open-ended prompt, tends to produce highly similar outputs, indicating a significant lack of output diversity within the same model.
2. **Inter-model homogeneity** – Different models (including distinct architectures and training corpora) produce strikingly similar outputs on the same open-ended queries, demonstrating convergence or homogenization across models.
3. **Mismatch with human preference plurality** – Models and model-based judges (e.g., reward models used for alignment) are less well calibrated to the range of human preferences elicited by open-ended tasks; they tend to converge toward “safe” or average responses rather than capturing the full spectrum of human subjectivity.

### Sample prompt demonstrating the issue
![alt](../img/Artificial_Hivemind.png)

### Why does LLM suffer with Artificial Hivemind effect
Possible issues highlighted (not conclusive):
1. Models prioritize correctness over diversity
2. Similarity in training data across multiple language models.
3. Reward models overvalues one of the completion from equally high quality completions. Reward models does not capture equivalence of diverse responses.
4. Models are primarily trained on datasets with higher human agreement for the response hence lacks diversity in training.

### Why does it matter?
Issues I can think of due to Artificial hivemind:
1. Loss of diversity and creativity: This particularly impacts tasks with creative writing and generating new ideas.
2. Long-term homogenization of human thought: This can occur due to repeated exposure to similar outputs. As a side effect can result into risk of reinforcing dominant norms and biases.