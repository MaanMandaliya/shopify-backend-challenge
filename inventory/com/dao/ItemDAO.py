from inventory import db
from inventory.com.vo.ItemVO import ItemVO

class ItemDAO:
    def insertItem(self, itemVO):
        db.session.add(itemVO)
        db.session.commit()

    def viewItem(self, itemVO):
        item = ItemVO.query.get(itemVO.itemId)
        return item

    def viewAllItems(self):
        items = ItemVO.query.all()
        return items

    def viewFilteredItems(self, itemVO):
        items = ItemVO.query.filter_by(isDeleted=itemVO.isDeleted).all()
        return items
    
    def deleteItem(self, itemVO):
        # Soft Delete method
        selectedItem = ItemVO.query.get(itemVO.itemId)
        selectedItem.isDeleted = True
        selectedItem.deletionComment = itemVO.deletionComment
        db.session.merge(selectedItem)
        db.session.commit()

    def updateItem(self, itemVO):
        db.session.merge(itemVO)
        db.session.commit()