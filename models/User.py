import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, Text, Date, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID

from classes.Password import Password
from models.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    _gurded = ['password']

    uuid = Column(UUID, unique=True)
    name = Column(Text, nullable=False, index=True)
    surname = Column(Text, nullable=False, index=True)
    second_name = Column(Text, nullable=True)
    photo_url = Column(Text)
    login = Column(Text, nullable=False, index=True)
    password = Column(Text, nullable=False)
    date_birthday = Column(Date)
    last_active = Column(DateTime)
    is_active = Column(Boolean, default=True)

    def add_default_data(self):
        password_helpers = Password()

        self.session.add_all([
            User(
                uuid=str(uuid.uuid4()),
                login='default',
                password=password_helpers.get_hash('default'),
                name='default',
                surname='user',
                second_name='user',
                date_birthday=datetime.now().date(),
                is_active=True,
                create_at=datetime.now().date(),
            )
        ])
        self.session.commit()

    def _manual_response_fields(self, result: dict) -> None:
        result['full_name'] = f'{self.surname} {self.name[0]}.{self.second_name[0] if self.second_name else ""}'
