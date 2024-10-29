# Comprehensive Baby Care Guide

Welcome to the "Comprehensive Baby Care Guide" project!

This tool is designed to assist new parents in caring for their newborn, based on a curated set of books and authoritative sources on child health and development.

Our project aims to:
- Simplify the overwhelming task of infant care
- Provide easy-to-follow guidelines
- Offer practical tips and evidence-based recommendations

The guide covers all aspects of early childcare, including:
- Feeding schedules
- Sleep routines
- Common health concerns
- Developmental milestones

We've distilled a wealth of knowledge from respected pediatric resources into an accessible, user-friendly format.

Whether you're a first-time parent or looking to refresh your knowledge, this project offers valuable insights to help you navigate the challenges of caring for your little one with confidence.

## User Interface

Our application features a user-friendly chatbot interface, designed to provide quick and accurate answers to your childcare questions.

Key features:
- **Chatbot Interface**: Interact naturally by asking questions about baby care.
- **RAG Architecture**: Utilizes Retrieval-Augmented Generation for accurate and context-aware responses.
- **Streamlit UI**: Clean, responsive design that works well on both desktop and mobile devices.

The app is built using state-of-the-art natural language processing techniques, ensuring that you receive the most relevant and up-to-date information for your queries.

Try it out now: [Baby Care Guide Chatbot](https://komrag-1.streamlit.app/)

## Evaluation

We have conducted a comprehensive evaluation of our RAG (Retrieval-Augmented Generation) system using the RAGAS library. The evaluation focuses on key metrics for both the generator and retriever components of our system.

![Comparison of RAG Metrics](https://github.com/OsipovStas/komrag/blob/main/resources/avg_metrics_comparison.jpg)

### Metrics Explained:
- **Generator Metrics**:
  - Faithfulness: Measures how well the generated response aligns with the retrieved context.
  - Response Relevancy: Assesses how relevant the generated response is to the given query.
- **Retriever Metrics**:
  - Context Precision: Evaluates the accuracy of the retrieved context.
  - Context Recall: Measures how well the system retrieves all relevant information.

### Key Findings:
- Our system demonstrates strong performance across all evaluated models, with total average scores consistently above 0.88.
- The llama-3.2 hybrid model shows the highest overall performance, with a total average score of 0.92.
- Generator performance (faithfulness and relevancy) is generally higher than retriever performance (precision and recall) across all models.
- The gpt4-mini models show consistent performance in both hybrid and dense configurations.

These results indicate that our RAG system is effective in retrieving relevant information and generating faithful and relevant responses across different model configurations.

For a more detailed breakdown of the evaluation results, including specific scores for each metric and model, please visit our MLflow dashboard:

[Detailed Evaluation Results on MLflow](https://dagshub.com/OsipovStas/komrag-old/experiments)

This comprehensive evaluation ensures that our Baby Care Guide provides accurate and relevant information to parents, leveraging the strengths of advanced language models and efficient information retrieval.

## Ingestion Pipeline and Reproducibility

Our project includes an ingestion pipeline to process and prepare the data for the RAG (Retrieval-Augmented Generation) system. Currently, the ingestion process is implemented through a series of exploratory notebooks.

To reproduce the ingestion and RAG preparation steps:

1. Navigate to the `notebooks` folder in the repository.
2. You'll find a collection of Jupyter notebooks that guide you through the entire process.
3. These notebooks cover various stages, including:
   - Data collection and cleaning
   - Text preprocessing
   - Embedding generation
   - Vector store creation
   - RAG system setup

By following these notebooks, you can understand and replicate our data ingestion pipeline, allowing you to prepare your own data for use with the Baby Care Guide chatbot.

Please note that these notebooks are primarily for exploration and demonstration purposes. In future updates, we plan to refactor this process into a more streamlined, production-ready pipeline.

For any questions or issues related to the ingestion process, please refer to the documentation within each notebook or raise an issue in the GitHub repository.


## Monitoring and Containerization

We are currently in the process of enhancing our project's infrastructure and observability. This section outlines our ongoing efforts in monitoring and containerization.

### Work in Progress

- **Monitoring**: We are developing a comprehensive monitoring solution to track the performance, usage, and health of our application. This will include:
  - Real-time performance metrics
  - Usage statistics
  - Error logging and alerting
  - User interaction analysis

- **Containerization**: To improve deployment consistency and scalability, we are working on containerizing our application. This involves:
  - Creating Docker containers for the application and its dependencies
  - Developing Docker Compose files for easy local development and testing
  - Preparing Kubernetes manifests for potential cloud deployments

These enhancements are aimed at improving the reliability, scalability, and maintainability of our Baby Care Guide chatbot. We appreciate your patience as we work on implementing these features.

Stay tuned for updates in this space. Once completed, this section will provide detailed information on how to use our monitoring tools and containerized deployment options.

## Deployment and RAG Implementation

### Streamlit Cloud Deployment

Our Baby Care Guide chatbot is deployed and readily accessible on Streamlit Cloud. This allows users to interact with the application directly through their web browsers without any local setup. You can access the live application here:

[Baby Care Guide Chatbot on Streamlit Cloud](https://komrag-1.streamlit.app/)

### RAG Pipeline

The Retrieval-Augmented Generation (RAG) pipeline in our application utilizes a sophisticated hybrid search approach:

1. **Hybrid Search**: We combine the strengths of multiple search techniques to ensure comprehensive and accurate information retrieval.

2. **Dense Vector Search**: This method uses semantic similarity to find relevant information, allowing the system to understand and match the context of queries beyond simple keyword matching.

3. **Additional Search Methods**: Complementing the dense vector search, we employ other techniques (such as BM25 or exact matching) to capture different aspects of relevance.

This hybrid approach enables our chatbot to provide more accurate and contextually relevant responses to user queries about baby care. It balances the benefits of semantic understanding with the precision of traditional search methods, resulting in a more robust and reliable information retrieval system.

The combination of our cloud deployment and advanced RAG implementation ensures that users have access to a powerful, up-to-date, and user-friendly baby care information system.