"""elimar relaciones de rol y user

Revision ID: a0110c71204a
Revises: 166d39dc7fee
Create Date: 2025-08-20 13:44:06.312984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0110c71204a'
down_revision: Union[str, None] = '166d39dc7fee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Elimina directamente la tabla sin preocuparte por las relaciones
    op.drop_table("user_rols")


def downgrade() -> None:
    # Restaura la tabla con sus columnas y claves foráneas
    op.create_table(
        "user_rols",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("rol_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.ForeignKeyConstraint(["rol_id"], ["rols.id"]),
    )

