# pip install strands-harness
from strands_harness import create_harness

agent = create_harness(model="global.amazon.nova-2-lite-v1:0")
#agent("Research the top three vector databases, compare pricing and limits, and write it up in comparison.md")
agent("Write the result of the previous interaction in c:\\tmp\\comparison.md")