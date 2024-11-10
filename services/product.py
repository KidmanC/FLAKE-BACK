from models.product import Product as ProductModel
from schemas.product import Product

class ProductService:
    def __init__(self, db):
        self.db = db

    def get_product_by_id(self, product_id):
        return self.db.query(ProductModel).filter(ProductModel.id == product_id).first()

    def get_products(self):
        return self.db.query(ProductModel).all()
    
    def add_product(self, product: Product):
        new_product = ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return new_product

    def update_product(self, product_id, product: Product):
        query = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not query:
            return None
        query.name = product.title
        query.brand = product.brand
        query.created_by = product.created_by
        self.db.commit()
        return query

    def delete_product(self, product_id):
        product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not product:
            return None
        self.db.delete(product)
        self.db.commit()
        return product