from sqlalchemy import Column, Integer, String, Float
from database.connection import Base


class MaterialModel(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(50), nullable=False)
    percentage_of_defective_material = Column(Float, nullable=False)

    def __repr__(self):
        return (
            f"<Material(id={self.id}, type='{self.type}', "
            f"percentage_of_defective_material={self.percentage_of_defective_material})>"
        )
