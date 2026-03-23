from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

class CartItem(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    artwork_id: Mapped[int] = mapped_column(ForeignKey("artwork.id"), nullable=False)
    user = relationship("User")
    artwork = relationship("Artwork")

    def __repr__(self):
        return f"<CartItem user={self.user_id} artwork={self.artwork_id}>"