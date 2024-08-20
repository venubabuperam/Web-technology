from day4.requests.Items import Item


class ItemsSVC:

    def updateItem(self, q: str, item_id: int, item: Item):
        results = {"item_id": item_id}
        if q:
            results.update({"q": q})
        if item:
            results.update({"item": item})
        return results

    def deleteItem(self, q: str, item_id: int, item: Item):
        return True