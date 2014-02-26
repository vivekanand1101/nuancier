"""Add start and stop date and time

Revision ID: 22da948cbe48
Revises: None
Create Date: 2013-12-01 18:18:41.647140

"""

# revision identifiers, used by Alembic.
revision = '22da948cbe48'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ''' Add the election_date_start and election_date_end columns to the
    Elections table '''
    op.add_column(
        'Elections',
        sa.Column('election_date_start', sa.Date)
    )
    op.add_column(
        'Elections',
        sa.Column('election_date_end', sa.Date)
    )

    # This is required for prod as there is already an election in the DB
    try:
        ins = "UPDATE \"Elections\" SET election_date_start='2013-10-05';"
        op.execute(ins)
        ins = "UPDATE \"Elections\" SET election_date_end='2013-10-04';"
        op.execute(ins)
    except:
        pass

    ## Enforce the nullable=False
    op.alter_column('Elections', 'election_date_start', nullable=False)
    op.alter_column('Elections', 'election_date_end', nullable=False)


def downgrade():
    ''' Remove the columns election_date_start and election_date_end from the
    Elections table. '''
    op.drop_column('Elections', 'election_date_start')
    op.drop_column('Elections', 'election_date_end')
