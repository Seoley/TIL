from mingpt.model import GPT
from mingpt.trainer import Trainer

def make_instance():
    model_config = GPT.get_default_config()
    model_config.model_type = 'gpt2'
    model_config.vocab_size = 50257 # openai's model vocabulary
    model_config.block_size = 1024  # openai's model block_size (i.e. input context length)
    model = GPT(model_config) 


if __name__ == "__main__":
    make_instance()