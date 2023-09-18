from pydantic import BaseModel, field_validator

class User(BaseModel):
    id: int
    name: str

    @field_validator("name")
    def validate_name(cls, value):
        is_size_ok = len(value) < 10
        if not is_size_ok:
            raise ValueError("The name should be less than 10 characters.")
