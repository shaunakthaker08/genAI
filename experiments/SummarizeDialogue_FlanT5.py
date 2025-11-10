from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig

# Load dataset
huggingface_dataset_name = "knkarthick/dialogsum"
dataset = load_dataset(huggingface_dataset_name)

# Load model and tokenizer
model_name = 'google/flan-t5-base'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

# Helper function for in-context learning prompt construction
def make_prompt(example_indices_full, example_index_to_summarize):
    prompt = ''
    for index in example_indices_full:
        dialogue = dataset['test'][index]['dialogue']
        summary = dataset['test'][index]['summary']
        
        # The stop sequence '{summary}\n\n\n' helps FLAN-T5 understand section boundaries
        prompt += f"""
Dialogue:

{dialogue}

What was going on?
{summary}


"""
    
    dialogue = dataset['test'][example_index_to_summarize]['dialogue']
    
    prompt += f"""
Dialogue:

{dialogue}

What was going on?
"""
        
    return prompt

# Example setup for few-shot learning
example_indices = [40, 200]
dash_line = '-' * 100

example_indices_full = [40]
example_index_to_summarize = 200

# Build prompt
few_shot_prompt = make_prompt(example_indices_full, example_index_to_summarize)

print(few_shot_prompt)

# Reference summary
summary = dataset['test'][example_index_to_summarize]['summary']

# Generation config
generation_config = GenerationConfig(max_new_tokens=100, do_sample=True, temperature=0.5)

# Generate summary
inputs = tokenizer(few_shot_prompt, return_tensors='pt')
outputs = model.generate(
    inputs["input_ids"],
    generation_config=generation_config,
)
output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Display results
print(dash_line)
print(f'BASELINE HUMAN SUMMARY:\n{summary}\n')
print(dash_line)
print(f'MODEL GENERATION - ONE SHOT:\n{output_text}')
