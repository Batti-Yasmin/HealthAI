from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the IBM Granite model from Hugging Face
model_id = "ibm-granite/granite-3.3-2b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)

def ask_ibm_granite(prompt: str, max_tokens: int = 256) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result.strip()
