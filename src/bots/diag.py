import sys
import os
import time

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")
    sys.stdout.flush()

log("Diagnostic script started")

log("Testing print and flush...")
log("Step 1 basic imports successful")

try:
    log("Step 2: Testing lark-oapi import...")
    import lark_oapi as lark
    log("lark-oapi import successful")
except Exception as e:
    log(f"lark-oapi import FAILED: {e}")

try:
    log("Step 3: Testing yaml import...")
    import yaml
    log("yaml import successful")
except Exception as e:
    log(f"yaml import FAILED: {e}")

try:
    log("Step 4: Testing pydantic import...")
    import pydantic
    log("pydantic import successful")
except Exception as e:
    log(f"pydantic import FAILED: {e}")

try:
    log("Step 5: Testing langchain components import...")
    from langchain_community.embeddings import HuggingFaceEmbeddings
    log("langchain embeddings import successful")
except Exception as e:
    log(f"langchain embeddings import FAILED: {e}")

log("Diagnostic script finished")
