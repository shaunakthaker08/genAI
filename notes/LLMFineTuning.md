## Model evaluation

### ROUGE (Recall Oriented Understudy for Gisty Evaluation)

Comparison of LLM generated output with reference or set of references (human generated) for text sumnmarization.

**ROUGE-1**

$$
\text{ROUGE-1 Recall} = \frac{\text{number of unigram matches}}{\text{number of unigrams in reference}}
$$

$$
\text{ROUGE-1 Precision} = \frac{\text{number of unigram matches}}{\text{number of unigrams in output}}
$$

$$
\text{ROUGE-1 F1} = {2} \times \frac{\text{precision} \times \text{recall}}{\text{precision} + \text{recall}}
$$

**ROUGE - 2** : It compares bigrams of output with reference. Replace unigrams with bigrams in above formula

**ROUGE - L**: It compares LCS (Largest common subsequence) of output with reference.

$$
\text{ROUGE-L Recall} = \frac{\text{LCS(output, reference)}}{\text{number of unigrams in reference}}
$$

$$
\text{ROUGE-L Precision} = \frac{\text{LCS(output, reference)}}{\text{number of unigrams in output}}
$$

### BLEU (Bilingual Evaluation Understudy)
$$
\text{BLEU} = Avg(\text{precision across n-gram sizes})
$$
This focusses on precision hence it is more suitable for machine translation.

### Benchmarks

Benchmarks evaluate performance of LLM using standardized tests which includes predefined datasets, tasks and scoring mechanisms.

3 step process: Identify dataset across multiple tasks, Testing to run all desired tasks, Evaluation for scoring mechanism.

**HELM (Holistic evaluation of language models)**

Research paper: https://arxiv.org/pdf/2211.09110

**Key takeaways:**
1. Use multi metric approach for evaluation. This includes fairness, bias, toxicity, etc.
2. It has broad coverage of capabilities and risks. 
3. HELM has a top down approach which starts by defining scenarios and metrics required to be validated and then identifying corresponding dataset to run the test case.

## Instruction fine tuning


## Parameter efficient fine tuninig (PEFT)

Reference: https://www.ibm.com/think/topics/parameter-efficient-fine-tuning

PEFT works by freezing most of pretrained parameters while adding/re-training few trainable parameters.

**Benefits:**
1. Reduces storage cost for fine tuning as the output is not a new model with same size.
2. No catastrophic forgetting as most of the parameters are frozen.
3. Lower compute needs than full retraining.

### LORA

### Prompt tuning: Soft Prompts
