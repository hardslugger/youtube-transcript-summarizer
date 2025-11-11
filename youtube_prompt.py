from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template = """ You are a Youtube Summary Generator. Below is the transcript of the Youtube video. Summarize it.
    Transcript - 
    {text_file_content}
""",
input_variables=['text_file_content']
)

template.save('yt_template.json')