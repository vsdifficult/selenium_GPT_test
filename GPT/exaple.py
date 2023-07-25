import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPTTrainer:
    def __init__(self, model_name):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def train(self, input_text):
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model(input_ids, labels=input_ids)
        loss = outputs.loss
        loss.backward()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
        optimizer.step()
        self.model.zero_grad()

    def generate_text(self, prompt, max_length=100):
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=max_length, num_return_sequences=1)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text

trainer = GPTTrainer('gpt2')
trainer.train("python")
generated_text = trainer.generate_text("This is a prompt for generating text.")
print(generated_text)