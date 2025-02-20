# AnalyzingContractClausesForConflictsAndSimilarities Crew

# Hacknight 2/19/2025
Install crewai
uv pip install crewai




1. Update the knowledge directory to take different files (Could use kaggle data)
2. Update pre_process_weaviate.py to take different files
3. Add env variables
    - OPENAI_API_KEY
    - WEAVIATE_URL
    - WEAVIATE_API_KEY
4. Update your agents.yaml and tasks.yaml
5. Upload your crew to Github
6. Run your crew: `crewai run`
7. Deploy your crew to github
8. Sign up for a free account on crewai.com
9. Sync your github repo to crewai.com
10. Deploy your crew to crewai.com (takes a few minutes) and be sure to add your env variables
11. Use the management ui to run your crew



Welcome to the AnalyzingContractClausesForConflictsAndSimilarities Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/analyzing_contract_clauses_for_conflicts_and_similarities/config/agents.yaml` to define your agents
- Modify `src/analyzing_contract_clauses_for_conflicts_and_similarities/config/tasks.yaml` to define your tasks
- Modify `src/analyzing_contract_clauses_for_conflicts_and_similarities/crew.py` to add your own logic, tools and specific args
- Modify `src/analyzing_contract_clauses_for_conflicts_and_similarities/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the analyzing_contract_clauses_for_conflicts_and_similarities Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The analyzing_contract_clauses_for_conflicts_and_similarities Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the AnalyzingContractClausesForConflictsAndSimilarities Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
