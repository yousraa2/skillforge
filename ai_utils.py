from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def ask_ai(prompt):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"⚠️ Python error: {str(e)}"
