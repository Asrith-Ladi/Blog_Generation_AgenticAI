from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
        self.blog_node_obj = BlogNode(self.llm)

    def build_topic_graph(self):
        """
        Build a graph to generate based on the topic
        """
        ## Nodes

        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    
    def build_language_graph(self):
        """Building a graph for blog generation with inputs topic and language
        """

        print(self.llm)

        # Nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_creation",self.blog_node_obj.content_generation)    

    def setup_graph(self, usecase):
        if usecase == "topic":
            return self.build_topic_graph()

## Below code is for langsmith langgraph studio

llm=GroqLLM().get_llm()

## get the graph
graph = GraphBuilder(llm).build_topic_graph().compile()

## In the langgraph.json we shared the path of this file in dependencies
# we created graph_builder variable to handle the responsibility of compiled graph

##