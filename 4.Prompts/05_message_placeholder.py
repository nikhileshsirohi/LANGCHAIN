from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support expert'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# load chat history
chat_history = []
with open('4.Prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create our prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query': 'When will my order arrive'})

print(prompt)