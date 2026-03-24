import os
from typing import Any, Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class AgentOutputFileWriterSchema(BaseModel):
    """Input schema for AgentOutputFileWriter."""
    output_text: str = Field(..., description="The text content to be written to the file.")
    file_path: str = Field(..., description="The absolute or relative path where the output text should be written. If the file does not exist, it will be created. If it exists, it will be overwritten.")

class AgentOutputFileWriter(BaseTool):
    """
    AgentOutputFileWriter - A tool to write the agent's output to a text file.
    """
    name: str = "Agent Output File Writer"
    description: str = "A tool to write the output of the agent to a text file."
    args_schema: Type[BaseModel] = AgentOutputFileWriterSchema

    def _run(self, output_text: str, file_path: str) -> str:
        try:
            dir_name = os.path.dirname(file_path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(output_text)
            return f"Successfully wrote output to {file_path}"
        except Exception as e:
            return f"Error writing output to file: {str(e)}"