"""user, submission, rating table

Revision ID: bd4a5ccb480d
Revises: 
Create Date: 2018-08-30 07:33:24.875506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd4a5ccb480d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_password_hash'), 'user', ['password_hash'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=80), nullable=True),
    sa.Column('link', sa.String(length=150), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_submission_date'), 'submission', ['date'], unique=False)
    op.create_index(op.f('ix_submission_description'), 'submission', ['description'], unique=False)
    op.create_index(op.f('ix_submission_image'), 'submission', ['image'], unique=False)
    op.create_index(op.f('ix_submission_link'), 'submission', ['link'], unique=False)
    op.create_index(op.f('ix_submission_title'), 'submission', ['title'], unique=False)
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('submission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['submission_id'], ['submission.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rating_rating'), 'rating', ['rating'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rating_rating'), table_name='rating')
    op.drop_table('rating')
    op.drop_index(op.f('ix_submission_title'), table_name='submission')
    op.drop_index(op.f('ix_submission_link'), table_name='submission')
    op.drop_index(op.f('ix_submission_image'), table_name='submission')
    op.drop_index(op.f('ix_submission_description'), table_name='submission')
    op.drop_index(op.f('ix_submission_date'), table_name='submission')
    op.drop_table('submission')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_password_hash'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
