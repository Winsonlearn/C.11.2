"""Add full element fields

Revision ID: 99d0447e4869
Revises: 
Create Date: 2025-05-28 23:41:44.786036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d0447e4869'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('element',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('atomic_number', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('atomic_mass', sa.Float(), nullable=False),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('element_type', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('appearance', sa.String(length=255), nullable=True),
    sa.Column('boil', sa.Float(), nullable=True),
    sa.Column('density', sa.Float(), nullable=True),
    sa.Column('discovered_by', sa.String(length=255), nullable=True),
    sa.Column('melt', sa.Float(), nullable=True),
    sa.Column('molar_heat', sa.Float(), nullable=True),
    sa.Column('named_by', sa.String(length=255), nullable=True),
    sa.Column('phase', sa.String(length=50), nullable=True),
    sa.Column('source', sa.String(length=255), nullable=True),
    sa.Column('bohr_model_image', sa.String(length=255), nullable=True),
    sa.Column('bohr_model_3d', sa.String(length=255), nullable=True),
    sa.Column('spectral_img', sa.String(length=255), nullable=True),
    sa.Column('xpos', sa.Integer(), nullable=True),
    sa.Column('ypos', sa.Integer(), nullable=True),
    sa.Column('shells', sa.Text(), nullable=True),
    sa.Column('electron_configuration', sa.String(length=255), nullable=True),
    sa.Column('electron_configuration_semantic', sa.String(length=255), nullable=True),
    sa.Column('electron_affinity', sa.Float(), nullable=True),
    sa.Column('electronegativity_pauling', sa.Float(), nullable=True),
    sa.Column('ionization_energies', sa.Text(), nullable=True),
    sa.Column('cpk_hex', sa.String(length=10), nullable=True),
    sa.Column('image_title', sa.String(length=255), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('image_attribution', sa.Text(), nullable=True),
    sa.Column('block', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('element', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_element_atomic_number'), ['atomic_number'], unique=True)
        batch_op.create_index(batch_op.f('ix_element_name'), ['name'], unique=True)
        batch_op.create_index(batch_op.f('ix_element_symbol'), ['symbol'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('element', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_element_symbol'))
        batch_op.drop_index(batch_op.f('ix_element_name'))
        batch_op.drop_index(batch_op.f('ix_element_atomic_number'))

    op.drop_table('element')
    # ### end Alembic commands ###
