import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Safely set LangSmith key if available
ls_key = os.getenv("LANGSMITH_API_KEY")
if ls_key:
    os.environ["LANGSMITH_API_KEY"] = ls_key

# APIs
@app.post("/blogs")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic","")
    
    ## get the llm object 
    groq_llm=GroqLLM()
    llm = groq_llm.get_llm()

    # get the graph
    graph_builder = GraphBuilder(llm)
    if topic:
        # We pass "topic" as the usecase type for now
        graph = graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic": topic})
    
    return {"data":state}

if __name__=="__main__":
    uvicorn.run("app:app", host="0.0.0.0",port=8000, reload=True)
        