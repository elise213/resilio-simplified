"""empty message

Revision ID: e7858665cfd4
Revises: c64b9357c3a5
Create Date: 2023-04-11 12:57:11.582499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7858665cfd4'
down_revision = 'c64b9357c3a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Drop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('identification', sa.String(length=500), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FavoriteOfferings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Offering',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('offering_type', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('image2', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=256), nullable=True),
    sa.Column('category', sa.String(length=256), nullable=True),
    sa.Column('website', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('latitude', sa.String(length=250), nullable=True),
    sa.Column('longitude', sa.String(length=250), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('image2', sa.String(length=500), nullable=True),
    sa.Column('logo', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('is_org', sa.String(length=80), nullable=False),
    sa.Column('avatar', sa.String(length=80), nullable=True),
    sa.Column('picture', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.Column('comment_cont', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('parentId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parentId'], ['Comment.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['Resource.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mondayStart', sa.String(length=256), nullable=True),
    sa.Column('mondayEnd', sa.String(length=256), nullable=True),
    sa.Column('tuesdayStart', sa.String(length=256), nullable=True),
    sa.Column('tuesdayEnd', sa.String(length=256), nullable=True),
    sa.Column('wednesdayStart', sa.String(length=256), nullable=True),
    sa.Column('wednesdayEnd', sa.String(length=256), nullable=True),
    sa.Column('thursdayStart', sa.String(length=256), nullable=True),
    sa.Column('thursdayEnd', sa.String(length=256), nullable=True),
    sa.Column('fridayStart', sa.String(length=256), nullable=True),
    sa.Column('fridayEnd', sa.String(length=256), nullable=True),
    sa.Column('saturdayStart', sa.String(length=256), nullable=True),
    sa.Column('saturdayEnd', sa.String(length=256), nullable=True),
    sa.Column('sundayStart', sa.String(length=256), nullable=True),
    sa.Column('sundayEnd', sa.String(length=256), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resource_id'], ['Resource.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('Schedule')
    op.drop_table('Comment')
    op.drop_table('User')
    op.drop_table('Resource')
    op.drop_table('Offering')
    op.drop_table('Favorites')
    op.drop_table('FavoriteOfferings')
    op.drop_table('Drop')
    # ### end Alembic commands ###
