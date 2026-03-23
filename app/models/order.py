from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime
from datetime import datetime
from typing import List

class Order(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    items: Mapped[List["OrderItem"]] = relationship(back_populates="order")

    def __repr__(self):
        return f"<Order {self.id}>"

class OrderItem(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)
    artwork_id: Mapped[int] = mapped_column(ForeignKey("artwork.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    order: Mapped["Order"] = relationship(back_populates="items")
    artwork = relationship("Artwork")

    def __repr__(self):
        return f"<OrderItem order={self.order_id} artwork={self.artwork_id}>"