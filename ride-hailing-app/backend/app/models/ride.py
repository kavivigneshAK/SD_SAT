from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.session import Base
from sqlalchemy.orm import relationship

class Ride(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    pickup_latitude = Column(Float)
    pickup_longitude = Column(Float)
    pickup_address = Column(String)
    drop_latitude = Column(Float)
    drop_longitude = Column(Float)
    drop_address = Column(String)
    estimated_distance_km = Column(Float)
    estimated_fare = Column(Float)
    final_fare = Column(Float, nullable=True)
    status = Column(String, default="REQUESTED") # REQUESTED, ACCEPTED, ARRIVED, IN_PROGRESS, COMPLETED, CANCELLED
    requested_at = Column(DateTime(timezone=True), server_default=func.now())
    accepted_at = Column(DateTime(timezone=True), nullable=True)
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    cancelled_at = Column(DateTime(timezone=True), nullable=True)
