from langchain_core.globals import set_llm_cache
from langchain_community.cache import InMemoryCache, SQLiteCache

def enable_caching(cache_type="None"):
    if cache_type == "In-Memory":
        set_llm_cache(InMemoryCache())
    elif cache_type == "SQLite":
        set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))
    else:
        set_llm_cache(None)