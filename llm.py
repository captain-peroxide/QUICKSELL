import os
from accelerate import disk_offload
import torch
from langchain.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.embeddings import HuggingFaceEmbeddings

def llm():
    model_kwargs = {'device': 'cpu'}
    embeddings = HuggingFaceEmbeddings()
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M", low_cpu_mem_usage=True)
    disk_offload(model=model, offload_dir="offload")

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=150)
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm, embeddings