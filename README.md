# 🦜️🔗 LangChain

Large language models (LLMs) are emerging as a transformative technology, enabling developers to build applications that they previously could not. However, using these LLMs in isolation is often insufficient for creating a truly powerful app - the real power comes when you can combine them with other sources of computation or knowledge.

This library aims to assist in the development of those types of applications. Common examples of these applications include:

- ❓ Question Answering over specific documents
- 💬 Chatbots
- 🤖 Agents

## How it can useful ?

There are six main areas that LangChain is designed to help with. These are, in increasing order of complexity:

📃 LLMs and Prompts:

This includes prompt management, prompt optimization, a generic interface for all LLMs, and common utilities for working with LLMs.

🔗 Chains:

Chains go beyond a single LLM call and involve sequences of calls (whether to an LLM or a different utility). LangChain provides a standard interface for chains, lots of integrations with other tools, and end-to-end chains for common applications.

📚 Data Augmented Generation:

Data Augmented Generation involves specific types of chains that first interact with an external data source to fetch data for use in the generation step. Examples include summarization of long pieces of text and question/answering over specific data sources.

🤖 Agents:

Agents involve an LLM making decisions about which Actions to take, taking that Action, seeing an Observation, and repeating that until done. LangChain provides a standard interface for agents, a selection of agents to choose from, and examples of end-to-end agents.

🧠 Memory:

Memory refers to persisting state between calls of a chain/agent. LangChain provides a standard interface for memory, a collection of memory implementations, and examples of chains/agents that use memory.

🧐 Evaluation:

[BETA] Generative models are notoriously hard to evaluate with traditional metrics. One new way of evaluating them is using language models themselves to do the evaluation. LangChain provides some prompts/chains for assisting in this.


## What we built

Here, we are  building  a streamlit app to create and explore prompts and chains in [LangChain](https://python.langchain.com/en/latest/) library.

This streamlit app is used to give the response about the  celebrity , his date of birth  and give 5 major events happened around his dob in the world by taking the celebrity name as Prompt.

To run the streamlit app:
```bash
cd Langchain
```

```bash
streamlit run CelebritySearchResults.py
```
For more information on these topics, you can follow this [documentation](https://python.langchain.com/en/latest/).
