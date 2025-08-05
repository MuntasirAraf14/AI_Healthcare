modules = [
    'category_encoders',
    'langchain',
    'langchain_community',
    'langchain_huggingface',
    'huggingface_hub',
    'sentence_transformers',
    'faiss',
    'transformers',
    'torch'
]

for module in modules:
    try:
        __import__(module)
        print(f"✅ {module} imported successfully")
    except ImportError as e:
        print(f"❌ {module} error: {e}")