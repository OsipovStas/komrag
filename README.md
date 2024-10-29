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

![Comparison of RAG Metrics](https://raw.githubusercontent.com/OsipovStas/komrag/resources/avg_metrics_comparison.jpg)

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


