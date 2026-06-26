# Third-party sources and design provenance

The skills in this repository are original adaptations. They do not copy complete third-party skills. The following sources informed structure, activation, validation, and workflow design.

## Agent Skills format and progressive disclosure

- OpenAI Skills Catalog: https://github.com/openai/skills
- Agent Skills specification: https://github.com/agentskills/agentskills
- GitHub Agent Skills documentation: https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills

Concepts used:

- one self-contained folder per skill
- concise YAML activation metadata
- task-specific instructions, scripts, and references
- progressive disclosure rather than one oversized global prompt
- validation of skill names, structure, and catalog integrity

## Software engineering discipline

- Matt Pocock engineering skills: https://github.com/mattpocock/skills
- Obra Superpowers: https://github.com/obra/superpowers
- Awesome GitHub Copilot: https://github.com/github/awesome-copilot

Concepts used:

- reproduce and minimize before fixing
- root-cause analysis and falsifiable hypotheses
- test-first vertical slices
- architecture and ownership preservation
- evidence before completion claims
- technical evaluation of review comments
- durable worklogs rather than full transcript replay

## Scientific and medical research workflows

- K-Dense scientific agent skills: https://github.com/K-Dense-AI/scientific-agent-skills
- AIPOCH medical research skills: https://github.com/aipoch/medical-research-skills
- SciWrite manuscript review skill: https://github.com/labarba/sciwrite
- ByteDance DeerFlow academic review skills: https://github.com/bytedance/deer-flow

Concepts used:

- structured evidence synthesis
- explicit reporting-guideline checks
- citation verification
- separation of evidence, inference, and uncertainty
- protocol/manuscript consistency audits

## Document and artifact quality

- OpenAI document and PDF skills: https://github.com/openai/skills
- Anthropic document skill examples: https://github.com/anthropics/skills

Concepts used:

- native format generation
- render/open verification
- formula and layout validation
- delivery of the actual artifact rather than text-only output

## ChatGPT project architecture

- OpenAI Projects in ChatGPT documentation: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt

Concept used:

- project instructions, files, project chats, and project memory provide the shared context layer for recurring ChatGPT work

## License note

Each upstream repository has its own license. This repository uses general workflow concepts and independently written instructions. Before importing any third-party script, template, or substantial text, inspect and comply with the source file's license and attribution requirements.
