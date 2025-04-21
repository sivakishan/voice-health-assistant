from opperai import Opper
from pydantic import BaseModel, Field

opper = Opper()

class ResponseModel(BaseModel):
    reply: str = Field(description="Assistant's response")

def ask_gpt(prompt):
    output, _ = opper.call(
        name="healthcare_assistant",
        instructions="Provide medical advice based on the user's input.",
        input={"user_input": prompt},
        output_type=ResponseModel,
    )
    return output.reply
