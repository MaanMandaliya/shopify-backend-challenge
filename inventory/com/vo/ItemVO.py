from inventory import db


class ItemVO(db.Model):
    __tablename__ = 'items'
    itemId = db.Column('itemId', db.Integer,
                       primary_key=True, autoincrement=True)
    itemName = db.Column('itemName', db.String(25))
    itemPrice = db.Column('itemPrice', db.Integer)
    itemQuantity = db.Column('itemQuantity', db.Integer)
    isDeleted = db.Column('isDeleted', db.Boolean, default=False)
    deletionComment = db.Column('deletionComment', db.String(30), default=None)

    def as_dict(self):
        return{
            'itemId': self.itemId,
            'itemName': self.itemName,
            'itemPrice': self.itemPrice,
            'itemQuantity': self.itemQuantity,
            'isDeleted': self.isDeleted,
            'deletionComment': self.deletionComment
        }


db.create_all()
