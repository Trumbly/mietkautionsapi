from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class BaseModelWithUUID(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique identifier") 