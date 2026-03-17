from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        sefl.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate based on the topic
        """
        ## Nodes

        self.graph.add_node("title_creation", )
        self.graph.add_node("content_generation")

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_ege("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph