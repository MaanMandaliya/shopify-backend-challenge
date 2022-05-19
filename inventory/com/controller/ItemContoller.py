from flask import render_template, redirect, request, url_for

from inventory import app
from inventory.com.dao.ItemDAO import ItemDAO
from inventory.com.vo.ItemVO import ItemVO


@app.route("/", methods=['GET'])
def getInventoryItems():
    try:
        itemVO = ItemVO()
        itemVO.isDeleted = False
        itemDAO = ItemDAO()
        items = itemDAO.viewFilteredItems(itemVO)
        print(items)
        return render_template('index.html', items=items)
    except Exception as exception:
        print(exception)


@app.route("/inventory/addItem", methods=['GET'])
def addInventoryItem():
    try:
        return render_template('addItem.html')
    except Exception as exception:
        print(exception)


@app.route("/inventory/insertItem", methods=['POST'])
def insertInventoryItem():
    try:
        itemVO = ItemVO()
        itemVO.itemName = request.form['itemName']
        itemVO.itemPrice = request.form['itemPrice']
        itemVO.itemQuantity = request.form['itemQuantity']
        itemDAO = ItemDAO()
        itemDAO.insertItem(itemVO)
        return redirect(url_for('getInventoryItems'))
    except Exception as exception:
        print(exception)


@app.route("/inventory/editItem", methods=['GET'])
def editInventoryItem():
    try:
        itemId = request.args.get('itemId')
        itemVO = ItemVO()
        itemVO.itemId = itemId
        itemDAO = ItemDAO()
        item = itemDAO.viewItem(itemVO)
        return render_template('editItem.html', item=item)
    except Exception as exception:
        print(exception)


@app.route("/inventory/updateItem", methods=['POST'])
def updateInventoryItem():
    try:
        itemVO = ItemVO()
        itemVO.itemId = request.form['itemId']
        itemVO.itemName = request.form['itemName']
        itemVO.itemQuantity = request.form['itemQuantity']
        itemVO.itemPrice = request.form['itemPrice']
        itemDAO = ItemDAO()
        itemDAO.updateItem(itemVO)
        return redirect(url_for('getInventoryItems'))
    except Exception as exception:
        print(exception)


@app.route("/inventory/deleteItem", methods=['GET'])
def deleteInventoryItem():
    try:
        itemId = request.args.get('itemId')
        itemVO = ItemVO()
        itemVO.itemId = itemId
        itemDAO = ItemDAO()
        item = itemDAO.viewItem(itemVO)
        return render_template('deleteItem.html', item=item)
    except Exception as exception:
        print(exception)


@app.route("/inventory/softDeleteItem", methods=['POST'])
def softDeleteInventoryItem():
    try:
        itemVO = ItemVO()
        itemVO.itemId = request.form['itemId']
        itemVO.isDeleted = True
        itemVO.deletionComment = request.form['deletionComment']
        itemDAO = ItemDAO()
        itemDAO.updateItem(itemVO)
        return redirect(url_for('getInventoryItems'))
    except Exception as exception:
        print(exception)


@app.route("/inventory/undeleteItems", methods=['GET'])
def undeleteInventoryItems():
    try:
        itemVO = ItemVO()
        itemVO.isDeleted = True
        itemDAO = ItemDAO()
        items = itemDAO.viewFilteredItems(itemVO)
        return render_template('undeleteItems.html', items=items)
    except Exception as exception:
        print(exception)


@app.route("/inventory/undeleteItem", methods=['POST'])
def undeleteInventoryItem():
    try:
        itemVO = ItemVO()
        itemVO.itemId = request.args.get('itemId')
        itemVO.isDeleted = False
        itemVO.deletionComment = None
        itemDAO = ItemDAO()
        itemDAO.updateItem(itemVO)
        return redirect(url_for('getInventoryItems'))
    except Exception as exception:
        print(exception)
