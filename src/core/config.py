from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Config(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


config = Config()
